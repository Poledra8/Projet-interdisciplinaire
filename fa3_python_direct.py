import numpy as np
import struct


fs = 44100
note = 176
harmoniques = [
    {"note": "fa3", "h": note, "db": 100},
    {"note": "fa4", "h": note*2, "db": 25},
    {"note": "do5", "h": note*3, "db": 12},
    {"note": "fa5", "h": note*4, "db": 8},
    {"note": "la5", "h": note*5, "db": np.float64(2.4)},
    {"note": "do6", "h": note*6, "db": np.float64(2.05)},
    {"note": "mib6", "h": note*7, "db": np.float64(2.5)},
    {"note": "fa6", "h": note*8, "db": np.float64(1.2)},
    ]
   # {"note": "la6", "h": 172*10, "db": 20.5},
#    {"note": "si6", "h": 172*11, "db": 24.6},
 #   {"note": "do7", "h": 172*12, "db": 24.2},
  #  {"note": "reb7", "h": 172*13, "db": 18.6},
   # {"note": "mib7", "h": 172*14, "db": 25.3
sample = 44100
duration = 5
x = np.arange(sample*duration)
f = open("fa.wav", "wb")
for harmonique in harmoniques:
    f = open(harmonique["note"]+".wav", "wb")
    y = np.float64(harmonique["db"]*np.sin(np.pi * harmonique["h"] * x / fs))
    for i in y:
        f.write(struct.pack("b", int(i)))
f.close()
print("fichier cree")
