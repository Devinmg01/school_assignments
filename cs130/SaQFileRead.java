/*Devin Grace 04/03/23  This program will read a file to determine if a file has balanced delimiters or not stating which of the two
 are present and printing the file if they are balanced. It does so by converting the file to string then passing it along to a method
 turning string into a character array and passing delimiters to a stack where it can push and pop as needed to ensure balanced delimiters are 
 present




*/
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Scanner;
import java.util.Stack;

public class SaQFileRead {

	public static void main(String[] args) throws IOException {
		
		
		//++++++++++++++++++++++++++++++++++++insert file path here+++++++++++++++++++++++++++ 
		String path = "C:\\Users\\devin\\OneDrive\\Eclipse_workplace\\CSC130\\src\\RecursiveFibonacciTimer.java";
		File file = new File(path);
		Scanner scan = new Scanner(file);
		
		String theFile = Files.readString(Paths.get(path));
		String fileLine = "";
		//determines if file is balanced if balanced print file and correct statement if not print error statement
		if (balacneCheck(theFile)) {
			while(scan.hasNextLine()) {
				fileLine = scan.nextLine();
				System.out.println(fileLine);
			}
			//end while
			System.out.println("++++++++++++++++++++++++++++");
			System.out.println("File Delimiters are Balanced");
			System.out.println("++++++++++++++++++++++++++++");
		}
		//end if
		else {
			System.out.println("++++++++++++++++++++++++++++++++");
			System.out.println("File Delimiters are Not Balanced");
			System.out.println("++++++++++++++++++++++++++++++++");
		}
		//end else
		
		
		scan.close();
		
				
	}
	// end of main
	
	//Method to check if brackets are balanced
	public static boolean balacneCheck(String file) {
		
		
		//Using Stack as a resize able array to push and pop delimiters
		Stack<Character> stack = new Stack<Character>();
		
		// loop to traverse file
		for (int i = 0;i < file.length(); i++) {
			char character = file.charAt(i);
			//System.out.print(character);
			// checks to see if current character is an opening delimeter
			if (character == '{' || character == '(' || character == '[' ) 
				// pushes given parenthesis into the stack
				stack.push(character);
			// checks to see if a closing delimeter comes before any opening ones also pops delimeters if matching 
			else if (character == '}' || character == ')' || character == ']') {
				//declares unbalanced if close delimeter appears before open
				if (stack.empty())
					return false;
				//pop for balanced deliemeter
				if (character == ')' && stack.peek() == '(')
					stack.pop();
				else if (character == '}' && stack.peek() == '{')
					stack.pop();
				else if (character == ']' && stack.peek() == '[')
					stack.pop();
				// declares unbalanced if no match
				else
					return false;
			}
			// end else if
				
			
			
		}
		//end for loop
		// balance if stack is clear unbalanced if stack has leftovers
		if (stack.empty())
			return true;
		else
			return false;
		
		
	}
	//end balance check
	
}
//end class
