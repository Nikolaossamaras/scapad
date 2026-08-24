import board
import keypad
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


# USB HID keyboard
keyboard = Keyboard(usb_hid.devices)


# PCB switch connections
#
# SW1 -> XIAO D10 -> GND
# SW2 -> XIAO D9  -> GND
# SW3 -> XIAO D8  -> GND
#
# The switches are active-low, so a pressed switch reads False.
keys = keypad.Keys(
    (board.D10, board.D9, board.D8),
    value_when_pressed=False,
    pull=True,
)


while True:
    event = keys.events.get()

    if event is None:
        continue

    # Only send a shortcut when a key is pressed,
    # not when it is released.
    if not event.pressed:
        continue

    if event.key_number == 0:
        # SW1 -> Ctrl+C (Copy)
        keyboard.send(Keycode.CONTROL, Keycode.C)

    elif event.key_number == 1:
        # SW2 -> Ctrl+V (Paste)
        keyboard.send(Keycode.CONTROL, Keycode.V)

    elif event.key_number == 2:
        # SW3 -> Ctrl+Z (Undo)
        keyboard.send(Keycode.CONTROL, Keycode.Z)
