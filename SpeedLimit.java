import java.util.Scanner;

public class SpeedLimit {
	
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		int count = in.nextInt();
		int total = 0;
		int mph = 0;
		int time = 0;
		int prev = 0;
		
		while(count != -1) {
			total  =  0;
			prev = 0;
			for (int i = 0; i < count; i++) {
				mph = in.nextInt();
				time = in.nextInt();
				total += mph * (time - prev);
				prev = time;
			}
			System.out.println(total + " miles");
			count = in.nextInt();
		}
		
	}

}
