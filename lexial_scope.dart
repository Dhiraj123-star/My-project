//lexial scope example in dart
main(List<String> args) {
  initial1(){
    var name = "Dart is fantabulous programming language";

    void disp_name(){
      print(name);
    }
    disp_name();

  }
  initial1();
 
}
