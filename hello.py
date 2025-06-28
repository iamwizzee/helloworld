import os

dir = "/home/"

a = 1
for file in os.listdir(dir):
    print(a ,file)
    a = a+1