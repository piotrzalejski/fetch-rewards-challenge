# Fetch Coding Exercise - SDET
## Game
---
Given a balance scale and 9 gold bars of the same size and look. You don’t know the exact weight of each bar,
but you know they all weigh the same, except for one fake bar. It weighs less than others. You need to find the fake
gold bar by only bars and balance scales.
You can only place gold bars on scale plates (bowls) and find which scale weighs more or less.

## Website
---
Website http://sdetchallenge.fetch.com/ allows you to simulate the scaling process. You can write gold bar number(s)
in left and right bowl grids. Press the “Weigh” button and it will tell you which side weighs more or less or the same.
The weighing result will be shown in the “Weighing” list so you can track records.
After you are done with one weighing you can press the “Reset” button to reset the plates grid to empty values so you
can do another weighing.
When you find the fake gold bar click on the button with a number corresponding to the fake gold bar at the bottom of
the screen and check if you were right or wrong: an alert will pop up with two possible messages: “Yay! You found it!”
or “Oops! Try Again!”.
NOTE: Do not refresh the page as it will reset the fake bar to a random
NOTE: Buttons at the bottom with numbers DO NOT represent weights. It’s just the sequential number.
## Challenge
---
1. Play around with the website and find the best algorithm (minimum number of weighings for any possible
fake bar position) to find the fake gold bar.
2. Create the test automation project using any preferred language to perform
a. clicks on buttons (“Weigh”, “Reset”)
b. Getting the measurement results (field between the 'bowls')
c. filling out the bowls grids with bar numbers (0 to 8)
d. getting a list of weighing
e. Clicking on the gold bar number at the bottom of the website and checking for the alert message
3. Code the algorithm from step 1 which uses a set of actions from step 2 to find the fake gold bar
The algorithm should populate and weigh gold bars until a fake one is found, click on a fake bar number, output the
alert message, number of weighing, and list of weighing made.

## Requirements
___
### Python
- Check to see if python is installed
    ```
    $python --version
    Python 3.11.4
    ```
    If python is not installed you can go to https://www.python.org/downloads/
    to download and install

- Create a Virtual Environment:
    `$ ptyhon -m venv venv`
- Activate the virtual environment
    - On Windows:
        `.\venv\Scripts\activate`
    - on macOS and Linux:
        `$ source venv/bin/activate`
- Install dependencies from `requirements.txt`
    `$ pip install -r requirements.txt`

### Running the script
    `$ python fetch_coding_challenge.py`

### Clean up
- When you're don you can deactivate the virtual environment:
    `$ deactivate`