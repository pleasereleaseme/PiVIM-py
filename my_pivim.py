#!/usr/bin/env python3
"""DocString"""
import time
from pivim import mobile_broadband as mb
from pivim import control_panel as cp
from pivim import data_portal as dp
#from pivim import temperature as t

def main():
    """Evolving picture of how all the different code modules will work together"""
    cp.display_config()

    try:
        while True:
            mobile = mb.MobileBroadband()
            mobile.get_status()

            signalbar = mobile.signalbar
            network_type = mobile.network_type

            latest_temp = 20 # t.read_temp()

            cp.clear_screen()
            cp.message_right_top(network_type)
            cp.message_right_middle('*' * int(signalbar))
            cp.message_right_middle(latest_temp)

            dp.upload_data("Temperature", latest_temp)
            time.sleep(5)

    except KeyboardInterrupt:
        cp.display_off()

if __name__ == '__main__':
    main()
