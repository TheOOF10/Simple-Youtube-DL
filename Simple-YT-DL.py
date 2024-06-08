print("Loading...")
import os
import sys
arguments = sys.argv
nomerge = 0
url = 0
name = 0
idkwhattonamethis = 0
urltmp = 0
for item in arguments:
    if item == "--help":
            print("-----------")
            print("Tutorial Downloading a video")
            print("-----------")
            print("Type the command you just entered but instead of --help insert the url")
            print("Also after you add the url you can add the filename you want the video file to be (don't forget the extension) by using the -o flag and adding the name")
            print("The downloader will ask you if you want an audio file or a video file")
            print("Then it will ask you in which resolution you want the video to be (only avaible when on video mode)")
            print("There is nothing involving arguments and stuff just the instructions above it's called Simple Youtube DL for a reason")
            print("-----------")
            print("Extra Inforamtion")
            print("-----------")
            print("60fps Downloading is only avaible on 1080p+ but even then it might not be available")
            print("-----------")
            print("Extra Arguments")
            print("-----------")
            print("--nomerge | When Downloading 1080p+ youtube only offers both the video and the audio on seperate streams so the script downloads both files and merges them if you don't want to merge the files for whatever reason use that")
            exit()
    if item[:8] == "https://" or item[:8] == "http://w" or item[:8] == "http://y" or item[:8] == "www.yout" or item[:8] == "youtube." or item[:8] == "music.yo" or item[:8] == "http://m" or item[:8] == "www.musi": #check for url
        urltmp = item
    if item == "-o":
        idkwhattonamethis = 2
    if idkwhattonamethis == 1:
        name = item
        idkwhattonamethis = 0
    if item == "--nomerge":
        nomerge = 1
    if idkwhattonamethis == 2:
        idkwhattonamethis = 1

from pytube import YouTube
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
url = YouTube(urltmp)

confline1 = 0   
conffile = "conf.txt"
if not os.path.exists(conffile):
        print("ERROR configuration file not found creating one...")
        print("Should downloading in 60fps be the default?")
        yn = input()
        if yn == "yes" or yn == "y":
            confline1 = "60fpsDefault: 1\n"
        elif yn == "no" or yn == "n":
            confline1 = "60fpsDefault: 0\n"
        with open(conffile, "w") as conf:
            conf.write(confline1)

with open(conffile, "r") as f:
    fpsDefault = f.read()[:15]
forbiten_chars = [":", "/", "\\", "?", "*", "|", "<", ">", '"', "'"]
def remove_chars(input_string):
    for char in forbiten_chars:
        input_string = input_string.replace(char, '')
    return input_string
print("Done Loading!")

print("Do you want to download either video or audio")
c = input() # input lol
if c == "video" or c == "v": #Downloads Video
    if name == 0:
        name = url.title + ".mp4"
    print("You selected video mode")
    print("What resolution do you want to download the video in? (type number)")
    print("1. 4K")
    print("2. 1440p")
    print("3. 1080p")
    print("4. 720p")
    print("5. 360p")
    res = input()
    text = "Downloading " + url.title + "..."
    print(text)
    if name == "--nomerge":
        nomerge = 1
    name = remove_chars(name)
    if int(res) == 1: # Download Video files
        if fpsDefault == "60fpsDefault: 1":
            stream = url.streams.get_by_itag(337)
            try:
                stream.download(filename="tmp.mp4")
            except AttributeError:
                print("ERROR could not download at 60fps trying at 30fps")
                stream = url.streams.get_by_itag(313)
                stream.download(filename="tmp.mp4")
        else:
            stream = url.streams.get_by_itag(313)
            try:
                stream.download(filename="tmp.mp4")
            except AttributeError:
                print("ERROR could not download at 30fps trying at 60fps")
                stream = url.streams.get_by_itag(337)
                stream.download(filename="tmp.mp4")
        stream = url.streams.get_by_itag(251)
        stream.download(filename="tmpaudio.webm")
    elif int(res) == 2:
        if fpsDefault == "60fpsDefault: 1":
            stream = url.streams.get_by_itag(336)
            try:
                stream.download(filename="tmp.mp4")
            except AttributeError:
                print("ERROR could not download at 60fps trying at 30fps")
                stream = url.streams.get_by_itag(271)
                stream.download(filename="tmp.mp4")
        else:
            stream = url.streams.get_by_itag(271)
            try:
                stream.download(filename="tmp.mp4")
            except AttributeError:
                print("ERROR could not download at 30fps trying at 50fps")
                stream = url.streams.get_by_itag(336)
                stream.download(filename="tmp.mp4")
        stream = url.streams.get_by_itag(251)
        stream.download(filename="tmpaudio.webm")
    elif int(res) == 3:
        if fpsDefault == "60fpsDefault: 1":
            stream = url.streams.get_by_itag(335)
            try:
                stream.download(filename="tmp.mp4")
            except AttributeError:
                print("ERROR could not download at 60fps trying at 30fps")
                stream = url.streams.get_by_itag(137)
                stream.download(filename="tmp.mp4")
        else:
            stream = url.streams.get_by_itag(137)
            try:
                stream.download(filename="tmp.mp4")
            except:
                print("ERROR could not download at 30fps trying at 60fps")
                stream = url.streams.get_by_itag(335)
                stream.download(filename="tmp.mp4")
        stream = url.streams.get_by_itag(251)
        stream.download(filename="tmpaudio.webm")
    elif int(res) == 4:
        stream = url.streams.get_by_itag(22)
        stream.download(filename=name)
    elif int(res) == 5:
        stream = url.streams.get_by_itag(18)
        stream.download(filename=name)
    else:
        print("ERROR wrong input")
    if int(res) < 3 or int(res) == 3: #Merges video and audio file if res higher than 1080p (because i can't download audio and video all once in a single file because youtube uses a diffrent streaming method in these resolutions)
        if nomerge == 1: #Final stuff when using --nomerge
            name = remove_chars(url.title)
            os.rename("tmp.mp4", name + ".mp4")
            os.rename("tmpaudio.webm", name + ".webm")
        if nomerge == 0:
            print("Finalazing...")
            video_clip = VideoFileClip("tmp.mp4")
            audio_clip = AudioFileClip("tmpaudio.webm")
            video_clip = video_clip.set_audio(audio_clip)
            video_clip.write_videofile(name)
elif c == "audio" or c == "a": # Downloads audio
    print("You selected audio mode")
    text = "Downloading " + url.title + "..."
    print(text)
    stream = url.streams.get_by_itag(251)
    fname = url.title + ".webm"
    fname = remove_chars(fname)
    stream.download(filename=fname)
    print("Finalazing...")
    filename = url.title + ".webm"
    if name == 0:
        finalname = url.title + ".mp3"
    else:
        finalname = name
    finalname = remove_chars(finalname)
    filename = remove_chars(filename)
    clip = AudioFileClip(filename)
    print(finalname)
    clip.write_audiofile(finalname)
    os.remove(filename)
    print("Done")
    print("Audio saved as " + finalname)
