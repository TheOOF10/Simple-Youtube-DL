print("Loading...")
from pytube import YouTube
import sys
import os
import ffmpeg
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
arguments = sys.argv
script_name = arguments[0]
first = arguments[1]
firstl = first[:8]

if first == "--help":
    print("Tutorial Downloading a video")
    print("type the command you just entered but instead of --help insert the url")
    print("The downloader will ask you if you want an audio file or a video file")
    print("Then it will ask you in which resolution you want the video to be (only avaible when on video mode)")
    print("There is nothing involving arguments and stuff just the instructions above it's called Simple Youtube DL for a reason")
elif firstl == "https://" or firstl == "http://w" or firstl == "http://y" or firstl == "www.yout" or firstl == "youtube.": #check for url
    url = YouTube(first)
    print("Do you want to download either video or audio")
    c = input()
    if c == "video" or c == "v":
        print("You selected video mode")
        print("What resolution do you want to download the video in? (type number)")
        print("1. 1080p")
        print("2. 720p")
        print("3. 360p")
        res = input()
        text = "Downloading " + url.title + "..."
        if int(res) == 1:
            stream = url.streams.get_by_itag(137)
            stream.download(filename="tmp.mp4")
            stream = url.streams.get_by_itag(22)
            stream.download(filename="tmpaudio.mp4")
        elif int(res) == 2:
            stream = url.streams.get_by_itag(22)
            stream.download()
        elif int(res) == 3:
            stream = url.streams.get_by_itag(18)
            stream.download()
        else:
            print("ERROR wrong input")
        if int(res) < 1 or int(res) == 1: #added < because there might be more resolutions in the future
            print("Finalazing...")
            outfile = url.title + ".mp4"
            video_clip = VideoFileClip("tmp.mp4")
            audio_clip = AudioFileClip("tmpaudio.mp4")
            video_clip = video_clip.set_audio(audio_clip)
            video_clip.write_videofile(outfile)
    elif c == "audio" or c == "a":
        print("You selected audio mode")
        text = "Downloading " + url.title + "..."
        print(text)
        stream = url.streams.get_by_itag(18)
        stream.download()
        print("Finalazing...")
        filename = url.title + ".mp4"
        finalname = url.title + ".mp3"
        clip = VideoFileClip(filename)
        clip.audio.write_audiofile(finalname)
        os.remove(filename)
        print("Done")
        print("Audio saved as " + finalname)
    else:
        print("ERROR input error")
else:
    print("ERROR: Argument not found type --help for help")
