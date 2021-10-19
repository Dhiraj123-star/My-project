//named constructor
main(List<String> args) {
  //creating constructor
  my_class myobj= my_class(); //for default constructor
  my_class myobj1=new my_class.namedConst("Dart Programming");
}
class my_class{
  //declaring constructor
  my_class(){
    print("This is default constructor");

  }
  //second constructor
  my_class.namedConst(String name){
    print("I am learning $name");
  }


}