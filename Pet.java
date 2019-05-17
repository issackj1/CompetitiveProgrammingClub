import java.util.ArrayList;
import java.util.Scanner;

public class Pet {
	
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		int winner = 0;
		int score = 0;
		int temp = 0;

		for (int i = 0; i < 5; i++) {
			temp = 0;
			for(int j = 0; j < 4; j++) {
				temp += in.nextInt();
			}
			if(temp > score) {
				score = temp;
				winner = i+1;
			}
		}
		
		System.out.print(winner + " " + score);
		
	}

}
