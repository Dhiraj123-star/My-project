//hierarchical inheritance example in  dart
//parent class
class Parent{
  void displayName(String name ){
    print("The name in Parent class : ${name}");
  }
}
class peter extends Parent{
  void age(int myage){
    print("The age is: ${myage}");
  }
}
class james extends Parent{
  void result(String result_1){
    print("The Result is : ${result_1}");
  }
}
void  main(){
  //creating object of james class
  james j1=new james();
  j1.result("Passed");
  j1.displayName("Dhiraj");
  //creating object of peter class
  peter p1=new peter();
  p1.age(22);
  p1.displayName("Pratham");

  print("Thanks for using Dart Programming language :)");
}