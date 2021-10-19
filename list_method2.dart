//another program for list and its method
main(List<String> args) {
  //list  declaration
  var list1=[100,200,300,400,500];
  print("before updating the list is: $list1");

  //update the element in the list at index 2
  list1[2]=0 ; 
  print("After updating the list is: $list1");

  //using replacerange()method
  list1.replaceRange(1, 3,[1,2,4,100]);
  print("After using replaceRange(): ${list1}");

  //another list of programming languages
  List strlst=["Java","JavaScript","TypeScript","Go","Dart"] ; 
  //using remove method
  strlst.remove("Go"); //remove Go from the list

  print("After removing the element: ${strlst}");

  //using removeAt()method
  strlst.removeAt(2); //remove element at index 2

  print("After removing element at index 2 : ${strlst} ");
  //using removeLast() method

  strlst.removeLast();//remove the last item from the list

  print("after removing the last element from the list : ${strlst}");

  //using removeRange() method

  //list of numbers
  List mynumList=[100,120,140,160,340];

  print("the number list is: ${mynumList}");

mynumList.removeRange(1, 3); //remove the elements from range 1 to 3 but excluding index 3

print("After removing from index 1 to 3 is: ${mynumList}");






}