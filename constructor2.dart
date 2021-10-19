//parametrised constructor
main(List<String> args) {
  
  myclass m1=new myclass("Dart",1);
}
class myclass{
  myclass(String name,int rank){ //parametrised constructor

print("The language is: $name");
print("The rank is $rank");
  }
}