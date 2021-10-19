#program to implement standard streams
import sys
f1=open(r"test.txt")
line1=f1.readline()
line2=f1.readline()
line3=f1.readline()
sys.stdout.write(line1)
sys.stdout.write(line2)
sys.stdout.write(line3)
