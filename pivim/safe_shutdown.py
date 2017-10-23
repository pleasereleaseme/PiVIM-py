"""
Module for.
"""
import warnings
import os
try: # Stop pylint genrating and error for libraries not availble on Windows or other OSes
    from signal import pause
    from gpiozero import Button
    from gpiozero import LEDBoard
except ImportError:
    pass

OFF_GPIO = 21
OFF_TIME = 6            # shut down after offtime seconds
MIN_TIME = 1            # notice switch after mintime seconds
ACTIVITY_LED_GPIO = 47  # activity LED
POWER_LED_GPIO = 35     # power LED

def shutdown(button):
    # find how long the button has been held
    p = button.pressed_time
    # blink rate will increase the longer we hold
    # the button down. E.g., at 2 seconds, use ¼ second rate.
    leds.blink(on_time=0.5/p, off_time=0.5/p)
    if p > OFF_TIME:
        os.system("sudo poweroff")

def when_pressed():
    # start blinking with ½ second rate
    leds.blink(on_time=0.5, off_time=0.5)

def when_released():
    # be sure to turn the LEDs off if we release early
    leds.off()

def init():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
    global leds
    leds = LEDBoard(ACTIVITY_LED_GPIO, POWER_LED_GPIO)

    btn = Button(OFF_GPIO, hold_time=MIN_TIME, hold_repeat=True)
    btn.when_held = shutdown
    btn.when_pressed = when_pressed
    btn.when_released = when_released
    pause()
