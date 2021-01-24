from pytube import YouTube
import time
#if you get an error about pytbue3 , use the command down below
#python3 -m pip install --upgrade "git+https://github.com/nficano/pytube.git"


video = input("Enter the video link here : ")

YouTube(video).streams.first().download()