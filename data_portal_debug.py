"""Debug code for testing module is functioning properly.
"""

from pivim import data_portal as dp
import ptvsd # pylint: disable=unused-import

def main():
    """Uncomment ptvsd lines to enable remote debugging from Visual Studio
    Use format tcp://pi@hostname.local:5678 or
    tcp://pi@ipaddress:5678 when attaching to the debugger.
    """

    # ptvsd.enable_attach(secret='pi')
    # ptvsd.wait_for_attach()

    dp.upload_temp_data()

if __name__ == '__main__':
    main()