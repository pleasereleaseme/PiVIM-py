"""Debug code for testing module is functioning properly.
"""

from pivim import mobile_broadband as mb

def main():
    """
    Debug code for testing module is functioning properly.
    Uncomment ptvsd lines to enable remote debugging from Visual Studio
    Use format tcp://pi@hostname.local:5678 or
    tcp://pi@ipaddress:5678 when attaching to the debugger.
    """

    # ptvsd.enable_attach(secret='pi')
    # ptvsd.wait_for_attach()

    mobile = mb.MobileBroadband()
    mobile.get_status()

    signal = mobile.signalbar
    network_type = mobile.network_type

    print(signal)
    print(network_type)
    print(mobile.is_connected())

if __name__ == '__main__':
    main()
