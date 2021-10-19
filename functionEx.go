//function example in go
package main
import "fmt"

	type Employee struct{ //go structure
		fname string
		lname string

	}
	func (emp Employee )fullname(){ //function
		fmt.Println(emp.fname + " " +emp.lname)
	}
	
func main(){
	e1:=Employee{"Dhiraj","kumar"}
	e1.fullname()
}