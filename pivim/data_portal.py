"""
The
"""
import time
from random import randint
from ISStreamer.Streamer import Streamer

def upload_temp_data():
    """The """

    streamer = Streamer(bucket_name="PiViM", bucket_key="pivim_test", access_key="8077mAn79ul7pd5sf2bvdyfjaoAQCBZ4")

    while True:
        streamer.log("Temperature", randint(25, 30))
        time.sleep(1)

