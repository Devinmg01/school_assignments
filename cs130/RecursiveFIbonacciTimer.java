/*Devin Grace 01/30/23
CS130 - Lab assignment 1

This program will take a positive integer input then proceed to return the fibonacci sequence value at the given integer
The program also times itself while calling the fibonacci method and will display the timing along the following 6 terms from the given integer.


*/

import java.util.Scanner;





public class RecursiveFibonacciTimer {
	
	
	
	
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
				long start = System.currentTimeMillis();
				
				//print statement and calls method 
				System.out.println("The Fibonacci term at position " + Fib +" is " + FibTime(Fib));
				
				//second part of timer after calling method
				long end = System.currentTimeMillis();
				Fib++;
			
				//computes time and divides by 1000 to get seconds
				float timer = ((end - start)/ 1000F);
				System.out.println(" Computed in " + timer + " seconds");
			//end loop
			}
		}
		
	//end of main		
	}
	
	//recursive method to find a fibonacci term
	public static int FibTime(int targetTerm) {
		
		//This is the BASE CASE so our recursion algorithm knows when to stop calling itself
		if ((targetTerm == 0) || (targetTerm == 1)) {
			return targetTerm;
		}
		// RECURSION CASE the else statement to begin recursivly calling itself to return target Term
		else {
			return (FibTime(targetTerm - 1) + FibTime(targetTerm - 2));
		}
	//end of FibTime	
	}
	
	

//end of class
}
