//using super keyword with constructor
class Parent{
  Parent(){
    print("This is parent class constructor !!!");
  }
}
class Child extends Parent{
  Child():super(){ //calling super class constructor
  print("This is Child class constructor ");

  }
}
main(List<String> args) {
  

  //creating object of child class
  Child obj1=new Child();
  
}