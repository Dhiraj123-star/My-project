//string and its methods
main(List<String> args) {
  //string example
  String str1= "DART PROGRAMMING";

  //change into the lower case
  print("The lowercase is :${str1.toLowerCase()}");

  String str2= "dhiraj dart programmer";

  //change into the uppercase

  print("The uppercase is: ${str2.toUpperCase()}");

  String  str3="" ; //empty string

  //check if string is empty 

  print("The string 3 is empty ?? ${str3.isEmpty}");//returns true
  print("The string 2 is empty ?? ${str2.isEmpty}"); //returns false

  //check if string not empty
  print("The string 3 is not empty ?? ${str3.isNotEmpty}"); //returns false
  print("The string 2 is not empty ?? ${str2.isNotEmpty}");//returns true

  //find the length of the string

  print("The length of the first string is: ${str1.length}"); //returns 16

  //trim method

  String str4 = "  Dhiraj  ";
  print("Before Trim: ${str4}");

  print("After trimed: ${str4.trim()}");

  String str5 ="Dhiraj";
  String str6 ="Dhiraj";

  //compare method
  print("Comparing string 5 and 6: ${str5.compareTo(str6)}");/*returns 0
  if true and equal  */

/* returns 1 if first string is greater */
  print("Comparing string 3 and string 4 :${str4.compareTo(str3)}");


/* returns -1 if first string is smaller */
  print("Comparing string 3 and string 4 :${str3.compareTo(str4)}");

  


}