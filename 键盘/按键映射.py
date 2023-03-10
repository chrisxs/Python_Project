import keyboard

# 获取用户输入的两个按键
print("请输入第一个按键：")
key1 = input()
print("请输入第二个按键：")
key2 = input()

# 设置按键映射
keyboard.add_hotkey(key1, lambda: keyboard.press_and_release('ctrl+c'))
keyboard.add_hotkey(key2, lambda: keyboard.press_and_release('ctrl+v'))

# 监听键盘事件
keyboard.wait()
