//exception handling with on--catch
main(List<String> args) {
  
  int a=10;
  int b=0;
  int res;
  try{
    res=a~/b;

  } on IntegerDivisionByZeroException catch(E){
    print(E);
  }
}