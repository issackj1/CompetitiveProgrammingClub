import java.util.Scanner;

public class Trik {
	
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		String moves = in.nextLine();
		int position = 1;

		for (int i = 0; i < moves.length(); i++) {
			if(moves.charAt(i) == 'A' && position == 1) {
				position = 2;
				
			}else if(moves.charAt(i) == 'A' && position == 2) {
				position = 1;
			}
			else if(moves.charAt(i) == 'B' && position == 2) {
				position = 3;
			}
			else if(moves.charAt(i) == 'B' && position == 3) {
				position = 2;
			}else if(moves.charAt(i) == 'C' && position == 1) {
				position = 3;
			}else if(moves.charAt(i) == 'C' && position == 3) {
				position = 1;
			}else {
				
			}

		}
		
		System.out.print(position);
		
	}

}
