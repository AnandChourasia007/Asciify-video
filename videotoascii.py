import cv2
import numpy as np
import os
import natsort
from os.path import isfile, join
from PIL import Image, ImageDraw, ImageOps, ImageFont


######################### code to extract frames begins here ##########################
vidcap = cv2.VideoCapture('horse.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("./images/image"+str(count)+".jpg", image)     # save each frame as JPG file
    return hasFrames
sec = 0
frameRate = 0.25    # it will capture image in each 0.25 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
############################# code to extract the frames ends here ############################




############################# code to convert frames to ascii images begins here ##########################
Character = {
    "standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}
def get_data(mode):
    font = ImageFont.truetype("fonts/DejaVuSansMono-Bold.ttf", size=20)
    scale = 2
    char_list = Character[mode]
    return char_list, font, scale
# Making Background Black or White
bg = "white"
# bg = "black"
if bg == "white":
    bg_code = 255
elif bg == "black":
    bg_code = 0
# Getting the character List, Font and Scaling characters for square Pixels
char_list, font, scale = get_data("complex")
num_chars = len(char_list)
num_cols = 300

pathIn= './images/'
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
files=natsort.natsorted(files)  # sorts images according to name
for i in range(len(files)):
    filename=pathIn + files[i]
    #reading each file
    image = cv2.imread(filename)
    print(filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = image.shape
    cell_w = width / num_cols
    cell_h = scale * cell_w
    num_rows = int(height / cell_h) 
    char_width, char_height = font.getsize("A")
    out_width = char_width * num_cols
    out_height = scale * char_height * num_rows 
    out_image = Image.new("L", (out_width, out_height), bg_code)
    draw = ImageDraw.Draw(out_image)   
    for i in range(num_rows):
        min_h = min(int((i + 1) * cell_h), height)
        row_pix = int(i * cell_h)
        # lst = [i for i in range(5)] => We can make strings/lists/tuples in this way => lst = [0, 1, 2, 3, 4]
        # lst[first:last] gives us a sublist from the first index to the last index excluding the last index => lst[1:4]==[1, 2, 3]
        line = "".join([char_list[
            min(int(
                np.mean(image[row_pix:min_h, int(j*cell_w)
                        :min(int((j + 1) * cell_w), width)]) / 255 * num_chars
            ), num_chars - 1)]
            for j in range(num_cols)]) + "\n"
        # Draw string at a given position (x,y)
        draw.text((0, i * char_height), line, fill=255-bg_code, font=font)
    if bg == "white":
        cropped_image = ImageOps.invert(out_image).getbbox()
    elif bg == "black":
        cropped_image = out_image.getbbox()
    out_image = out_image.crop(cropped_image)
    out_image.save(filename)

############################# code to convert frames to ascii images ends here ############################



############################# code to merge the frames begins here ############################
pathIn= './images/'
pathOut = 'output.avi'
fps = 4          # since a frame was captured every 0.1 second, fps is 10
frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
# files=natsort.natsorted(files)  # sorts images according to name
for i in range(len(files)):
    filename=pathIn + files[i]
    #reading each files
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    
    #inserting the frames into an image array
    frame_array.append(img)
out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
print("Video converted successfully!!!")
out.release()
######################## code to merge the frames ends here ################################
