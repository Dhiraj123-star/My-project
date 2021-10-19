package main
import "fmt"
func main(){
	var fname string
	fmt.Println("Enter your name: ")
	fmt.Scan(&fname)
	var age int
	fmt.Println("Enter Your age: ")
	fmt.Scan(&age)
	fmt.Println("Your name is :"+fname)
	fmt.Println(age)
}