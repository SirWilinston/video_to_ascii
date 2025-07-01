import os
from natsort import natsorted
import time
import colorama
import pygame
from threading import Thread

colorama.init()

path = "ascii/*" # Change the * to the name of your ascii art directory
items = natsorted(os.listdir(path))
target_fps = 60 # Change this to the video frame rate
frame_time = 1.0 / target_fps
audio_file = "audio/*.mp3" # Change the * to the name of the audio

frames = []
for item in items:
    with open(f'{path}/{item}', 'r', encoding='utf-8') as f:
        frames.append(f.read())

pygame.mixer.init()
pygame.mixer.music.load(audio_file)
pygame.mixer.music.set_volume(0.1)

def play_audio():
    pygame.mixer.music.play()

Thread(target=play_audio, daemon=True).start()

time.sleep(.1)

start_time = time.perf_counter()
current_frame = 0

while current_frame < len(frames):
    target_time = start_time + (current_frame * frame_time)
    
    current_time = time.perf_counter()
    
    if current_time >= target_time:
        print("\033[H\033[J" + frames[current_frame], end='', flush=True)
        current_frame += 1
    else:
        time.sleep(0.001)  

    try:
        pass
    except KeyboardInterrupt:
        break

while pygame.mixer.music.get_busy():
    time.sleep(0.1)
