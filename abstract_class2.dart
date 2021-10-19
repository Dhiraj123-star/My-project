//another example of dart abstract class
const pi=3.14 ; //declaring the value of pi 

abstract class FindArea{
  void displayArea(); //abstract method
}
class Rectangle extends FindArea{
  late int l; //late marks show it'll be initialise later 
  late int  b;

  void get_value(int l, int  b){
    this.l=l;
    this.b=b;

  }
  void displayArea(){
    print("The area of the rectangle is: ${this.l * this.b}");

  }
}
class circle extends FindArea{
  late int radius; //late marks show it'll be initialise later 
 void getmyside(int radius){
   this.radius=radius;

 } 
 void displayArea(){
   print("The area of the circle is: ${pi*this.radius*this.radius}");

 }

}
main(List<String> args) {
  Rectangle r1=new Rectangle(); //creating the object of class Rectangle
  r1.get_value(23, 3);
  r1.displayArea();
  //creating the object of class circle
  circle c1=new circle();
  c1.getmyside(10);
  c1.displayArea();

}