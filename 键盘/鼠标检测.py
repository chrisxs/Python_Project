from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        if button == mouse.Button.left:
            print("左键")
        elif button == mouse.Button.middle:
            print("中键")
        elif button == mouse.Button.right:
            print("右键")
        else:
            print("非标准鼠标按键")

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
