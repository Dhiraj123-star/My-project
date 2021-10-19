//concurrency example in go
package main

import (
	"fmt"
	"time"
)

//go program to illustrate the concept of Go rountine
func display (str string){
	for w:=0; w<=5; w++{
		time.Sleep(5*time.Second)
		fmt.Println(str)
	}


}
func main(){
	//calling gorountine
	go display("Welcome")
	
	//calling normal function
	display("Go programming ")

}