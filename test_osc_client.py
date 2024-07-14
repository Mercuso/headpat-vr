import argparse
import time
from pythonosc import udp_client

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=9001,
      help="The port the OSC server is listening on")
  parser.add_argument("--range", type=int, default=20,
      help="Number of iterations to increase speed from 0 (min) to 1 (max)")
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)

  for x in range(args.range):
    value = x/args.range
    print(value)
    client.send_message("/avatar/parameters/pat_left", value)
    time.sleep(0.1)
