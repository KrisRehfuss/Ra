import math


def Convert():
    Hz = input("What note in Hz? ")
    if Hz.isdigit():
        Hz = int(Hz)
    else:
        print("must be a digit.")
    Note2BPM = Hz * 60
    print(f'x60 {Note2BPM}')
    return Note2BPM


def GiveBPM(x):
    BPM = int(x)
    while BPM > 100:
        BPM = BPM/2
        print(f'x/2{BPM}')
    else:
        print(f'BPM is {BPM}')
        return BPM


def MakeUsable(y):
    RealBPM = float(y)
    while RealBPM < 60:
        RealBPM = RealBPM*2
    else:
        RealBPM = round(RealBPM)
        print(f'x2 = {RealBPM}bpm')
        return RealBPM


def Main():
    MakeUsable(GiveBPM(Convert()))


Main()
