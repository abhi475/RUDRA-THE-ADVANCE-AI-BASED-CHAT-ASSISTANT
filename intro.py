from playsound import playsound
import sys

def play_sound():
    try:
        playsound(sound_file_path)
    except Exception as e:
        print(f"Error: {e}")

# Replace 'sound_file_path' with the actual path of your sound file
sound_file_path = "thanos_snap.mp3"



