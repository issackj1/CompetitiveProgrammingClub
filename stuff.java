import java.util.Scanner;

public class stuff {


  public static void main(String args[]){

    countJars();

  }

  public static void countJars(){

    Scanner in = new Scanner(System.in);
    int sweet = in.nextInt();
    int sour = in.nextInt();

    while(sour != 0 || sweet != 0){

      if(sour == 0 && sweet == 0){
        return;
      }

      if(sweet + sour == 13){
        System.out.println("Never speak again.");
      }
      else if(sour > sweet){
        System.out.println("Left beehind.");
      }
      else if( sweet > sour){
        System.out.println("To the convention.");
      }
      else if(sweet == sour){
        System.out.println("Undecided.");
      }

      sweet = in.nextInt();
      sour = in.nextInt();


    }
    return;

  }

}
