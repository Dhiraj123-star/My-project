//enumeration example in dart
enum programming_lang{ //list of programming languages
  Python,
  JavaScript,
  Java,
  TypeScript,
  Ruby,
  Perl,
  C,
  Html,
  CSS,

}
main(List<String> args) {
  //access the values of enumaration
  print("Enumeration Example in Dart :)");
  print("\n"); //for new line
  print(programming_lang.values);
  //iterate through the enumeration

  programming_lang.values.forEach((v)=> /*print each values
   with its indices */
   print("value:$v,index :${v.index}"));


}