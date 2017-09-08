"""
The
"""
import datetime as dt
from ISStreamer.Streamer import Streamer

def upload_data(stream_name, temperature):
    """The """
    today = dt.date.today()

    streamer = Streamer(bucket_name="PiViM-{}".format(today), \
                        bucket_key="pivim_t{}".format(today), \
                        access_key="8077mAn79ul7pd5sf2bvdyfjaoAQCBZ4")

    streamer.log(stream_name, temperature)
