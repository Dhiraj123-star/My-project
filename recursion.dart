//dart recursion example
int factorial(int n){
  if(n==1){return 1;}
  else{
    return n*factorial(n-1);
  }
}

main(List<String> args) {
  int fact= factorial(8);
  print("The factorial of 8 is :$fact");
  
}
