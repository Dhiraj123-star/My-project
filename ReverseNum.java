import java.util.Scanner;
public class ReverseNum {
    public static void main(String[] args) {
        
    Scanner sc=new Scanner(System.in);

    int number ;

    System.out.println("Enter Your number: ");

    number=sc.nextInt();

    //creating object 

    ReverseNum obj=new ReverseNum();

    //calling the function

    System.out.println("The Reversed Number is: "+obj.Reverse_Num(number));

    //closing the scanner resource

    sc.close();



    }
    public int Reverse_Num(int num){
        int rev=0;

        while(num>0){
            int mynum= num%10;
            rev=rev*10+mynum;

            num=num/10;

        }
        return rev;
    }


    
}
