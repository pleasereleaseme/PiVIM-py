"""
Module for.
"""

import os
try: # Stop pylint genrating and error for libraries not availble on Windows or other OSes
    from signal import pause
    from gpiozero import Button
except ImportError:
    pass

OFF_GPIO = 21
HOLD_TIME = 6            # shut down after offtime seconds

# the function called to shut down the RPI
def shutdown():
    os.system("sudo poweroff")

button = Button(OFF_GPIO, hold_time=HOLD_TIME)
button.when_held = shutdown
pause()    # handle the button presses in the background
