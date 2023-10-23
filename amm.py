import pyautogui as pag
import time
import random

# Define constants for the range of X and Y coordinates
X_RANGE = (600, 700)
Y_RANGE = (200, 700)
CLICK_INTERVAL = 30  # Time in seconds between clicks

# Infinite loop to repeatedly execute the actions
while True:
    # Generate random X and Y coordinates within the specified range.
    x = random.randint(*X_RANGE)
    y = random.randint(*Y_RANGE)

    # Move the mouse cursor to the generated X and Y coordinates over a 1-second duration.
    pag.moveTo(x, y, 1)

    # Simulate a mouse click at the current cursor position.
    pag.click()

    # Pause the program for the specified interval before the next iteration.
    time.sleep(CLICK_INTERVAL)
