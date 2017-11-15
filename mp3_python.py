#! /usr/bin/python
import vlc
import time
import random
import os

PLAY  = 0
PAUSE = 1
NEXT  = 2
PREV  = 3
QUIT  = 4

if __name__ == '__main__':

    instance = vlc.Instance()
    player = instance.media_player_new()

    state = PLAY
    mnt_root = '/media/usb'
    mnt_files = [instance.media_new(os.path.join(mnt_root,x)) for x in os.listdir(mnt_root) if x.endswith('.mp3')]
    random.shuffle(mnt_files)
    player.set_media(mnt_files[0])

    while(state!=QUIT):
        if(state==PLAY):
            player.play()
        if(state==NEXT):
            player.set_media(mnt_files[1])
            state=PLAY
        if(state==PAUSE):
            player.pause()
        try:
            state = int(raw_input())
        except:
            pass
    player.stop()
