//calculating the area of circle, rectangle,triangle,square

#include<stdio.h>

//function declaration or function prototype

double area_circle(double);
int area_tri(int,int);
int area_sq(int);
int area_rect(int,int);

const double PI=3.14;
int main(int argc, char const *argv[])
{ 
    int len,br, side, base,height;
    double radius;

    //read the dimensions of the rectangle
    printf("Enter the length of the rectangle : ");
    scanf("%d",&len);
    printf("Enter the breadth of the rectangle : ");
    scanf("%d",&br);

//read the dimensions of the square

printf("Enter the side of the square: ");
scanf("%d",&side);

//read the dimensions of the triangle 

printf("Enter the base of the triangle: ");
scanf("%d",&base);

printf("Enter the height of the triangle: ");
scanf ("%d",&height);

//read the dimension of circle
printf("Enter the radius of the circle: ");
scanf("%lf",&radius);

//calling the area of the rectangle
int recty = area_rect(len,br);

//calling the area of the square

int squary= area_sq(side);

//calling the area of the triangle

int triangy = area_tri(base,height);

//calling the area of the circle

double circy=area_circle(radius);

printf("\n"); //for new line


//printing the area of the rectangle 

printf("The area of the rectangle is:%d \n",recty);

//printing the area of the square 

printf("The area of the square is %d \n",squary);

//printing the area of the triangle 

printf("The area of the triangle is: %d \n",triangy);

//printing the area of the circle 

printf("The area of the circle is %lf \n",circy);

printf("\n"); //for new line

printf("Thanks for using C programming language :)");
    
    return 0;
}

//defining the function area_rect()
int area_rect(int len,int breadth){
    int result= len*breadth;
    return result;
}

//defining the function area_sq()

int area_sq(int side){
    int result=side*side;;
    return result;
}

//defining the function area_tri()

int area_tri(int base, int height){
    int result=0.5*base*height;
    return result;
}

//defining the function area_circle()

double area_circle(double radius){
    double result =PI*radius*radius;
    return result;
}
