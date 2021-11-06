import java.util.Arrays;
import java.util.List;
public class string_conv2 {
    public static void main(String[] args) {
        
        //array of strings

        String [] prog_name ={"Python","Java","C++","C","JavaScript"};

        String joined_str = String.join(" ", prog_name);

        System.out.println(joined_str);

        //another way of converting array into string

        CharSequence[]myarray={"h","e","l","l","o"};

        String joined_str2 = String.join(",", myarray);

        System.out.println(joined_str2);


        //another way of converting array into string using list
        

        
        List<String> mystrlist = Arrays.asList("code","with","me");

        String joined_str3=String.join("--",mystrlist);

        System.out.println(joined_str3);


    }
}
