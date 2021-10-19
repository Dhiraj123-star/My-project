//another example of set
void main(List<String> args) {
  print("Example - Remove element in the given set");
  var prog_name=<String>{"C","C++","Java","Python"};
  print("Removing element from the set: ${prog_name}");
  prog_name.remove("Java");
  print("After removing element from the set: ${prog_name}");
  //iterating over the set
  print("Iterating through the set :");
  prog_name.forEach((element) {
    print(element);
    
  });
  //removing all the element from the set
  prog_name.clear();
  print("after clearing the element:${prog_name}");
  //another set
  var myset=<int>{12,45,56};
  print("my set is: ${myset}");
  List <int> mylist=myset.toList();  //typecasting the set into the list
  print("my list is: ${mylist}");

}