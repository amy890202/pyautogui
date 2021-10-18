#https://hackmd.io/@truckski/rJ6hmNpUN?type=view
import pyautogui
from time import sleep
pyautogui.PAUSE = 1 #指令間隔一秒
# pyautogui.hotkey('win', 'r')
# #如果會卡中文輸入法，請切換到英文 (下載英文鍵盤)
# #pyautogui.press('shiftleft') 無法切
# #pyautogui.click(1749, 1065)#pyautogui.position()
# pyautogui.typewrite('cmd')
# sleep(5)
# pyautogui.press('enter')
# #pyautogui.click(1749, 1065)
# pyautogui.typewrite('echo Hello world')
# pyautogui.press('enter')

pyautogui.hotkey('win', 'd')
pyautogui.doubleClick(242,173)
pyautogui.typewrite('https://sketchpad.app/')
pyautogui.press('enter')
pyautogui.click(1770,438)
pyautogui.moveRel(0, 0, 10)
pyautogui.click(30,257)
# 6. 移動到作畫區

pyautogui.moveTo(901,223)

# 7. 畫出樹
pyautogui.dragRel(50,100,0.5)
pyautogui.dragRel(-100,0,0.5)
pyautogui.dragRel(50,100,0.5)
pyautogui.dragRel(-100,0,0.5)

pyautogui.dragRel(-50,100,0.5)
pyautogui.dragRel(-100,-35,0.5)
pyautogui.dragRel(50,-100,0.5)

pyautogui.dragRel(-100,-20,0.5)
pyautogui.dragRel(150,-70,0.5)
pyautogui.dragRel(-100,-20,0.5)
pyautogui.dragRel(255,-80,0.5)
