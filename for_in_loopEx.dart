//for in  loop example
main(List<String> args) {
  //list of numbers
  var num_list=[12,34,55,67,77,90];
  //iterate through the list
  print("Iterating through num list :) ");
  for (var i in num_list){
    print(i);
    
  }
  //list of programming languages
  var prog_list=["Java","Python","JavaScript","TypeScript"];
  print("Iterating through the programming list :)");
  //iterate through the list
  for (var me in prog_list){
    print(me);
  }

}