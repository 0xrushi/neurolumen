'''
Sender script
use this on pc for replacement of Chamsys MagicQ
'''

from stupidArtnet import StupidArtnet
import time
import random

target_ip = '192.168.4.170'
universe = 1
packet_size = 100

# CREATING A STUPID ARTNET OBJECT
# SETUP NEEDS A FEW ELEMENTS
# TARGET_IP   = DEFAULT 127.0.0.1
# UNIVERSE    = DEFAULT 0
# PACKET_SIZE = DEFAULT 512
# FRAME_RATE  = DEFAULT 30
# ISBROADCAST = DEFAULT FALSE
a = StupidArtnet(target_ip, universe, packet_size, 30, True, True)


packet = bytearray(packet_size)
for i in range(packet_size):
    packet[i] = 0

# Set channel values
packet[0] = 255  # Set channel 1 to 255
packet[1] = 255  # Set channel 2 to 255

# Set packet data
a.set(packet)
# Send data
a.show()  

time.sleep(0.001)

packet[0] = 0
packet[1] = 255

a.set(packet)
a.show()
time.sleep(0.002)

packet[0] = 255
packet[1] = 0

a.set(packet)
a.show()
time.sleep(0.1)
