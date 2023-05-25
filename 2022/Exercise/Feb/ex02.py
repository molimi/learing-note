"""
Version: 0.1
Author: CarpeDiem
Date: 2023/5/12
Description: 
思路：每晚按时自动发送消息
"""
import pyautogui,pyperclip,time
from urllib.request import urlopen

def Open_Wechat():
    pyautogui.hotkey('ctrl', 'alt', 'w')
    time.sleep(1)

def Chat_Who(Who_Name):
    pyautogui.hotkey("ctrl","f")
    pyperclip.copy(Who_Name)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.hotkey('Enter')
    time.sleep(1)

def Sent_Msg(Msg):
    pyperclip.copy(str(Msg))
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('Enter')


if __name__=='__main__':
    YU = 0
    while True:
        NOW = str(time.strftime('%H%M', time.localtime()))
        if NOW  == "2310":
            YU += 1
            Open_Wechat()
            Chat_Who("Bae")
            # Sent_Msg(Get_Weather())
            Sent_Msg("晚安咯，扬扬，祝做个好梦！愿你带着“称心如意”的感觉，怀着“怡然自得”的心情，伴着“妙不可言”的美梦，接收“赏心悦目”的祝福，祝今晚睡一个“甘之如饴”的好觉！")
            print("又过去1天：合计守护", YU, "天")
            time.sleep(86000)