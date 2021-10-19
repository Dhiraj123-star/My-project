//switch example in go
package main
import "fmt"

func main(){
	var value string="two"
	switch value{
	case "one":
		fmt.Println("this is the python language :)")
	case "two","three":
		fmt.Println("this is swift language :)")
	case "four","five":
		fmt.Println("this is go language :)")
	default:
		fmt.Print("You are unique , please try again ::)")
	}
}