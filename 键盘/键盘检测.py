import keyboard

def on_press(event):
    if event.event_type == "down":
        print(f"您按下了按键：{event.name}")

keyboard.hook(on_press)

try:
    keyboard.wait()
except KeyboardInterrupt:
    print("程序已停止。")
