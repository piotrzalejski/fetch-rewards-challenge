import asyncio

from playwright.async_api import async_playwright, Playwright


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("http://sdetchallenge.fetch.com/")

    GROUPS = [[0,1,2], [3,4,5],[6,7,8]]

    buttons = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
    }

    async def fill_bars(page, bars, location):
        for i in range(len(bars)):
            # click the left or right grid and fill in bar
            await page.locator(f'#{location}_{i}').click()
            await page.locator(f'#{location}_{i}').fill(str(bars[i]))

    async def reset():
        # clear the grids
        await page.get_by_role("button", name="Reset").click()

    async def weigh_groups(group1, group2):
        await fill_bars(page, group1, 'left')
        await fill_bars(page, group2, 'right')
        await page.get_by_role("button", name="Weigh").click()

    async def weigh_result(lineitem):
        # wait for line items to appear
        await page.locator(".game-info li").nth(lineitem).is_visible()
        result_locator = page.locator(".game-info li").nth(lineitem)
        result_text = await result_locator.text_content()

        # Check if the result text contains '=', '>', or '<'
        if '=' in result_text:
            result = "Balanced"
        elif '>' in result_text:
            result = "Right"
        elif '<' in result_text:
            result = "Left"
        else:
            result = "Unknown"

        return result

    message = None
    expected = "Yay! You find it!"

    async def handle_dialog(dialog):
        # print(dialog.message)
        nonlocal message
        message = dialog.message
        await page.wait_for_timeout(1000)
        await dialog.dismiss()

    async def select_bar(button_name):
        nonlocal message
        page.on('dialog', handle_dialog)
        await page.get_by_role('button', name=button_name).click()

    async def play(groups):
        await weigh_groups(groups[0], groups[1])
        result = await weigh_result(0)

        if result == "Balanced":
            # Fake bar in 3rd group
            await reset()
            await weigh_groups(groups[2][:1], groups[2][1:2])
            second_result = await weigh_result(1)
            if second_result == "Balanced":
                await select_bar("8")
            elif second_result == "Left":
                await select_bar("6")
            elif second_result == "Right":
                await select_bar("7")
        elif result == "Right":
            await reset()
            await weigh_groups(groups[1][:1], groups[1][1:2])
            second_result = await weigh_result(1)
            if second_result == "Balanced":
                await select_bar("5")
            elif second_result == "Left":
                await select_bar("3")
            elif second_result == "Right":
                await select_bar("4")
        elif result == "Left":
            await reset()
            await weigh_groups(groups[0][:1], groups[0][1:2])
            second_result = await weigh_result(1)
            if second_result == "Balanced":
                await select_bar("2")
            elif second_result == "Left":
                await select_bar("0")
            elif second_result == "Right":
                await select_bar("1")

    await play(GROUPS)
    context.close()
    browser.close()


async def main():
    async with async_playwright() as pw:
        await run(pw)

if __name__ == "__main__":
    asyncio.run(main())