import java.util.*;
public class temp
{
    public static void main(String args[])
    {
        String s = "111111111";
        int a[] = {7 , 3 , 1 , 3 , 1};
                StringBuilder str = new StringBuilder();
                str.append(s);
                //int len_bin = 0;
                for(int i = 0;i<a.length;i++)
                {
                    int len_bin = 0;
                    String binary = "";
                    binary = Integer.toBinaryString(a[i]);
                    //System.out.print(binary+" ");
                    len_bin = binary.length();
                    int start = str.indexOf(binary);
                    //System.out.print(start+" ");
                    System.out.println(str.length()+" ");
                    if(str.indexOf(binary)==-1)
                        System.out.println("fghj");
                    else
                    {
                        start = str.indexOf(binary);
                        len_bin = len_bin+start;
                        str.delete(start,len_bin);
                    }
                }
                
    }
}