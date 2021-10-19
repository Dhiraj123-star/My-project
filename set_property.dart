//some set property
void main(List<String> args) {
  var myset=<String>{"Julia","Elixir","Haskell","TypeScript"};
  //the first property
  print("the first element of the set is:${myset.first}"); //returns the first element of the set
  //last property
  print("The last element of the set is: ${myset.last}"); //returns the last element of the set
  //hascode property
  print("the hascode :${myset.hashCode}"); //get hash code for the corresponding object
  
}