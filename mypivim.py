#!/usr/bin/env python3
"""DocString"""
import time
from pivim.mobilebroadband import MobileBroadband
from pivim import control_panel

def main():
    """Evolving picture of how all the different code modules will work together"""
    control_panel.init()

    try:
        while True:
            mobile = MobileBroadband()
            mobile.get_status()

            signalbar = mobile.signalbar
            network_type = mobile.network_type

            control_panel.clear_screen()
            control_panel.set_right_top(network_type)
            control_panel.set_right_middle('*' * int(signalbar))

            time.sleep(10)

    except KeyboardInterrupt:
        control_panel.destroy()

if __name__ == '__main__':
    main()
