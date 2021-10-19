//throwing an exception in dart
main(List<String> args) {
  try{
    check_marks(-10);

  }catch(e){
    print("the marks cannot be negative :(");
  }
}
void check_marks(int marks){
  if(marks<0){
    throw new FormatException(); //raising explanation externally
  }
}
