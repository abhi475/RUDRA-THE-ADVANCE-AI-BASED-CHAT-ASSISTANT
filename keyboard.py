
from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

def press_key(key):
    keyboard.press(key)
    keyboard.release(key)

def volume_up():
    for i in range(5):
        press_key(Key.media_volume_up)
        sleep(0.1)

def volume_down():
    for i in range(5):
        press_key(Key.media_volume_down)
        sleep(0.1)

def play_pause():
    press_key(Key.media_play_pause)

def next_track():
    press_key(Key.media_next)

def previous_track():
    press_key(Key.media_previous)


