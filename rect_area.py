def areaRectangle(length,breadth=1):
    area=length*breadth
    return area
def main():
    print("enter the following values for rectangle:")
    lengthRect=int(input('length:integer value'))
    breadthRect=int(input('breadth:integer value'))
    areaRect=areaRectangle(lengthRect,breadthRect)
    print('area of the rectangle is',areaRect)

if __name__=='main':
    main()
