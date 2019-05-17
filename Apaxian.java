import java.util.Scanner;

public class Apaxian {

	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		String other = in.nextLine();
		String result = "";
		int pointer = 0;
		char prev = ' ';

		int i = 1;
		result += other.charAt(0);
		while (i != other.length()) {
			prev = other.charAt(i-1);
			if (other.charAt(i) == prev) {
				i++;
			}else {
				result += other.charAt(i);
				i++;
			}
		}

		System.out.print(result);

	}

}
