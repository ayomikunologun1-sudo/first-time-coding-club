def on_button_pressed_a():
    radio.send_string("")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string("Can we chat")
    music.play(music.string_playable("E D G F B A C5 B ", 120),
        music.PlaybackMode.UNTIL_DONE)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    music.stop_all_sounds()
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(3)
radio.send_number(10)