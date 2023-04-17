import serial
import requests
import time

# Open the serial port
ser = serial.Serial('\\\\.\\COM10', 115200, timeout=0.15)

device_id = "[your device id here]"

token = "[yur token here]"


def play():
    url = f"https://api.spotify.com/v1/me/player/play?device_id={device_id}"

    data = {
        # "context_uri": "spotify:artist:6wyLmoC7u1PG52QcUvlbTf",
        # "offset": {
        # "uri": "spotify:artist:6wyLmoC7u1PG52QcUvlbTf",
        # "position": 0,
        # },
        "position_ms": 0
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.put(url, json=data, headers=headers)

    print("response code", response.status_code)


def pause():
    url = f"https://api.spotify.com/v1/me/player/pause?device_id={device_id}"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.put(url, json={}, headers=headers)

    print("response code", response.status_code)


def sensor_val():
    data = ser.read(100).split(b'\n')
    data = data[len(data) - 2]
    data = data.rstrip()
    return int(data)


# Read and print the data from the serial port
playing = False
playingTime = time.time()
while True:
    if ser.inWaiting() > 0:
        val = sensor_val()
        print(val, time.time())
        if val < 250:
            if not playing:
                print("playing ", time.time())
                play()
                playing = True
                playingTime = time.time()
        else:
            if playing and time.time()-playingTime >= 10:
                print("pausing", time.time())
                pause()
                playing = False
        time.sleep(0.15)
