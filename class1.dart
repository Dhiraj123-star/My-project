//class exammple in dart
class Student{
  var studName;
  var studId;
  var StudClass;

//defining class function
showDetail(){
  print("student name is: ${studName}");
  print("Student class is: ${StudClass}");
  print("Student id is: ${studId}");
}
}
void main(){
//creating object
var std=new Student();
std.studId=101;
std.StudClass="BCA";
std.studName="Dhiraj";
//calling class method 
std.showDetail();


}
