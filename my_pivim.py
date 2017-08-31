#!/usr/bin/env python3
"""DocString"""
import time
from pivim import mobile_broadband as mb
from pivim import control_panel as cp
from pivim import data_portal as dp
from pivim import temperature as t
from apscheduler.schedulers.background import BackgroundScheduler

def main():
    """Evolving picture of how all the different code modules will work together"""
    cp.display_config()

    global highest_temp = 0
    global lowest_temp = 100

    scheduler = BackgroundScheduler()

    try:
        scheduler.add_job(do_work, 'interval', seconds=5)
        scheduler.start()
    except KeyboardInterrupt:
        scheduler.shutdown()
        cp.display_off()

def do_work():
    mobile = mb.MobileBroadband()
    mobile.get_status()

    signalbar = mobile.signalbar
    network_type = mobile.network_type

    latest_temp = round(t.read_temp() -0.5)
    lowest_temp = latest_temp if latest_temp < lowest_temp else lowest_temp
    highest_temp = latest_temp if latest_temp > highest_temp else highest_temp

    cp.clear_screen()
    cp.message_right_top(network_type)
    cp.message_right_middle('*' * int(signalbar))
    cp.message_left_top("L: " + str(lowest_temp))
    cp.message_left_middle("N: " + str(latest_temp))
    cp.message_left_bottom("H: " + str(highest_temp))

    dp.upload_data("Temperature", latest_temp)

if __name__ == '__main__':
    main()
