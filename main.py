TRACK_R = 0
TRACK_L = 0

def on_button_pressed_a():
    music.start_melody(music.built_in_melody(Melodies.DADADADUM),
        MelodyOptions.ONCE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    global TRACK_R, TRACK_L
    TRACK_R = pins.digital_read_pin(DigitalPin.P13)
    TRACK_L = pins.digital_read_pin(DigitalPin.P14)
    if TRACK_L and TRACK_R:
        pins.digital_write_pin(DigitalPin.P8, 1)
        pins.digital_write_pin(DigitalPin.P12, 1)
        pins.analog_write_pin(AnalogPin.P1, 400)
        pins.analog_write_pin(AnalogPin.P2, 400)
    elif TRACK_R and not (TRACK_L):
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P12, 1)
        pins.analog_write_pin(AnalogPin.P1, 400)
        pins.analog_write_pin(AnalogPin.P2, 200)
    elif not (TRACK_R) and TRACK_L:
        pins.digital_write_pin(DigitalPin.P8, 1)
        pins.digital_write_pin(DigitalPin.P12, 0)
        pins.analog_write_pin(AnalogPin.P1, 200)
        pins.analog_write_pin(AnalogPin.P2, 400)
    else:
        pins.analog_write_pin(AnalogPin.P1, 0)
        pins.analog_write_pin(AnalogPin.P2, 0)
basic.forever(on_forever)
