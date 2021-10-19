//another example of go concurrency
package main

import (
	"fmt"	
	//"time"
)

func display(str string){
	for w:=0;w<=5; w++{
		//time.Sleep(1*time.Second ) wait for 1 second 
		fmt.Println(str)
	}
}
func main(){
	go display("Welcome") //go rountine 
	display("Go Programming ") //normal function 
}