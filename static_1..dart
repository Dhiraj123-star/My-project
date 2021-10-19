//static method
class Student{
   static late String stdBranch;//declaring static variable

  late String stdname;
  late int roll_num;

  show_info(){
    print("Student name is: ${stdname}");
    print("Student roll no is: ${roll_num}");
    print("Branch of the student is: ${stdBranch}");

  }


}
main(List<String> args) {
  
  Student std1=new Student();
  Student std2= new Student();

  //assigning value of static variable using class name
  Student.stdBranch="Computer Science";

  std1.stdname="Ramesh";
  std1.roll_num=120;
  std1.show_info();

print("\n"); //for new line 

  std2.stdname="Rahul";
  std2.roll_num=100;
  std2.show_info();
}