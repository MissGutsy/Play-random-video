import os
import random
import time
import vlc
from moviepy import VideoFileClip

dir = 'folder path'

vids = os.listdir(dir)
random.shuffle(vids)
media_player = vlc.MediaPlayer()
media_player.set_fullscreen(True)
for vid in vids:
    path = os.path.join(dir, vid)
    duration = VideoFileClip(path).duration
    duration = 2
    media = vlc.Media(path, 'file-caching=3000')
    media_player.set_media(media)
    media_player.play()
    time.sleep(duration)