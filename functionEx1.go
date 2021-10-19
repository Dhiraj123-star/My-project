//function example in go
package main
import "fmt"
func main(){
	//calling function
	fmt.Println("The area is: ",area(12,5))
}
//function definition
func area (a , b int)int{
	res:=a*b
	return res

}