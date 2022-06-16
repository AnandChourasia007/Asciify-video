# Asciify-video
This project aims at converting mp4 videos to ascii videos. Ascii videos means videos where each frame consists of ASCII characters instead of pixels. The video is broken down into several frames. The frame_rate can be decided by the user by changing the corresponding variable. Any change in frame_rate must be accompanied with corresponding change in the fps keeping in mind the relation, frame_rate x fps = 1. Each frame is then converted to grayscale image which are then processed and converted to ASCII images one by one. The ASCII images are then merged to create the final video output.

# How to run the project
1.Fork this repository, then clone it. 

2.Install the dependencies by using the following commands,

        pip install opencv-python
        pip install numpy
        pip install natsort
        pip install os
        pip install pillow
        
3.Delete the contents of the images folder and the video1.avi file. 

4.Put the video you want to asciify as 'video.mp4'.

5.Open terminal locate the directory where you have stored the downloaded code and run 'python videotoascii.py'

6.The terminal will display the name of each frame as it processes them in order.

7.After approximately (fps x duration of the video) seconds, the frames will be merged to create the output ascii video as 'output.avi'.

8.The terminal will show 'Video converted successfully!!!' message, you can now have the output.

# Internal Working
The following steps take place from when a video is input to when the output is obtained:

-> The first part of the code is yo rxtract the frames of the video as jpeg images. This is achieved by using opencv. Each frame is obtained by running a while loop as long as frames exist. As the frames are extracted, they are written using the cv2.imwrite() function.
 
-> The second part of the code converts each frame to ASCII images. We have two sets of characters to use depending on the clarity that we require and also the speed. The standard charcater set is processed faster giving relatively quicker results than the complex character set. We also have the choice to decide whether the final output will be white image on black canvas or black image on white canvas. Next we must sort the extracted images by name, for this we use natsort to avoid a string sorting algorithm. Then iterating over all the frames we calculate the height and width of the output frames, and map the pixels to the ASCII characters. AFter this the extra black or white portion is cropped and the images are ready to be merged.

-> The third part of the code is to merge the ASCII frames. Here also, same as above, we iterate over all the frames, read them and append to a  list. This list is then used to write to an empty variable which was intialised using cv2.VideoWriter() function. Using a for loop, the ASCII frames are appended to the variable. After creating the output file 'output.avi' this variable is cleared.


#Learnings from this project

