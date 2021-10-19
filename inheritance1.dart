//single inheritance
class Triangle{  //base class
  void display(){
    print("This is the triangle :)");
  }
}
class Rectangle extends Triangle{ //derived class
  void display_rect(){
    print("This is the rectangle ");
  }
} 
void main(){
//creating object
Rectangle rect1=new Rectangle();
//calling methods
rect1.display();
rect1.display_rect(); 
}
