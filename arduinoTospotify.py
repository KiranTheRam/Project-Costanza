import serial
import requests
import time

# Open the serial port
ser = serial.Serial('\\\\.\\COM10', 115200, timeout=0.15)

device_id = "50514a231092e6c14803486692b3974f6a20aca5"

token = "BQD4N7u7DzyOcFk3PZYNUwY8NuPYL0kd1iiAXnWZuyvYZE__VJuTQ1H7y_aLWY0iqW5Lbr_akUAZobSLFwEMqtavwc4q2CYNkQRTNX6hLfSVb-quYSOUw8XWwduZaXspmRYlTbcYe7MFgaox7gOOA_XGwlxPMEVFnC1CASbYAy_i5v4IUafs_FEVtuRDFYTKU1YN2XgysXS2fDJiBNPAKDO7l5uWlAFGJkTtEGbQqopZmI7TGzDTkJ65Jg0A9I2y0lkBHlAeYiUwYkw99bBQPr4s4WT784zzZL3xOVm1dIHqwKPy97RTRrHrkITPyfXN5lOOG8CR04WqOgJDT14p2kDQy8C8LEs21h2b6pttBKjq6Tc"


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
