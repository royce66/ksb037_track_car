input.onButtonPressed(Button.A, function () {
    music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
})
let TRACK_R = pins.digitalReadPin(DigitalPin.P13)
let TRACK_L = pins.digitalReadPin(DigitalPin.P14)
basic.forever(function () {
    if (TRACK_L && TRACK_R) {
        pins.digitalWritePin(DigitalPin.P8, 1)
        pins.digitalWritePin(DigitalPin.P12, 1)
        pins.analogWritePin(AnalogPin.P1, 400)
        pins.analogWritePin(AnalogPin.P2, 400)
    } else if (TRACK_R && !(TRACK_L)) {
        pins.digitalWritePin(DigitalPin.P8, 0)
        pins.digitalWritePin(DigitalPin.P12, 1)
        pins.analogWritePin(AnalogPin.P1, 400)
        pins.analogWritePin(AnalogPin.P2, 200)
    } else if (!(TRACK_R) && TRACK_L) {
        pins.digitalWritePin(DigitalPin.P8, 1)
        pins.digitalWritePin(DigitalPin.P12, 0)
        pins.analogWritePin(AnalogPin.P1, 200)
        pins.analogWritePin(AnalogPin.P2, 400)
    } else {
        pins.analogWritePin(AnalogPin.P1, 0)
        pins.analogWritePin(AnalogPin.P2, 0)
    }
})
