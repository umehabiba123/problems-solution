f = open('firstprogram.py','w')
f.write("hellow how are you ...........?")
f.close()

f = open('firstprogram.py','r')
text = f.read()
print(text)
f.close()
import os
for i in range(5):
    os.mkdir(f"PYTHONPROGRAMMING/day{i+1}")

