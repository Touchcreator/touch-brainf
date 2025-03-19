import touch_brainf
import sys
import os
import random

def file_error():
    what_to_print = random.randint(1, 10)

    if what_to_print != 4:
        print("Please import a .bf file")
    else:
        print("IMPORT A BRAN FLAKES FILE BOIIII 🗿🗿🗿🔥🔥🔥")

    exit()

def main():
    try:
        filename = str(sys.argv[1])
    except IndexError:
        file_error()

    if os.path.splitext(filename)[1] == ".bf":
        with open(filename, "r", encoding="utf8") as brainf_code:
            global code
            code = brainf_code.read()  
    else:
        file_error()

    # code = "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.[>+<-]>-."

    runner = touch_brainf.Runner(code)

    runner.run()

if __name__ == "__main__":
    main()