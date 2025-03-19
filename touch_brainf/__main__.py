import touch_brainf
import sys
import os
import random

filename = str(sys.argv[1])

if os.path.splitext(filename)[1] == ".bf":
    with open(filename, "r") as brainf_code:
        global code
        code = brainf_code.read()
        
else:

    what_to_print = random.randint(1, 10)

    if what_to_print != 4: print("Please import a .bf file")
    else: print("IMPORT A BRAN FLAKES FILE BOIIII 🗿🗿🗿🔥🔥🔥")

    exit()

# code = "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.[>+<-]>-."

runner = touch_brainf.Runner(code)

runner.run()