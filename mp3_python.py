#! /usr/bin/python
import vlc
import time

if __name__ == '__main__':
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new("Kalimba.mp3")
    player.set_media(media)
    player.play()
    time.sleep(10)
    player.stop()
