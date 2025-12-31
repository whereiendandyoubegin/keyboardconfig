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
    split_side=SplitSide.LEFT,
    data_pin=board.GP0, 
    data_pin2=board.GP1, 
    use_pio=True, 
    uart_flip=True
)
keyboard.modules.append(split)

keyboard.col_pins = (board.GP21, board.GP20, board.GP19, board.GP18, board.GP17, board.GP16)
keyboard.row_pins = (board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    # Layer 0 (Base)
    [
    # Row 1: left 6 keys, then right 6 keys
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,    KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS,
    
        # Row 2: left 6 keys, then right 6 keys
        KC.ESC,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,     KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.PGUP,
    
        # Row 3: left 6 keys, then right 6 keys
        KC.NUBS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,     KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.PGDN,
    
        # Row 4: left 6 keys, then right 6 keys
        KC.TAB,  KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,     KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.EQUAL,
    
        # Row 5: left 6 keys, then right 6 keys
        KC.NO,   KC.NO,   KC.BSPC, KC.COMM, KC.LCTL, KC.SPC,   KC.SPC,  KC.RSFT, KC.RBRC, KC.LBRC, KC.NO,   KC.NO,
    
        # Row 6: left 6 keys, then right 6 keys
        KC.NO,   KC.NO,   KC.ENT,   KC.MO(1),   KC.LGUI,   KC.BSPC,    KC.LALT, KC.LGUI, KC.RCTL, KC.TAB,  KC.NO,   KC.NO,    ],
    # Layer 1 (when left alt is held)
    [
        # Row 1 - Number keys become F keys
        KC.TRNS, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,    KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.TRNS,
        # Row 2
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        # Row 3 - HJKL become arrow keys
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT, KC.TRNS, KC.TRNS,
        # Row 4 - Comma becomes apostrophe
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.QUOT, KC.TRNS, KC.TRNS, KC.TRNS,
        # Row 5
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        # Row 6
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ],
]

if __name__ == '__main__':
    keyboard.go()
