#!/usr/bin/env python3

from queue import Queue

class Mod():
    def __init__(self, name, outputs):
        self.outputs = outputs
        self.name = name

    # True is high, False is low
    def pulse(self, i, p):
        pass

modules = {"output": Mod("output", [])}
queue = Queue()
pulses = {True: 0, False: 0}

class BC(Mod):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)

    def pulse(self, i, p):
        ps = 0
        for o in self.outputs:
            if o in modules:
                queue.put((modules[o], self, p))
            ps += 1
        pulses[p] += ps

class FF(Mod):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)
        self.prev = False

    def pulse(self, i, p):
        if not p:
            self.prev = not self.prev
            ps = 0
            for o in self.outputs:
                if o in modules:
                    queue.put((modules[o], self, self.prev))
                ps += 1
            pulses[self.prev] += ps

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
        ps = 0
        for o in self.outputs:
            if o in modules:
                queue.put((modules[o], self, new_p))
            ps += 1
        pulses[new_p] += ps
    
filename = "input20"
# filename = "test201"
file = open(filename, 'r')
lines = file.readlines() #[l.split(" ") for l in file.readlines()]
file.close()


cons = []
all_mods = set()
for l in lines:
    split = l.strip().split(" ")
    outs = list(map(lambda s: s.strip(","), split[2:]))
    for o in outs:
        all_mods.add(o)
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
    all_mods.add(name)
    modules[name] = m

# Hook up inputs to cons
for m in modules:
    mod = modules[m]
    for o in mod.outputs:
        if o in cons:
            modules[o].add_input(mod)

for i in range(1000):
    queue.put((modules["broadcaster"], None, False))
    pulses[False] += 1

    while not queue.empty():
        m, i, p = queue.get()
        m.pulse(i, p)

print(pulses[True] *  pulses[False])
