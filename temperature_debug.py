"""Debug code for testing module is functioning properly.
"""

import time
from pivim import temperature as t
import ptvsd # pylint: disable=unused-import

def main():
    """
    Debug code for testing module is functioning properly.
    Uncomment ptvsd lines to enable remote debugging from Visual Studio
    Use format tcp://pi@hostname.local:5678 or
    tcp://pi@ipaddress:5678 when attaching to the debugger.
    """

    # ptvsd.enable_attach(secret='pi')
    # ptvsd.wait_for_attach()

    while True:
        try:
            latest_temp = round(t.read_temp() -0.5)
            print(latest_temp)
            time.sleep(5)
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    main()
