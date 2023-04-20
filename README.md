# Project-Costanza
The Python portion of our TCNJ 2023 Hackathon. It takes the distance measurement from the Time-of-Flight sensor and sends it a laptop over serial. This Python script takes that measurement and check it. Once it reads a distance within a specified range, it trippgers an API call to Spotify to play music on a specified device. It plays for 5 seconds then pauses. This is all in a loop, so it works endlessly. 

arduinoTospotify.py  
This is the first version of our code

Seinfeld_Detector.py  
This is the version we submitted

main.py
A follow up version that uses the ToF sensor to play and pause my Spotify music with a simple wave of my hand.
