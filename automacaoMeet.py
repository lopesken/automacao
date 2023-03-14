#Para entrar automaticamente na sala do Meet

import pyautogui
import time

pyautogui.PAUSE= 2
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.hotkey('alt','space')
pyautogui.press('x')
pyautogui.write('meet.google.com/kuf-dorx-ibq')
pyautogui.press('enter')
time.sleep(5)
pyautogui.hotkey('ctrl', 'e')
pyautogui.hotkey('ctrl', 'd')
pyautogui.click(x=961, y=390)

#print(pyautogui.position())