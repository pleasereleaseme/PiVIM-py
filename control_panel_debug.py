import time
from pivim import control_panel as cp

def main():
    """
    Debug code for testing module is functioning properly.
    Uncomment ptvsd lines to enable remote debugging from Visual Studio
    Use format tcp://pi@hostname.local:5678 or
    tcp://pi@ipaddress:5678 when attaching to the debugger.
    """

    # ptvsd.enable_attach(secret='pi')
    # ptvsd.wait_for_attach()

    cp.init()

    try:
        while True:
            for i in range(10):
                cp.clear_screen()

                cp.set_left_top("LT{0}".format(i))
                cp.set_right_top("RT{0}".format(i))
                cp.set_left_middle("LM{0}".format(i))
                cp.set_right_middle("RM{0}".format(i))
                cp.set_left_bottom("LB{0}".format(i))
                cp.set_right_bottom("RB{0}".format(i))

                time.sleep(1)

    except KeyboardInterrupt:
        cp.destroy()

if __name__ == '__main__':
    main()