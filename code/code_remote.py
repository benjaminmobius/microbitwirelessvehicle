def on_button_pressed_a():
    radio.send_number(33)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    radio.send_number(71)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_b():
    radio.send_number(28)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_right():
    radio.send_number(70)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

radio.set_group(25)