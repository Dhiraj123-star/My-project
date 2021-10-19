//exception handling in dart
main(List<String> args) {
  int x=10;
  int y=0;
  int res;
  try{
    res=x~/y;  //throw error

  }
    on IntegerDivisionByZeroException{
      print("cannot divide by zero :)");
    }

    }
  
