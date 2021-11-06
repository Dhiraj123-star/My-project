

public class multi8 extends Thread{

    public void run(){
        for(int i=0; i<=5;i++){

            try{
                Thread.sleep(400);
            }catch(Exception e){
                System.out.println(e);
            }
            System.out.println(i);
        }
    }
    public static void main(String[] args) {
        multi8 t1 = new multi8();

        multi8 t2 = new multi8();

        multi8 t3 = new multi8();

        t1.start();

        try{
            t1.join(1500); //join for long milliseconds
        }
        catch(Exception e){
            System.out.println(e);
        }

        t2.start();

        t3.start();

    }
    
}
