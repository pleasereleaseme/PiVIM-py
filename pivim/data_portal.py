"""
Module for streaming data to Initial State.
"""
import datetime as dt
from ISStreamer.Streamer import Streamer

def upload_temperature_data(access_key, temperature):
    """Stream temperature data using supplied module."""
    today = dt.date.today()

    try:
        # Append date in order to identify the latest stream in the Initial State user interface
        streamer = Streamer(bucket_name="PiViM-{}".format(today), \
                            bucket_key="pivim_{}".format(today), \
                            access_key=access_key, debug_level=2)

        streamer.log("T", temperature)

        streamer.flush()
    except Exception: # pylint: disable=W0703
        pass
