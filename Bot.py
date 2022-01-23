from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Y:600
#x1 560
#660
#760
#860 

def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.05) #this pauses it for 1/100th of a second
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
	if pyautogui.pixel(560, 700)[0] == 0: #[0] is the index for R/red
		click(560, 700)	
	if pyautogui.pixel(660, 700)[0] == 0:
		click(660, 700)	
	if pyautogui.pixel(760, 700)[0] == 0:
		click(760, 700)
	if pyautogui.pixel(860, 700)[0] == 0:
		click(860, 700)
