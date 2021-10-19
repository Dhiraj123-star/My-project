//multilevel inheritance in Dart
class Bird{  //this is the first class 
  void fly(){ 
    print("Bird is flying :)");
  }
}
class parrot extends Bird{  //second class inherites the first class
  void speak(){
    print("Parrot is speaking :)");
  }
}
class Eagle extends parrot{ //third class inherites the second class 
  void fly1(){
    print("Eagle is flying :)");
  }
}
void main(){
  //creating object
  Eagle e1=new Eagle();
  e1.fly();
  e1.speak();
  e1.fly1();
}