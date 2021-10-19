#program for binary search in a list/array using recursion
def binary_search(list,low,high,val):
    if (high<low):
        return None
    else:
        midval=low+((high-low)//2)

#compare the search item with middle most value
        if list[midval]>val:
            return binary_search(list,low,midval-1,val)
        elif list[midval]<val:
            return binary_search(list,midval+1,high,val)
        else:
            return midval

list=[5,11,22,36,99,101]
print(binary_search(list,0,5,36))
print(binary_search(list,0,5,101))
