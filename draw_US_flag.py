import pyautogui
pyautogui.PAUSE = 1#指令間隔 1 秒
from time import sleep

# 1. 打開小畫家
pyautogui.hotkey('win','r')
pyautogui.typewrite('mspaint')
pyautogui.press('enter')
sleep(1)
pyautogui.hotkey('win','up') # 最大化


pyautogui.click(970, 78)#red
# 選到矩形(根據你的電腦選位置)

for i in range(7):#7
    pyautogui.click(523, 80)
    pyautogui.moveTo(100, 200+40*i)
    pyautogui.dragRel(494, 20, 0.3)
    pyautogui.click(325, 90)#fullin
    pyautogui.click(150, 200+40*i+10)

#blue rec
pyautogui.click(1107, 75)#choose blue
pyautogui.click(850, 118)
pyautogui.click(1107, 75)#choose blue
pyautogui.click(523, 80)
pyautogui.moveTo(100, 200)
pyautogui.dragRel(200, 160, 0.3)
pyautogui.click(672, 104)
pyautogui.click(691, 159)

pyautogui.click(503, 130)#choose star
pyautogui.click(890, 107)#white
pyautogui.click(802, 97)
pyautogui.click(890, 107)#white
pyautogui.click(853, 88)
pyautogui.click(890, 107)#white

for i in range(6):
    for j in range(5):
        x = 100 + 10 +33 * i
        y = 200 + 10 +33 * j
        pyautogui.moveTo(x, y)
        pyautogui.dragRel(14, 14, 0.3)
for i in range(5):
    for j in range(4):
        x = 100 + 24 +33 * i
        y = 200 + 24 +33 * j
        pyautogui.moveTo(x, y)
        pyautogui.dragRel(14, 14, 0.3)

