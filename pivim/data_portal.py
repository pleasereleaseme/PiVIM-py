"""
The
"""

from ISStreamer.Streamer import Streamer

def upload_data(stream_name, temperature):
    """The """
    streamer = Streamer(bucket_name="PiViM", \
                        bucket_key="pivim_test", \
                        access_key="8077mAn79ul7pd5sf2bvdyfjaoAQCBZ4")
    streamer.log(stream_name, temperature)
