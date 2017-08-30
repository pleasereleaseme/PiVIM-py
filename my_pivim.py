#!/usr/bin/env python3
"""DocString"""
import time
from pivim import mobile_broadband as mb
from pivim import control_panel as cp
from pivim import data_portal as dp
from pivim import temperature as t

def main():
    """Evolving picture of how all the different code modules will work together"""
    cp.display_config()

    highest_temp = 0
    lowest_temp = 0

    try:
        while True:
            mobile = mb.MobileBroadband()
            mobile.get_status()

            signalbar = mobile.signalbar
            network_type = mobile.network_type

            latest_temp = t.read_temp()
            lowest_temp = latest_temp if latest_temp < lowest_temp else lowest_temp
            highest_temp = latest_temp if latest_temp > highest_temp else highest_temp

            cp.clear_screen()
            cp.message_right_top(network_type)
            cp.message_right_middle('*' * int(signalbar))
            cp.message_left_top(str(lowest_temp))
            cp.message_left_middle(str(latest_temp))
            cp.message_left_bottom(str(highest_temp))

            dp.upload_data("Temperature", latest_temp)
            time.sleep(5)

    except KeyboardInterrupt:
        cp.display_off()

if __name__ == '__main__':
    main()
