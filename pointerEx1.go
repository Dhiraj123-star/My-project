//pointer example in go
package main
import "fmt"
func main(){
	//taking normal variable
	var x int=12
	//declaration of pointer
	var p* int
	//initialisation of pointer
	p=&x;
	//displaying the result
	fmt.Println("The value of x is: ", x)
	fmt.Println("The value of address  of x is: ",&x)
	fmt.Println("The value of pointer is: ",p)
	fmt.Println("The value of pointer is: ",*p)
}