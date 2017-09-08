"""
Module for streaming data to Initial State.
"""
import datetime as dt
from ISStreamer.Streamer import Streamer

def upload_temperature_data(access_key, temperature):
    """Stream temperature data using supplie module."""
    today = dt.date.today()

    # Tag on date in order to identify the latest stream in the Initial State user interface
    streamer = Streamer(bucket_name="PiViM-{}".format(today), \
                        bucket_key="pivim_{}".format(today), \
                        access_key=access_key)

    streamer.log("T", temperature)
