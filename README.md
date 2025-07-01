# video_to_ascii
This is a short proyect where I wanted to create a program to transform mp4 video to ascii art to play Bad Apple in the cmd of windows. Not great but as some people say, if it works don't touch it,


# Important requirements
For this to work you need to install this libraries

-pygame
-colorama
-natsort
-pathlib
-pillow
-opencv

# How to use
1) Select the video
First you need to get a video, preferably with high contrast colors.

2) Run video_to_frames.py
This will let you get all the video frames in a separate folder that will be saved in an output folder, this will also separate the audio for the playing part

3) Run directory_to_ascii.py
This will let you select the directory with all the frames to convert it to ascii. I could have done this in the same file as video_to_frames.py but i was lazy

4) Set the player settings
In the reproductor.py file you need to put the directory of the ascii art and the sound for it to work, you also need to change the desired_fps variable to the fps of the original video.

5) Open PowerShell and play
Finally you can open the powershell (the cmd goes lagged so it desyncs the ascii from the sound) and run the reproductor.py file.

6) Enjoy
You can get any mp4 video to work, just set the correct frame rate and enjoy ^^
