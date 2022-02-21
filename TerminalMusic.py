'''
Terminal Music Visualizer
'''

# Imports
import time
import numpy as np

# Main Functions
# Terminal Wave Functions
def TerminalWave_Random(print_obj, c="*", delay=0.1, max_frames=-1, displayRange=(1, 10)):
    '''
    Randomly generates a wave and displays it in the terminal object.
    '''
    # Generate wave and display
    wave_val = np.random.randint(displayRange[0], displayRange[1]+1)
    i = 0
    while(max_frames < 0 or i < max_frames):
        # Generate random shift (+1/-1)
        wave_shift = np.random.choice([-1, 1])
        # Calculate New Wave Val
        wave_val = min(max(wave_val + wave_shift, displayRange[0]), displayRange[1])
        # Display wave
        print_obj(c * wave_val)
        # Delay
        time.sleep(delay)
        i += 1

# Main Vars
TERMINAL_WAVES = {
    "Random": TerminalWave_Random
}

# Driver Code
# # Params
# DISPLAY_CHAR = "-"
# DELAY = 0.01
# MAX_FRAMES = -1
# DISPLAY_RANGE = (1, 10)
# # Params

# # RunCode
# TerminalVis_Random(print, DISPLAY_CHAR, DELAY, MAX_FRAMES, DISPLAY_RANGE)