#program to write list sequence in a binary file
def foperation():
    import pickle
    list1=[10,20,40,50]
    f=open('list.dat','wb')
    pickle.dump(list1,f)
    print("file added to binary file")
    f.close()

foperation()
