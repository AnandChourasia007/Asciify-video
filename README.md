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
