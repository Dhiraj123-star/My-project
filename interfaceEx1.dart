//Interface example in dart
class Employee{
  void display(){
    print("I'm working as an employee :)");
  }
}
//defining interface by implanting another class
class Engineer implements Employee{
  void display(){
    print("I'm working as an Engineer");
  }
}
main(List<String> args) {
  Engineer eng=new Engineer(); //creating object
  eng.display();  // calling method
  

}
