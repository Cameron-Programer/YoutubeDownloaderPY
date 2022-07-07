
#Import moduels 
from __future__ import unicode_literals
import youtube_dl
import os

#This is the help meunu that the user can access if they are unsure about anything. ⚠️This must be avaliable to init before any of the yt and ffmpeg moduals are used or its kinda pointless
def helpMenu():
    print("Welcome to the help menu")
    helpinusr = input("Do you want help with installing 'FFMPEG' or help installing 'choco'?: ")
    if helpinusr == ("FFMPEG"):
        print("https://community.chocolatey.org/packages/ffmpeg")
        if input("Do you want this program to automate the installation of FFMPEG?: [y]/[n]") == "Yes":
            print("ERROR:000x. If you contact a help desk tell them it is an ID  -  10  -  T error ")  #TODO:Send the ffmpeg install request to command line 
    elif helpinusr == ("choco"):
        print("https://chocolatey.org/install#individual")
    elif helpinusr == "piq":
        vidUrllocater
    else:
        print("You have not selected a valid option please type one of the presented options or type 'piq' to retun to the first menu")

#start message
print("Welcome to the Youtube to Mp3 python file, You MUST have FFMPEG and Youtube_dl installed. If you need assistance installing this type 'help'")
numOfVids = int(input("How many videos do you want to download?: "))
arrayOfLink = []
if numOfVids == ("help"):
    helpMenu()
numOfVids = int(numOfVids)
#The user will enter the url here the entered URLS will be added to an array that will then be passed to the API moduel
def vidUrllocater():
    for state in range(0,numOfVids):
        print(arrayOfLink)
        print("Enter video URL for video number", state + 1)
        videoURL = input("URL: ")
        arrayOfLink.append(videoURL)
        




#this is the modual that will contact the youtube API and rip the audio there is no user input in this sub
def vidyoinker2000():
    for i in range (0,len(arrayOfLink)):   
        ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '320'
        }],
        'postprocessor_args': [
            '-ar', '16000'
        ],
        'prefer_ffmpeg': True,
        'keepvideo': True
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([arrayOfLink[i]])

#Gonna start calling subprograms here

vidUrllocater()
vidyoinker2000()

print("This program will automaticaly close when it has finished yoinking")
