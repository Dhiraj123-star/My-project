//list and its methods
main(List<String> args) {
var  list= []; //for empty list
//adding elements into the list by add() method
list.add("julia");
list.add("Python");
print("List after add() method: $list");

//adding elements into the list by addAll() method
list.addAll(["C","C++","C#","Java"]);
print("List after addAll() method: $list");
//another list example
List mylist=[120,240,360,480];
mylist.insert(2, 100); //adding element at index 2
print("After inserting the element is: $mylist");
//using insertAll()
mylist.insertAll(1, [7,14,21,28]); //adding multiple elements at index 1
print("After multiple elements : ${mylist}");

}