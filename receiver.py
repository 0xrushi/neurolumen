'''
Receiver script
Use this on pc for replacement of ArtNetView
'''

from stupidArtnet import StupidArtnetServer
import time
import datetime
import json

OUTPUT_FILE = "artnet_data.json"

def test_callback(data, universe):
    """Callback function to process received Art-Net packet"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    # channels = list(range(1, len(data) + 1))
    intensities = list(data)

    # Prepare the data entry
    data_entry = {
        "timestamp": timestamp,
        "universe": universe,
        "intensities": intensities
    }

    with open(OUTPUT_FILE, "a") as json_file:
        json.dump(data_entry, json_file)
        json_file.write("\n")  

a = StupidArtnetServer()

universe_to_listen = 1
listener_id = a.register_listener(universe=universe_to_listen, callback_function=test_callback)

print("Listening for Art-Net packets...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    a.delete_listener(listener_id)
    a.close()
    print("Stopped listening for Art-Net packets.")
