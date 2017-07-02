"""Debug code for testing module is functioning properly.
"""

import time
from pivim import control_panel as cp

def main():
    """Uncomment ptvsd lines to enable remote debugging from Visual Studio
    Use format tcp://pi@hostname.local:5678 or
    tcp://pi@ipaddress:5678 when attaching to the debugger.
    """

    # ptvsd.enable_attach(secret='pi')
    # ptvsd.wait_for_attach()

    cp.display_config()

    try:
        while True:
            for i in range(10):
                cp.clear_screen()

                cp.message_left_top("LT{0}".format(i))
                cp.message_right_top("RT{0}".format(i))
                cp.message_left_middle("LM{0}".format(i))
                cp.message_right_middle("RM{0}".format(i))
                cp.message_left_bottom("LB{0}".format(i))
                cp.message_right_bottom("RB{0}".format(i))

                time.sleep(1)

    except KeyboardInterrupt:
        cp.display_off()

if __name__ == '__main__':
    main()
