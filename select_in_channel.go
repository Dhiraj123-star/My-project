package main

import (
	"fmt"
	"time"
)

//function1


func  portal1(channel1 chan string){
	time.Sleep(3*time.Second)
	channel1<-"Welcome to the channel1 "
}
//function2
func portal2(channel2 chan string){
	time.Sleep(2*time.Second)
	channel2<-"welcome to channel2"
}
//main function

func main() {
	//creating channels
	C1:=make (chan string)
	C2 :=make(chan string)
	//calling function 1 and 
	//function 2 in gorountine
	go portal1(C1)
	go portal2(C2)

	select{
		//case 1 for portal 1
	case op1:= <-C1:
		fmt.Println(op1)
		//case 2 for portal 2

	case op2:= <- C2:
		fmt.Println(op2)
	}

	}

