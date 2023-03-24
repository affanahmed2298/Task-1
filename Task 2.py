import cv2


input_video = cv2.VideoCapture('"C:\Users\HP\Desktop\\test1.mp4"')        #loading the input video 


fps = int(input_video.get(cv2.CAP_PROP_FPS))            #getting frame rate of the video using CAP_PROP_FPS

# Define the output video codec and frame size
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))      #getting the frame width of the input video such that output video can match the frame dimensions
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))    #getting the frame height of the input video for the same reason as above
print(height,width,fourcc,sep = "\n")
output_video = cv2.VideoWriter('"C:\Users\HP\Desktop\lol1.mp4"', fourcc, fps, (width, height), isColor=True)      #initializing new video with original input video format

# Loop through the input video frames and write every 4th frame to the output video
frame_count = 1
while True:
    ret, frame = input_video.read()
    if not ret:
        break
    
    if frame_count % 4 == 0:
        output_video.write(frame)
    frame_count += 1


input_video.release()
output_video.release()

cv2.destroyAllWindows()