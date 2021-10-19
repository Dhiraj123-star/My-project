//slice example
package main
import "fmt"
func main(){
	//creating Array
	arr:=[5]string{"Java","JavaScript","Go","C","C++"}	
	//displaying array
	fmt.Println("the array is: ",arr)

	//creating slice
	myslice:=arr[1:4]
	//displaying slice
	fmt.Println("the slice is: ",myslice)
	//displaying the length of the slice
	fmt.Println("the length of the slice is:",len(myslice))
	//length capacity of the slice

	fmt.Println("The length of the slice is : ",cap(myslice))
}