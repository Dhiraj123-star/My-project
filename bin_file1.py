#program to read python dictionary contents back from the file
import pickle
f=open('bin_file.dat','rb')
dict1=pickle.load(f)
f.close()
print(dict1)
