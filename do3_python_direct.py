import numpy as np
import struct


fs = 44100
note = 132
harmoniques = [
    {"note": "do3", "h": note, "db": 80},
    {"note": "do4", "h": note*2, "db": 80},
    {"note": "sol4", "h": note*3, "db": 20},
    {"note": "do5", "h": note*4, "db": 10},
    {"note": "mi5", "h": note*5, "db": 10},
    {"note": "sol5", "h": note*6, "db": 4},
    {"note": "sib5", "h": note*7, "db": np.float64(4.4)},
    {"note": "do6", "h": note*8, "db": np.float64(1.6)},
    {"note": "re6", "h": note*9, "db": np.float64(4.5)}
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
