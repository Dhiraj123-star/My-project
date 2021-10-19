//using the catch block 
main(List<String> args) {
  int x=100;
  int y=0;
  int res;
  try{
    res=x~/y;
  }
  //it returns the built-in exception related to the occurring exception
  catch(E){
    print(E);

  }
}