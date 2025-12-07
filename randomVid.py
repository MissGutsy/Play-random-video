import os
import random
import time
import vlc
from moviepy import VideoFileClip

dir = '/home/jule/Coding/Python/Play-random-video/vids'

vids = os.listdir(dir)
random.shuffle(vids)
media_player = vlc.MediaPlayer()
for vid in vids:
    path = os.path.join(dir, vid)
    duration = VideoFileClip(path).duration
    media = vlc.Media(path)
    media_player.set_media(media)
    media_player.play()
    time.sleep(duration)