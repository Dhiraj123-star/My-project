//dart runes for special symbol
main(List<String> args) {
  var heart_rune ='\u2665';
  var theta_rune ="\u0398";
  var  smile_face="\u{1f600}";
  print(heart_rune);
  print(theta_rune);
  print(smile_face);

  //string.codeUnitAt() method
  String str="Dart Programming";
  print("Learning Dart :)");
  print(str.codeUnitAt(1));//returns the unicode for 'D'
  print(str.codeUnits); //returns the unicode-16 code units 
  //in the list

  //string.runes property
  "Dart Programming Language".runes.forEach((int rune) {
    var character=new String.fromCharCode(rune);
    print(character); //it iterates the given string through 
    //UTF-16 CODE UNIT
   });




}