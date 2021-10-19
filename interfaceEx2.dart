//another example of dart interface
class student{
  late String name;
  late int age; //late marks show it'll be initialise later 


void displayName(){
  print("I am ${name}");

}
void displayAge(){
  print("My age is ${age}");
}
}
class faculty {
  late String dept_name;
  late int salary;
  void displayDepartment(){
    print("The  Department is ${dept_name}");
  }
  void displaySalary(){
    print("The Salary is ${salary}");
  }
}
//defining interface by implementing another class
class college implements student,faculty{

  //overriding the student class members

  late String name; //late marks show it'll be initialise later 
  late int age;
  @override
  void displayName() {
    print("I'm ${name}");

}
@override
void displayAge(){
  print("My age is ${age}");
}
//overriding each data member of faculty class

late String dept_name;
late int salary;
void displayDepartment(){
  print("I am a professor of ${dept_name}");

}
void displaySalary(){
  print("My salary is ${salary}");
}

}
main(List<String> args) {
  college c1=new college();
  c1.name="HandsCobe";
  c1.age=22;
  c1.dept_name='Data Structure';
  c1.salary=90000;

  //calling methods
  c1.displayName();
  c1.displayAge();
  c1.displayDepartment();
  c1.displaySalary();




}

