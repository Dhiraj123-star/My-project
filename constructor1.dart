//constructor example
import 'class1.dart';

void main(List<String> args) {
Student st=new Student("Dhiraj",12);

}
class Student{
  //declaring a constructor
  Student(String name,int id){
    print("the name of the student is: $name");
    print("the roll no of the student is: $id");


  }
}