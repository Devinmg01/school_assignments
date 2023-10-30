import java.util.Scanner;





public class dynamicFibonacciTimer {
	
	
	
	
	public static void main(String args[] ) {
		
		// Scans for integer and store into Fib to get starting argument
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter a positive integer: ");
		int Fib = scan.nextInt();
		scan.close();
		
		//if else case to ensure positive integer
		if (Fib < 0) {
			System.out.println("Please enter a positive integer.");
		}
		else {
			
			// loop to display the following 6 terms in sequence
			for (int j = 1; j <= 6; j++) {
				
				//1st part of timer before calling method 
				long start = System.nanoTime();
				
				//print statement and calls method 
				System.out.println("The Fibonacci term at position " + Fib +" is " + FibTime(Fib));
				
				//second part of timer after calling method
				long end = System.nanoTime();
				Fib++;
			
				//computes time and divides by 1000 to get seconds
				float timer = ((end - start));
				System.out.println(" Computed in " + timer + " nanoseconds");
			//end loop
			}
		}
		
	//end of main		
	}
	
	
	
	//method where Fibonacci sequence takes place using arrays (Fastest)
	public static int FibTime(int startTerm) {
		//create array with extra spaces to handle case of 0 and 1
		int arr[] = new int[startTerm + 2];
		arr[0] = 0;
		arr[1] = 1;
		
		//main for loop to go through fibonacci sequence adding the two prior terms to get the next term in loop
		for (int i = 2; i <= startTerm; i++) {
			arr[i] = arr[i-1] + arr[i-2];
		}
		return arr[startTerm];
		
		
	//end of FibTime	
	}
	

//end of class
}
