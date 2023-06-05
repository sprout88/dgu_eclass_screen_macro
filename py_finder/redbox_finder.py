import pywin32_draw
import pyautogui as p
from PIL import Image
import os, time

app = pywin32_draw.draw()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
target_img_path = "confirm_button.png"
img = Image.open(target_img_path)

width,height=img.size
print(width)

while(True):
    target_img_cord = p.locateOnScreen(target_img_path)
    if(target_img_cord!=None):
        print("target found!")
        app.rect(target_img_cord.left,target_img_cord.top,target_img_cord.width,target_img_cord.height,(255,0,0))
        time.sleep(5)
        p.click(target_img_cord.left + target_img_cord.width / 2, target_img_cord.top + target_img_cord.height / 2)
        print("clicked!!!")
    else:
        print("target is None...")
