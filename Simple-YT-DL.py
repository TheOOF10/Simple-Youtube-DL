print("Loading...")
from pytube import YouTube
import sys
import os
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
arguments = sys.argv
script_name = arguments[0]
try:
    first = arguments[1]
except IndexError:
    print("ERROR: Argument not found type --help for help")
    sys.exit(1) 

firstl = first[:8]
if first == "--help":
    print("Tutorial Downloading a video")
    print("type the command you just entered but instead of --help insert the url")
    print("The downloader will ask you if you want an audio file or a video file")
    print("Then it will ask you in which resolution you want the video to be (only avaible when on video mode)")
    print("There is nothing involving arguments and stuff just the instructions above it's called Simple Youtube DL for a reason")
elif firstl == "https://" or firstl == "http://w" or firstl == "http://y" or firstl == "www.yout" or firstl == "youtube.": #check for url
    url = YouTube(first)
    #for stream in url.streams:
    #    print(stream)
    print("Do you want to download either video or audio")
    c = input()
    if c == "video" or c == "v":
        print("You selected video mode")
        print("What resolution do you want to download the video in? (type number)")
        print("1. 4K")
        print("2. 1440p")
        print("3. 1080p")
        print("4. 720p")
        print("5. 360p")
        res = input()
        text = "Downloading " + url.title + "..."
        if int(res) == 1:
            stream = url.streams.get_by_itag(337)
            try:
                stream.download(filename="tmp.mp4")
            except AttributeError:
                print("ERROR could not download at 60fps trying at 30fps")
                stream = url.streams.get_by_itag(313)
                stream.download(filename="tmp.mp4")
            stream = url.streams.get_by_itag(251)
            stream.download(filename="tmpaudio.webm")
        elif int(res) == 2:
            stream = url.streams.get_by_itag(336)
            try:
                stream.download(filename="tmp.mp4")
            except AttributeError:
                print("ERROR could not download at 60fps trying at 30fps")
                stream = url.streams.get_by_itag(271)
                stream.download(filename="tmp.mp4")
            stream = url.streams.get_by_itag(251)
            stream.download(filename="tmpaudio.webm")
        elif int(res) == 3:
            stream = url.streams.get_by_itag(335)
            try:
                stream.download(filename="tmp.mp4")
            except AttributeError:
                print("ERROR could not download at 60fps trying at 30fps")
                stream = url.streams.get_by_itag(137)
                stream.download(filename="tmp.mp4")
            stream = url.streams.get_by_itag(251)
            stream.download(filename="tmpaudio.webm")
        elif int(res) == 4:
            stream = url.streams.get_by_itag(22)
            stream.download()
        elif int(res) == 5:
            stream = url.streams.get_by_itag(18)
            stream.download()
        else:
            print("ERROR wrong input")
        if int(res) < 3 or int(res) == 3:
            print("Finalazing...")
            outfile = url.title + ".mp4"
            video_clip = VideoFileClip("tmp.mp4")
            audio_clip = AudioFileClip("tmpaudio.webm")
            video_clip = video_clip.set_audio(audio_clip)
            video_clip.write_videofile(outfile)
    elif c == "audio" or c == "a":
        print("You selected audio mode")
        text = "Downloading " + url.title + "..."
        print(text)
        stream = url.streams.get_by_itag(251)
        stream.download()
        print("Finalazing...")
        filename = url.title + ".webm"
        finalname = url.title + ".mp3"
        clip = AudioFileClip(filename)
        clip.write_audiofile(finalname)
        os.remove(filename)
        print("Done")
        print("Audio saved as " + finalname)
    else:
        print("ERROR input error")
else:
    print("ERROR: Argument not found type --help for help")
