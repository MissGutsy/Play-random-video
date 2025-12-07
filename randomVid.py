import os
import random
import subprocess

dir = 'folder path'

vids = os.listdir(dir)
random.shuffle(vids)
for vid in vids:
    path = os.path.join(dir, vid)
    subprocess.run(['vlc', '--play-and-exit', path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)