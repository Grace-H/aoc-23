#!/usr/bin/env python3

from queue import Queue
from parse import compile
from itertools import repeat
from collections import Counter
from functools import reduce
from operator import mul, concat
import sys
import numpy as np

def strparse(lines):
    p = compile("Game {:d}: {}\n")
    return map(getattr, map(p.parse, lines), repeat('fixed'))

class Mod():
    def __init__(self, name, outputs):
        self.outputs = outputs
        self.name = name

    # True is high, False is low
    def pulse(self, i, p):
        pass

button_presses = 0
modules = {"output": Mod("output", [])}
queue = Queue()

class RX(Mod):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)

    def pulse(self, i, p):
        if not p:
            print(button_presses)
            sys.exit()

class BC(Mod):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)

    def pulse(self, i, p):
        for o in self.outputs:
            queue.put((modules[o], self, p))

class FF(Mod):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)
        self.prev = False

    def pulse(self, i, p):
        if not p:
            self.prev = not self.prev
            for o in self.outputs:
                queue.put((modules[o], self, self.prev))

class Con(Mod):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)
        self.prev = False
        self.inputs = {}

    def add_input(self, i):
        self.inputs[i] = False

    def pulse(self, i, p):
        self.inputs[i] = p
        anded = True
        for k in self.inputs:
            anded &= self.inputs[k]
        new_p = not anded
        for o in self.outputs:
            queue.put((modules[o], self, new_p))
    
filename = "input20"
# filename = "test201"
file = open(filename, 'r')
lines = file.readlines() #[l.split(" ") for l in file.readlines()]
file.close()

cons = []
for l in lines:
    split = l.strip().split(" ")
    outs = list(map(lambda s: s.strip(","), split[2:]))
    name = ""
    m = None
    if split[0] == "broadcaster":
        name = split[0]
        m = BC(name, outs)
    elif split[0][0] == "%":
        name = split[0][1:]
        m = FF(name, outs)
    elif split[0][0] == "&":
        name = split[0][1:]
        m = Con(name, outs)
        cons.append(name)
    modules[name] = m

modules["rx"] = RX("rx", [])

# Hook up inputs to cons
for m in modules:
    mod = modules[m]
    for o in mod.outputs:
        if o in cons:
            modules[o].add_input(mod)


while(True):
    queue.put((modules["broadcaster"], None, False))
    button_presses += 1
    if button_presses % 1000 == 0:
        print("at", button_presses)

    while not queue.empty():
        m, i, p = queue.get()
        m.pulse(i, p)

