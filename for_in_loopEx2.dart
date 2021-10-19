//another example of for..in loop
main(List<String> args) {
  //list of numbers
  var num_list=[100,200,300,400];
  var sum=0; //initialise the sum with 0
  for(var i in num_list){
    sum+=i; //adding numbers of the list and assign into sum
  }
  print("The total sum is: $sum");
  
  print("Thanks for using Dart Programming Language :)");

}