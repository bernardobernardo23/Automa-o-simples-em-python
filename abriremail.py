import pyautogui as pa
import time

pa.press('win')
pa.write("chrome")
pa.press('ENTER')
time.sleep(2)
pa.press('TAB')
pa.press('ENTER')
time.sleep(1)
pa.write("gmail.com")
pa.press('ENTER')
