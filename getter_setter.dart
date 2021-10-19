//getter and setter example in dart
class student{
  late String student_name;//late marks show it'll be initialise later 

  late String branch;//late marks show it'll be initialise later 
  late int age;
//getter method
String get getName{
  return student_name;
}
void set std_name(String name){
  this.student_name=name;
}
void set set_age(int age){
  if (age<=18){
    print("Student should be greater than 20 :)");

  }
  else{
    this.age=age;
  }
}
int get Std_age{
  return age;
}
void set Stud_branch(String branch){
  this.branch=branch;

}
String get std_branch{
  return branch;
}
}
main(List<String> args) {
  student st=new student();
  //st.set_age=12; return null,because it is less than 18
  st.age=18;

  st.std_name="Dhiraj";
  st.Stud_branch ="Computer Science";
  
  print("The Name of the student is: ${st.getName}");

  print("The Age  of the student is :${st.Std_age}");

  print("The Branch of the student is: ${st.std_branch}");

  print("Thanks for using Dart Programming Language :)");




}