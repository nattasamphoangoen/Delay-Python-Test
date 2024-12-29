import sys
import time
from time import sleep

# So I'ma love you every night like it's the last night
# Like it's the last night 
# If the world was ending 
# I'd wanna be next to you 
# If the party was over 
# And our time on Earth was through 
# I'd wanna hold you just for a while 
# And die with a smile 
# If the world was ending 
# I'd wanna be next to you
# Right next to you

lines = [
    ("So I'ma love you every night like it's the last night", 0.1),
    ("Like it's the last night", 0.2),
    ("If the world was ending", 0.3),
    ("I'd wanna be next to you", 0.1),
    ("If the party was over", 0.2),
    ("And our time on Earth was through", 0.3),
    ("I'd wanna hold you just for a while", 0.1),
    ("And die with a smile", 0.2),
    ("If the world was ending", 0.3),
    ("I'd wanna be next to you", 0.1),
    ("Right next to you", 0.2),
]

delays = [0.1, 0.2, 0.3, 0.1, 0.2, 0.3, 0.1, 0.2, 0.3, 0.1, 0.2]

for (line, char_delay), delay in zip(lines, delays): 
    for char in line:
        print(char, end='', flush=True)
        sys.stdout.flush()
        sleep(char_delay)  
    time.sleep(delay)  
    print('')  
