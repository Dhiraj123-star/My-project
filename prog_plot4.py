#program to plot frequency of marks using line chart

import matplotlib.pyplot as plt

def fnplot(list1):
    plt.plot(list1)
    plt.title("marks line chart")
    plt.xlabel("value")
    plt.ylabel("frequency")
    plt.show()


list1=[50,50,50,65,65,75,75,80,80,90,90,90]
fnplot(list1)
