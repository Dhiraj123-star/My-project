//method overriding
class Human{
  //overriden method
  void run(){
    print("Human is running");
  }
}
class Man extends Human{
  void run(){
    super.run(); //calling parent class method
    print("Man is runnning :)");
  }

}
void main(List<String> args) {
  Man m=new Man();
  m.run(); 
}