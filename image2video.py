import os
import cv2
import glob
import subprocess

def convert(videoName):
    if videoName == "" :
        return "No video name entered!"
    img_array = []
    for filename in glob.glob('tweets/*.png'):
        img = cv2.imread(filename)
        try:
            height, width, layers = img.shape
            size = (width, height)
        except AttributeError:
            pass
        img_array.append(img)
    videoName += ".avi"
    out = cv2.VideoWriter(videoName, cv2.VideoWriter_fourcc('I', '4', '2', '0'), 1 / 3, size)
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    return "Video created!"

# def convert():
#     # parent = os.getcwd()
#     # directory = "tweets"
#     # path = os.path.join(parent,directory)
#     # os.chdir(path)
#     # -r is the framerate (fps)
#     # -crf is the quality, lower means better quality, 15-25 is usually good
#     # -s is the resolution
#     # -pix_fmt yuv420p specifies the pixel format, change this as needed
#     subprocess.call(['ffmpeg','-r','1/3','-f', 'image2','-s','1920x1080','-i', 'img%d.png', '-vcodec','libx264','-crf','25', '-pix_fmt','yuv420p','out.mp4'],cwd = './tweets/')
#     # os.chdir("..")