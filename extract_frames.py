import cv2
import os

video_path = "recordings/gameplay.mp4"
output_folder = "frames"

os.makedirs(output_folder, exist_ok=True)

video = cv2.VideoCapture(video_path)

fps = video.get(cv2.CAP_PROP_FPS)
print(f"Video FPS: {fps}")

frame_interval = int(fps / 2)

frame_number = 0
saved_images = 0

while True:
    success, frame = video.read()

    if not success:
        break

    if frame_number % frame_interval == 0:
        filename = os.path.join(
            output_folder,
            f"frame_{saved_images:04d}.jpg"
        )

        cv2.imwrite(filename, frame)
        saved_images += 1

    frame_number += 1
video.release()
print(f"Saved {saved_images} images.")