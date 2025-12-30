import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.layers import Layers
from kmk.extensions.international import International

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.extensions.append(International())

split = Split(
    split_type=SplitType.UART,
    split_side=SplitSide.LEFT,  # Change this to RIGHT if you are flashing the right half
    data_pin=board.GP0, 
    data_pin2=board.GP1, 
    use_pio=True, 
    uart_flip=True
)
keyboard.modules.append(split)

keyboard.col_pins = (board.GP21, board.GP20, board.GP19, board.GP18, board.GP17, board.GP16)
keyboard.row_pins = (board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [[
    # Row 1: left 6 keys, then right 6 keys
    KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,    KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS,
    
    # Row 2: left 6 keys, then right 6 keys
    KC.ESC,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,     KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC,
    
    # Row 3: left 6 keys, then right 6 keys
    KC.NUBS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,     KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,
    
    # Row 4: left 6 keys, then right 6 keys
    KC.NUHS, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,     KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT,
    
    # Row 5: left 6 keys, then right 6 keys
    KC.NO,   KC.NO,   KC.SCLN, KC.QUOT, KC.LCTL, KC.SPC,   KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT, KC.NO,   KC.NO,
    
    # Row 6: left 6 keys, then right 6 keys
    KC.NO,   KC.NO,   KC.ENT,  KC.LALT, KC.LGUI, KC.BSPC,  KC.DEL,  KC.TAB,  KC.RALT, KC.RCTL, KC.NO,   KC.NO,
]]


if __name__ == '__main__':
    keyboard.go()

