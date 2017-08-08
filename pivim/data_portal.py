"""
The
"""
import datetime as d
from ISStreamer.Streamer import Streamer

def upload_data(stream_name, temperature):
    """The """
    streamer = Streamer(bucket_name="PiViM-{}".format(d.date), \
                        bucket_key="pivim_{}".format(d.date), \
                        access_key="8077mAn79ul7pd5sf2bvdyfjaoAQCBZ4")

    streamer.log(stream_name, temperature)
