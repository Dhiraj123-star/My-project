//iterating through the list elements

main(List<String> args) {
  List mylist=[100,321,553,33,5];
print("Iterating through the list without index: ");
mylist.forEach((element) {
  print(element);
});
List myAnotherList=[10,20,30,40,50,60];
print("Iterating through the list with index: ");
myAnotherList.forEach((element) {
  print("${myAnotherList.indexOf(element)}: $element");
});
print("Thanks for using Dart Programming language :)");

}