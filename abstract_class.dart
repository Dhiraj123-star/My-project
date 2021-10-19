//abstrct class in dart
abstract class Person{
  //declaring abstract method
  void display();

}
class boy extends Person{
  //overriding method
  void display(){
    print("I'm a boy :)");

  }
}
class girl extends Person{
  //overriding method
  void display(){
    print("i'm a girl :)");
  }
}
main(List<String> args) {
  
  girl g=new girl(); //creating object of girl
  g.display(); //invoking method of girl class

  boy b=new boy(); //creating object of boy

  b.display(); //invoking method of boy class 


}