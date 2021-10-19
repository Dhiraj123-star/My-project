//struct example in go
package main
import "fmt"
type prog_detail struct{
	prog_name string
	rank int
	
}
func main(){
	x:=prog_detail{prog_name: "Python",rank:2};
	fmt.Println(x)
	fmt.Println(x.prog_name) //returns Python
	fmt.Println(x.rank)  //returns 2
}