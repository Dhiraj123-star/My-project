//dart set example
void main(List<String> args) {
  print("initialising the set :");
  var names=<String>{"Dhiraj","Yasweer","Rahul"};
  print("the Set is: ${names}");
  //using add method
  var top_name=<String>{};  //declaring empty set

  top_name.add("Pratham") ; //adding single value in the set by add()
  print("After adding single value: ${top_name}");

  //adding multiple elements
  top_name.addAll(names); //adding multiple values in the set by addAll()
  print("After adding multiple value: ${top_name}");
 //access the set elements
 var x=top_name.elementAt(3); //access the element at index 3
 print(x);
//finding element in the set
if (top_name.contains("Pratham")){
  print("element found :)");
}else{
  print("Element not found :(");
}

}