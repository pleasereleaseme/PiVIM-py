#!/usr/bin/env python3
"""DocString"""
import time
from pivim import mobile_broadband as mb
from pivim import control_panel as cp

def main():
    """Evolving picture of how all the different code modules will work together"""
    cp.display_config()

    try:
        while True:
            mobile = mb.MobileBroadband()
            mobile.get_status()

            signalbar = mobile.signalbar
            network_type = mobile.network_type

            cp.clear_screen()
            cp.message_right_top(network_type)
            cp.message_right_middle('*' * int(signalbar))

            time.sleep(10)

    except KeyboardInterrupt:
        cp.display_off()

if __name__ == '__main__':
    main()
