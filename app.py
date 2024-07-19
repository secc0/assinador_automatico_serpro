import pyautogui
import time
import pyperclip

x_click1 = 1601
y_click1 = 1053
x_click2 = 1606
y_click2 = 971
x_click3 = 1773
y_click3 = 548
x_click4 = 629
y_click4 = 471
x_click5 = 753  # Posição atualizada
y_click5 = 644  # Posição atualizada
x_click6 = 724
y_click6 = 371
x_click7 = 916
y_click7 = 800
x_click8 = 826
y_click8 = 650
x_click9 = 1028
y_click9 = 838
x_click10 = 1019
y_click10 = 555
x_click11 = 726
y_click11 = 403

x_start = 1308
y_start = 174
x_end = 1308
y_end = 350

x_mouse_down = 369
y_mouse_down = 238
x_mouse_up = 1428
y_mouse_up = 560

x_folder_click = 698
y_folder_click = 361

x_click_after_delay_1 = 1271
y_click_after_delay_1 = 705
x_click_after_delay_2 = 973
y_click_after_delay_2 = 550
x_click_after_delay_3 = 800
y_click_after_delay_3 = 1051

time.sleep(0.5)

pyautogui.moveTo(x_click1, y_click1, duration=0.09)
pyautogui.click()

pyautogui.moveTo(x_click2, y_click2, duration=0.09)
pyautogui.click()

pyautogui.moveTo(x_click3, y_click3, duration=0.09)
pyautogui.click()

pyautogui.moveTo(x_click4, y_click4, duration=0.09)
pyautogui.click()

pyautogui.moveTo(x_click5, y_click5, duration=0.09)
pyautogui.doubleClick()

time.sleep(0.09)
pyautogui.moveTo(x_click6, y_click6, duration=0.09)
pyautogui.click()
pyautogui.click()

time.sleep(2.2)
for _ in range(6):
    pyautogui.moveTo(x_click7, y_click7, duration=0.09)
    pyautogui.click()

pyautogui.moveTo(x_start, y_start, duration=0.3)
pyautogui.mouseDown()
pyautogui.dragTo(x_end, y_end, duration=0.3)
pyautogui.mouseUp()

pyautogui.moveTo(x_click8, y_click8, duration=0.09)
pyautogui.click()

pyautogui.moveTo(x_click9, y_click9, duration=0.09)
pyautogui.click()

pyautogui.moveTo(x_click10, y_click10, duration=1.4)
pyautogui.click()

pyautogui.moveTo(726, 403, duration=0.09)
pyautogui.mouseDown()
pyautogui.mouseUp()

time.sleep(0.09)
pyautogui.moveTo(x_click11, y_click11, duration=0.09)
pyautogui.click()

pyautogui.moveTo(x_click_after_delay_1, y_click_after_delay_1, duration=0.09)
pyautogui.click()

pyautogui.moveTo(x_click_after_delay_2, y_click_after_delay_2, duration=0.09)
pyautogui.click()

pyautogui.moveTo(x_click_after_delay_3, y_click_after_delay_3, duration=0.09)
pyautogui.click()

time.sleep(0.6)

pyperclip.copy("dossies_BT")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(0.5)
pyautogui.moveTo(x_click_after_delay_3, y_click_after_delay_3, duration=0.5)
pyautogui.click()

time.sleep(0.8)

pyperclip.copy("BT_dossies assinados")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
