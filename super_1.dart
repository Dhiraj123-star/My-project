//super keyword example in Dart

class car{  //base class  

  int speed =200;

  void display(){
    print("This is base class method");
    print("the speed of car is: $speed");
  }

}
//sub class 
class Bike extends car{
  int speed=120;

  void display()
  {
    print("This is derived class method");
    print("The speed of bike is: $speed");

  }
  void message(){
    display();
    super.display();
  }
}
main(List<String> args) {
  
  //creating object
  Bike b1=new Bike();

  b1.message(); //calling method 
}
