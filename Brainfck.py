from sys import argv
from sys import exit

class Memory:
    __maxValue = 127
    __mem = []
    __ptr = 0

    def __init__(self):
        self.__mem.append(0)

    def go_right(self):
        if len(self.__mem) <= self.__ptr+1:
            self.__mem.append(0)
        self.__ptr+=1

    def go_left(self, iptr):
        if(self.__ptr - 1 < 0):
            r = "Index out of Bounds (Char at " + iptr.__str__() +"): Memory index cannot be negative!"
            exit(r)
        self.__ptr-=1

    def decrease(self, iptr):
        if(self.__mem[self.__ptr] - 1 < 0):
            r = "Illegal State (Char at " + iptr.__str__() + "): Memorycellvalue cannot be negative"
            exit(r)
        self.__mem[self.__ptr]-=1

    def increase(self, iptr):
        if (self.__mem[self.__ptr] + 1 > self.__maxValue):
            r = "Illegal State (Char at " + iptr.__str__() + "): Memorycellvalue cannot exceed 16Byte"
            exit(r)
        self.__mem[self.__ptr]+=1

    def get_value(self):
        return self.__mem[self.__ptr]

    def set_value(self, value, iptr):
        if value > self.__maxValue:
            r = "Illegal State (Char at " + iptr.__str__() + "): Memorycellvalue cannot exceed 16Byte"
            exit(r)
        self.__mem[self.__ptr] = value








# initializing code from arguments

code = ""
args = argv.copy()
args[0] = ""
for arg in args:
    code+=arg

# starting console output

print("Executing code:")
print(code)
print("")
print("-------------------------------------------\n\n")


# counting loops

loopBeginCount = 0
loopEndCount = 0

for c in code:
    if c == "[":
        loopBeginCount += 1
    elif c == "]":
        loopEndCount += 1

# checking consistency

if loopBeginCount != loopEndCount:
    exit("loops inconsistent")

loopCount = loopBeginCount

del loopBeginCount
del loopEndCount

# determining loops

loopBegin = []
loopEnd   = []
loopDepth = 0

for i, c in enumerate(code):
    if c == "[":
        loopDepth+=1
        for j, d in enumerate(code[i+1:], i+1):
            if d == "]":
                loopDepth-=1
                if loopDepth == 0:
                    loopBegin.append(i)
                    loopEnd.append(j)
                    break
            elif d == "[":
                loopDepth+=1


# initializing instruction pointer and wokring-memory

iptr = 0
mem = Memory()

# main loop

while(iptr < len(code)):
    if code[iptr] == '+':
        mem.increase(iptr)
    elif code[iptr] == '-':
        mem.decrease(iptr)
    elif code[iptr] == '<':
        mem.go_left(iptr)
    elif code[iptr] == '>':
        mem.go_right()
    elif code[iptr] == ']':
        if mem.get_value() != 0:
            for i in range(0, loopCount):
                if loopEnd[i] == iptr:
                    iptr = loopBegin[i]
                    break
    elif code[iptr] == ".":
        print(chr(mem.get_value()), end='')
    elif code[iptr] == ",":
        tmp = input()
        tmpint = ord(tmp[0])
        mem.set_value(tmpint, iptr)


    iptr+=1

# end text

print("\n\n-------------------------------------------")
