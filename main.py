import pyautogui as pya
from PIL import ImageGrab
import pytesseract, cv2, numpy, time, keyboard
pytesseract.pytesseract.tesseract_cmd = r'D:\\Users\\jt\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
def Tick():
     obj=False;obd=False
     image=ImageGrab.grab(bbox=(705,366,868,429))
     image.save("TickScanner.png")
     if pya.locate("./Danger/A_1.png", "TickScanner.png", confidence=0.7) != None:
          obj=True
     if pya.locate("./Danger/A_2.png", "TickScanner.png", confidence=0.7) != None:
          obj=True
     if pya.locate("./Danger/A_3.png", "TickScanner.png", confidence=0.7) != None:
          obj=True
     if pya.locate("./Danger/A_4.png", "TickScanner.png", confidence=0.7) != None:
          obj=True
     if pya.locate("./Danger/B_1.png", "TickScanner.png", confidence=0.7) != None:
          obd=True
     if pya.locate("./Danger/B_2.png", "TickScanner.png", confidence=0.7) != None:
          obd=True
     if pya.locate("./Danger/B_3.png", "TickScanner.png", confidence=0.7) != None:
          obj=True
     if pya.locate("./Danger/B_4.png", "TickScanner.png", confidence=0.7) != None:
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
     time.sleep(0.0005)
