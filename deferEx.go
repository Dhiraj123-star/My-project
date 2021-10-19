//defer example in go
package main
import "fmt"
//function
func multiply(num1,num2 int)int{
	res:=num1*num2
	fmt.Println("The result is: ",res)
	return 0
}
func show(){
	fmt.Println("Hello!!, Thanks for using Go Programming Language")
}
//main function
func main(){
	//calling multiply() , it behaves like a normal function
	multiply(12,5)
	//calling multiply(), using defer function
	defer multiply(12,6)
	//calling show function
	show()

}