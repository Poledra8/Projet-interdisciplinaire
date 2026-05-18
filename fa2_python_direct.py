import numpy as np
import struct


fs = 44100
note = 89
harmoniques = [
    {"note": "fa2", "h": note, "db": 12},
    {"note": "fa3", "h": note*2, "db": 40},
    {"note": "do4", "h": note*3, "db": 100},
    {"note": "fa4", "h": note*4, "db": 32},
    {"note": "la4", "h": note*5, "db": 70},
    {"note": "do5", "h": note*6, "db": 38},
    {"note": "mib5", "h": note*7, "db": 38},
    {"note": "fa5", "h": note*8, "db": 36},
    {"note": "sol5", "h": note*9, "db": 20},
    {"note": "la5", "h": note*10, "db": 23},
    {"note": "si5", "h": note*11, "db": 14},
    {"note": "do6", "h": note*12, "db": 10},
    {"note": "reb6", "h": note*13, "db": 15}
    ]
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
