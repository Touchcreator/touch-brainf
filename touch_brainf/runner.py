from touch_brainf.errors import *

class Runner:

    def __init__(self, code: str):
        self.code = code



    def interpret(self, code: str): # interpret the program
        mem = [0]
        memPos = 0

        i = 0
        while i < len(code):
            if code[i] == ">":
                memPos += 1
                if len(mem) <= memPos:
                    mem.append(0)
            if code[i] == "<":
                memPos -= 1
                if memPos < 0:
                    raise PointerNotInRangeError("Attempted to go to a negative memory position", memPos)
            if code[i] == "+":
                mem[memPos] += 1
                if mem[memPos] >= 256:
                    mem[memPos] = 0
            if code[i] == "-":
                mem[memPos] -= 1
                if mem[memPos] <= -1:
                    mem[memPos] = 255    
            if code[i] == ".":
                print(chr(mem[memPos]), end="")
            if code[i] == ",":
                ascii_to_numb = str(input("Input Requested (Only the first character will be accepted): "))
                mem[memPos] = ord(ascii_to_numb[0])
            if code[i] == "[":
                print("[ detected")
            if code[i] == "]":
                print("] detected")
                
            i+=1 # iterate (or something)

    def run(self):
        self.interpret(self.code)


            


    