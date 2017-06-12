#!/usr/bin/env python3
"""DocString"""
import time
from PiVIM.mobilebroadband import MobileBroadband
from PiVIM import display

def main():
    """Evolving picture of how all the different code modules will work together"""
    display.init()

    try:
        while True:
            mobile = MobileBroadband()
            mobile.get_status()

            signalbar = mobile.signalbar
            network_type = mobile.network_type

            display.clear_screen()
            display.set_right_top(network_type)
            display.set_right_middle('*' * int(signalbar))

            time.sleep(10)

    except KeyboardInterrupt:
        display.destroy()

if __name__ == '__main__':
    main()
