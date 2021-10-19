//another map methods
void main(List<String> args) {
  Map student={"name":"Dhiraj","age":23};
  print("The map is: ${student}");
  student.addAll({"marks":345,"hobby":"coding"});
  print("map after adding :${student}");
  //remove method
  student.remove("age"); //removing the key age
  print("After removing the key: ${student}");
  //clear the map
  student.clear();
  print("After Clear :${student}");

}