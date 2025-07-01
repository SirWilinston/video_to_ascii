import cv2
import os
from tkinter import filedialog 
import pathlib
import ffmpeg

def video_to_frames(rutaVideo, rutaGuardado):
    try:
        capture = cv2.VideoCapture(rutaVideo)
        print("Video loaded correctly")
    except Exception as e:
        print(f"Error opening the video: {e}")

    f = 0

    while (capture.isOpened()):
        
        ret, frame = capture.read()

        if ret == False:
            if f == 0:
                print("Error procesing the video :(")
                break
            print("Video procesing finished")
            break
        
        cv2.imwrite(f"{rutaGuardado}/{str(f)}.jpg", frame)

        f += 1

if __name__ == "__main__":

    path = ""

    file_path = filedialog.askopenfilename(
            initialdir="./",
            title="Select video",
        )

    current = str(pathlib.Path(__file__).parent.resolve()).replace("\\","/")

    filenameFull = os.path.basename(file_path)
    filename = filenameFull.split(".")
    file = filename[0]

    ruta_guardado = "output/" + str(file)

    os.makedirs(ruta_guardado, exist_ok=True)

    if file_path != "":
        try:
            path = file_path.replace(str(current + "/"), "")
            print(path)
        except Exception as e:
            print(f"Error {e}")

    if path != "":
        print("Path correct")
        (
            ffmpeg.input(path)
            .output(ruta_guardado.replace("output","audio") + ".mp3")
            .run()
        )
        video_to_frames(path, ruta_guardado)
