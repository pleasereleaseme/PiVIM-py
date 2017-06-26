"""Module for controlling the Pimoroni Display-O-Tron.

"""
import time
from threading import Thread
from dothat import lcd
from dothat import backlight
from dothat import touch

ROW_TOP = 0
ROW_MID = 1
ROW_BOTTOM = 2

BACKLIGHT_AUTO_OFF_DELAY = 30

def init():
    """Sets the display to initial values."""
    lcd.set_contrast(50)

    # Backlight is set to be on initially but to turn off after a delay
    backlight.hue(0.43)
    backlight_auto_off()

def destroy():
    """Turns the display off."""
    backlight.off()
    lcd.clear()

def clear_screen():
    """The screen usually needs to be cleared before writing any text
    to avoid text from previous writes being displayed.
    """
    lcd.clear()

def set_left_top(message):
    """Sets message at top left."""
    set_cursor_left(ROW_TOP)
    lcd.write(message)

def set_left_middle(message):
    """Sets message at middle left."""
    set_cursor_left(ROW_MID)
    lcd.write(message)

def set_left_bottom(message):
    """Sets message at bottom left."""
    set_cursor_left(ROW_BOTTOM)
    lcd.write(message)

def set_right_top(message):
    """Sets message at top right."""
    set_cursor_right(message, ROW_TOP)
    lcd.write(message)

def set_right_middle(message):
    """Sets non-null message at middle right."""
    set_cursor_right(message, ROW_MID)
    lcd.write(message)

def set_right_bottom(message):
    """Sets message at bottom right."""
    set_cursor_right(message, ROW_BOTTOM)
    lcd.write(message)

def set_cursor_right(message, row):
    """Calculates first position of a string that needs to be
    right-aligned based on the display being 16 characters wide.
    """
    if not message:             # If the message is empty just set the cursor to the last column
        cursor_position = 15
    else:                       # Otherwise calculate starting position
        cursor_position = 15 - len(message)

    lcd.set_cursor_position(cursor_position, row)

def set_cursor_left(row):
    """Sets first position of a left-aligned string."""
    lcd.set_cursor_position(0, row)

@touch.on(touch.LEFT)
def backlight_off(channel, event): # pylint: disable=unused-argument
    """Configures the left touch button to turn the backlight off."""
    backlight.off()

@touch.on(touch.RIGHT)
def backlight_on(channel, event): # pylint: disable=unused-argument
    """Configures the right touch button to turn the backlight on."""
    init()
    backlight_auto_off()

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

def debug_module():
    """
    Debug code for testing module is functioning properly.
    Uncomment ptvsd lines to enable remote debugging from Visual Studio
    Use format tcp://pi@hostname.local:5678 or
    tcp://pi@ipaddress:5678 when attaching to the debugger.
    """

    # ptvsd.enable_attach(secret='pi')
    # ptvsd.wait_for_attach()

    init()

    try:
        while True:
            for i in range(10):
                set_left_top("LT{0}".format(i))
                set_right_top("RT{0}".format(i))
                set_left_middle("LM{0}".format(i))
                set_right_middle("RM{0}".format(i))
                set_left_bottom("LB{0}".format(i))
                set_right_bottom("RB{0}".format(i))

                time.sleep(1)

    except KeyboardInterrupt:
        destroy()

if __name__ == '__main__':
    debug_module()
