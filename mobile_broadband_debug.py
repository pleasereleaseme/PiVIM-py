"""Debug code for testing module is functioning properly.
"""

from pivim import mobile_broadband as mobile_broadband
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

    mb = mobile_broadband.MobileBroadband() # pylint: disable=invalid-name
    mb.get_status()

    signal = mb.signalbar
    network_type = mb.network_type
    network_provider = mb.network_provider

    print(signal)
    print(network_type)
    print(network_provider)
    print(mb.is_connected())

if __name__ == '__main__':
    main()
