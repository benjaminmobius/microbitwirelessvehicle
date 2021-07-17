def on_received_number(receivedNumber):
    global groupnumber
    groupnumber = receivedNumber
    if groupnumber == 70:
        kitronik_servo_lite.turn_right(90)
    elif groupnumber == 33:
        kitronik_servo_lite.drive_forwards(7)
    elif groupnumber == 28:
        kitronik_servo_lite.drive_backwards(7)
    else:
        if groupnumber == 71:
            kitronik_servo_lite.turn_left(90)
radio.on_received_number(on_received_number)

groupnumber = 0
radio.set_group(25)
kitronik_servo_lite.set_distance_per_second(7)
kitronik_servo_lite.set_degrees_per_second(90)
basic.show_icon(IconNames.HAPPY)