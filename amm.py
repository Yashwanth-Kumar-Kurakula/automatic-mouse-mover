import pyautogui as pag
import time
import random

def perform_random_clicks(x_range, y_range, click_interval):
    """
    Perform random mouse clicks within specified coordinates.

    Parameters:
    - x_range (tuple): Range of X coordinates (min, max).
    - y_range (tuple): Range of Y coordinates (min, max).
    - click_interval (int): Time in seconds between clicks.

    Returns:
    None
    """
    while True:
        # Generate random X and Y coordinates within the specified range.
        x = random.randint(*x_range)
        y = random.randint(*y_range)

        # Move the mouse cursor to the generated X and Y coordinates over a 1-second duration.
        pag.moveTo(x, y, 1)

        # Simulate a mouse click at the current cursor position.
        pag.click()

        # Pause the program for the specified interval before the next iteration.
        time.sleep(click_interval)

# Define constants for the range of X and Y coordinates
X_RANGE = (600, 700)
Y_RANGE = (200, 700)
CLICK_INTERVAL = 30  # Time in seconds between clicks

# Call the function with the defined constants
perform_random_clicks(X_RANGE, Y_RANGE, CLICK_INTERVAL)
