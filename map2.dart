//another example of dart map
void main(){
  var prog=new Map();
  prog[1]="Julia";
  prog[2]="Scala";
  prog[3]="Python";
  prog[4]="C#";
  prog[5]="Elixir";
  print("The map is :${prog}");
  //printing all the keys
  print("All the keys are: ${prog.keys}");
  //printing all the values 
  print("All the values are: ${prog.values}");
  //length of the map
  print("the length of the map is: ${prog.length}");
  //isEmpty function
  print(prog.isEmpty); //returns false
  //isNotEmpty function
  print(prog.isNotEmpty); //returns true

  print("Thanks for using Dart Programming Language :)");
}