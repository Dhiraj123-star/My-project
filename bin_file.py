#program to write dictionary to a binary file
import pickle
dict1={'python':90,'java':95,'c++':85}
f=open('bin_file.dat','wb')
pickle.dump(dict1,f)
f.close()
