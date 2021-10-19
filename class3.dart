//another example of class constructor

void main(){
  //creating object
  MyClass st=new MyClass(); //object for default constructor
  MyClass st2=new MyClass.namedConst("Computer Science");

}
//defining class
class MyClass{
  //declaring constructor
  MyClass(){
    print("this is default Constructor");

  }
  MyClass.namedConst(String course){
    print("The branch is: ${course}");
  }
}