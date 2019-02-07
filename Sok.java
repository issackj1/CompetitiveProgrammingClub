import java.util.Scanner;
import java.lang.Math;

public class Sok {


  public static void main(String args[]){

    countJars();

  }

  public static void countJars(){

    Scanner in = new Scanner(System.in);
    double oJ = in.nextInt();
    double aJ = in.nextInt();
    double pJ = in.nextInt();

    double ratioOJ = in.nextInt();
    double ratioAJ = in.nextInt();
    double ratioPJ = in.nextInt();

    double numOJ = oJ / ratioOJ;
    double numAJ = aJ / ratioAJ;
    double numPJ = pJ / ratioPJ;

    if(numOJ < numAJ && numOJ < numPJ){

      System.out.print("0.000000 ");
      System.out.print(aJ - (ratioAJ * numOJ) + " ");
      System.out.print(pJ - (ratioPJ * numOJ));
    }
    else if(numAJ < numOJ && numAJ < numPJ){

      System.out.print((oJ - (ratioOJ * numAJ)) + " ");
      System.out.print("0.000000 ");
      System.out.print(pJ - (ratioPJ * numAJ));
    }else if(numPJ < numOJ && numPJ < numAJ){
      System.out.print((oJ - ratioOJ * numPJ) + " ");
      System.out.print((aJ - ratioAJ * numPJ)  + " ");
      System.out.print("0.000000");
    }else if(numOJ == numAJ && numOJ == numPJ){
      System.out.print("0.000000 ");
      System.out.print("0.000000 ");
      System.out.print("0.000000");
    }

  }

}
