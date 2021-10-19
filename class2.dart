//decalaring class with its constructor
void main(){
  //creating object
  var tri1=new Triangle(12,45);  //calling constructor automatically 
  var rect1=new Rectangle(10,2); //calling constructor automatically 
}
//defining class triangle
class Triangle{
  
  Triangle(int a,int b){
    print("The area of the triangle is :${0.5*a*b}");

  }
}
//defining another class
class Rectangle{
  Rectangle(int a,int b){
    print("The area of the triangle is: ${a*b}");
  }
}