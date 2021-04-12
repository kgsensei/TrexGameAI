import pyautogui as pya
from PIL import ImageGrab
import cv2, time

def Tick():
     obj=False
     obd=False
     image=ImageGrab.grab(bbox=(737,432,875,477))
     image.save("TickScanner.png")
     if pya.locate("./Danger/A_1.png","TickScanner.png",confidence=0.8,grayscale=True)!= None:
          obj=True
     if pya.locate("./Danger/A_2.png","TickScanner.png",confidence=0.8,grayscale=True)!= None:
          obj=True
     if pya.locate("./Danger/A_3.png","TickScanner.png",confidence=0.8,grayscale=True)!= None:
          obj=True
     if pya.locate("./Danger/A_4.png","TickScanner.png",confidence=0.8,grayscale=True)!= None:
          obj=True
     if pya.locate("./Danger/B_1.png","TickScanner.png",confidence=0.8,grayscale=True)!= None:
          obd=True
     if pya.locate("./Danger/B_2.png","TickScanner.png",confidence=0.8,grayscale=True)!= None:
          obd=True
     if pya.locate("./Danger/B_3.png","TickScanner.png",confidence=0.8,grayscale=True)!= None:
          obj=True
     if pya.locate("./Danger/B_4.png","TickScanner.png",confidence=0.8,grayscale=True)!= None:
          obj=True
     if obd == True:
          return "ObD"
     if obj == True:
          return "ObJ"

while True:
     OBJTF=Tick()
     if OBJTF == "ObJ":
          print("Object Detected - Jump")
          pya.press('up')
     elif OBJTF == "ObD":
          pya.keyDown('down')
          print("Object Detected - Duck")
          time.sleep(0.125)
          pya.keyUp('down')
     time.sleep(0.00075)
