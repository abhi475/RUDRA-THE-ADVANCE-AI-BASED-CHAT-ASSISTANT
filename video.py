import cv2
import os
from threading import Thread

def play_video():
    video = cv2.VideoCapture('animation.mp4')  # Replace 'animation.mp4' with your video file path
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    cv2.namedWindow('Video Player', cv2.WINDOW_NORMAL)

    background = cv2.imread('bg.jpg')  # Replace 'bg.jpg' with your background image path
    if background is None:
        print("Error: Could not load background image.")
        video.release()
        cv2.destroyAllWindows()
        return

    desired_width = 720
    desired_height = 380

    while True:
        ret, frame = video.read()

        if not ret:
            video = cv2.VideoCapture('animation.mp4')
            continue

        background = cv2.resize(background, (desired_width, desired_height))
        resized_frame = cv2.resize(frame, (desired_width, desired_height))
        background[:] = resized_frame

        cv2.imshow('Video Player', background)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

def main():
    video_thread = Thread(target=play_video)
    video_thread.start()

    # Your other code or function calls go here
    # ...

    # Wait for the video thread to finish
    video_thread.join()

if __name__ == "__main__":
    main()