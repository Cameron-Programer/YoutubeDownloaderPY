#Import moduels 
from __future__ import unicode_literals
import os
import youtube_dl
userchosenCodec = 'm4a'

#colours the terminal [CREDIT: G4G]
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


#start message
print("Welcome to the Youtube to Mp3 python file, You MUST have FFMPEG, and Youtube_dl installed.")
numOfVids = input("How many videos do you want to download?: ")
arrayOfLink = []
#this will allow the user to input a video URL into the first box and it will automaticaly start downloading it 
if numOfVids[0] == ("h"):
    prRed("QUICK DOWNLOAD: ENABLED")
    quickMenu = True
    arrayOfLink.append(numOfVids)

    numOfVids = 1
else:
    int(numOfVids)
    quickMenu = False

numOfVids = int(numOfVids)


#The user will enter the url here the entered URLS will be added to an array that will then be passed to the API moduel unless quickmenu is enabled
def vidUrllocater():
    for state in range(0,numOfVids):
        print("Enter video URL for video number", state + 1)
        videoURL = input("URL: ")
        arrayOfLink.append(videoURL)
    
def codecLocator():
    fish = input("Do you want to change your format from m4a to a new format?: Y/N: ")
    fish = fish.lower()
    if fish[0] == "y":
        userchosenCodec = input("Enter your chosen Codec: ")
        print("Your Codec has been updated to",userchosenCodec) 
        return userchosenCodec
    

     
#this is the modual that will contact the youtube website and rip the audio there is no user input in this sub
def vidyoinker2000():
   
    print("Starting Download Process: Codec",userchosenCodec)
    for i in range (0,len(arrayOfLink)):   
        ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': userchosenCodec,
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
if quickMenu == False:
    vidUrllocater()
    userchosenCodec = codecLocator()
    vidyoinker2000()
elif quickMenu == True:
    vidyoinker2000()
else:
    print("ERROR | Subprogram never called | Open an issue on Github!")

def endmessage():
    print("     ⠀   ")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("-                                                          -")
    print("-               Thanks for using this script! :D           -")
    print("-                                                          -")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("-                                                          -")
    print("-                                                          -")
    print("-    If you have any errors open an issue on github        -")
    print("- https://github.com/Cameron-Programer/YoutubeDownloaderPY -")
    print("-                                                          -")
    print("-                       o(*≧▽≦)ツ                          -")#this need to be 1 further out than the rest proably an ususal char.
    print("-                                                          -")
    print("============================================================")
endmessage()