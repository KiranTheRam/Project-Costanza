import spotipy
from spotipy import SpotifyOAuth
import configparser
import time
import serial


def sensor_val():
    data = ser.read(100).split(b'\n')
    data = data[len(data) - 2]
    data = data.rstrip()
    return int(data)


# Open the serial port
ser = serial.Serial('\\\\.\\COM3', 115200, timeout=0.15)

# Set up configparser
config = configparser.ConfigParser()
config.read('config.ini')

# Set up Spotify/Spotipy values
client_id = config.get('spotify', 'client_id')
client_secret = config.get('spotify', 'client_secret')
scope = config.get('spotify', 'scope')
redirect_uri = config.get('spotify', 'redirect_uri')

# Authenticate with Spotify
print("Authenticating...")
auth_manager = SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret,
                            redirect_uri=redirect_uri)
sp = spotipy.Spotify(auth_manager=auth_manager)
print("Auth succeeded")

while True:
    # Check if we are getting data. Print it to the console
    if ser.inWaiting() > 0:
        val = sensor_val()
        print(val)
        # print(val, time.time())
        # If a hand is detected within range
        if val < 250:
            current_track = sp.current_playback()
            if current_track is not None and current_track['is_playing']:
                print("Pause")
                sp.pause_playback()
            elif current_track is not None:
                print("Play")
                sp.start_playback()
            else:
                print("No device is currently playing. Start playback on any device")
            time.sleep(0.15)
