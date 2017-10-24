"""Module for controlling the Pimoroni Display-O-Tron HAT.

Display consists of 3 rows by 16 columns.
"""
import time
import os
from threading import Thread
try: # Stop pylint genrating and error for libraries not availble on Windows or other OSes
    from dothat import lcd
    from dothat import backlight
    from dothat import touch
except ImportError:
    pass

ROW_TOP_INDEX = 0
ROW_MID_INDEX = 1
ROW_BOTTOM_INDEX = 2
COL_LEFT_INDEX = 0
COL_RIGHT_INDEX = 15

BACKLIGHT_AUTO_OFF_DELAY = 10

SHUTDOWN_DELAY_COUNT = 0

def display_config():
    """Sets the display to display_configial values."""
    lcd.set_contrast(50)

    # Backlight is set to be on display_configially but to turn off after a delay
    backlight.hue(0.43)
    backlight_auto_off()

    touch.enable_repeat(True)

def display_off():
    """Turns the display off."""
    backlight.off()
    lcd.clear()

def clear_screen():
    """The screen usually needs to be cleared before writing any text
    to avoid text from previous writes being displayed.
    """
    lcd.clear()

    global SHUTDOWN_DELAY_COUNT
    SHUTDOWN_DELAY_COUNT = 0

def message_left_top(message):
    """Sets message at top left."""
    position_cursor_left(ROW_TOP_INDEX)
    lcd.write(message)

def message_left_middle(message):
    """Sets message at middle left."""
    position_cursor_left(ROW_MID_INDEX)
    lcd.write(message)

def message_left_bottom(message):
    """Sets message at bottom left."""
    position_cursor_left(ROW_BOTTOM_INDEX)
    lcd.write(message)

def message_right_top(message):
    """Sets message at top right."""
    position_cursor_right(message, ROW_TOP_INDEX)
    lcd.write(message)

def message_right_middle(message):
    """Sets non-null message at middle right."""
    position_cursor_right(message, ROW_MID_INDEX)
    lcd.write(message)

def message_right_bottom(message):
    """Sets message at bottom right."""
    position_cursor_right(message, ROW_BOTTOM_INDEX)
    lcd.write(message)

def position_cursor_right(message, row):
    """Calculates first position of a string that needs to be
    right-aligned based on the display being 16 characters wide.
    """
    if not message:             # If the message is empty just set the cursor to the last column
        cursor_position = COL_RIGHT_INDEX
    else:                       # Otherwise calculate starting position
        cursor_position = COL_RIGHT_INDEX - len(message)

    lcd.set_cursor_position(cursor_position, row)

def position_cursor_left(row):
    """Sets first position of a left-aligned string."""
    lcd.set_cursor_position(COL_LEFT_INDEX, row)

@touch.on(touch.LEFT)
def backlight_on(channel, event): # pylint: disable=unused-argument
    """Configures the left touch button to turn the backlight on."""
    display_config()
    backlight_auto_off()

@touch.on(touch.RIGHT)
def backlight_off(channel, event): # pylint: disable=unused-argument
    """Configures the right touch button to turn the backlight off."""
    backlight.off()

def backlight_auto_off():
    """Create a new thread from which to call a countdown timer
        to avoid blocking the main program.
    """
    thread = Thread(target=backlight_countdown)
    thread.start()

def backlight_countdown():
    """Turns the backlight off after the specified period has elapsed"""
    time.sleep(BACKLIGHT_AUTO_OFF_DELAY)
    backlight.off()

@touch.on(touch.BUTTON)
def shutdown_after_delay(channel, event): # pylint: disable=unused-argument
    """"""
    global SHUTDOWN_DELAY_COUNT

    SHUTDOWN_DELAY_COUNT += 1

    if SHUTDOWN_DELAY_COUNT == 60:
        display_off()
        os.system("sudo poweroff")
    else:
        lcd.clear()
        message_left_middle('Powering down in {}.'.format(SHUTDOWN_DELAY_COUNT))
        message_left_bottom('Release button to cancel.')
