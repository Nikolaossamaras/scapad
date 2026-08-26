import board
import keypad
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

keys = keypad.Keys(
    (board.D10, board.D9, board.D8),
    value_when_pressed=False,
    pull=True,
)

while True:
    event = keys.events.get()

    if event is None:
        continue
    if not event.pressed:
        continue

    if event.key_number == 0:
        keyboard.send(Keycode.CONTROL, Keycode.C)

    elif event.key_number == 1:
        keyboard.send(Keycode.CONTROL, Keycode.V)

    elif event.key_number == 2:
        keyboard.send(Keycode.CONTROL, Keycode.Z)
