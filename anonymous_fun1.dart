//anonymous function in dart
main(List<String> args) {
  var list=["Python","Java","JavaScript","Scala"];

  print("Example of anonymous function");

  list.forEach((item) {
    print("${list.indexOf(item)} $item");
    
  });


}