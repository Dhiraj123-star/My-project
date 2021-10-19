package main
import "fmt"
type prog interface
{
	print()
}
func foo(p prog){
	fmt.Println(p)
}
type me struct{
	name string
	age int64
}
func (m me)print(){
	fmt.Println("Displaying :)")
}
func main(){
	m1:=me{"Dhiraj",22}
	m1.print()
	foo(m1)
	fmt.Println("Thanks for using Go :)")

	
}