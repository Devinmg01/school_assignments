/*Devin Grace 04/06/23  
 * CS130 Lab assignment 3 part 2
 * 
 * This program will be using hash maps to take a geneaology file and search through the data within to return a chain of family
 * members going from 1st given ancestor to 2nd requested member then print that info to the screen secondly if given chain does not exist 
 * that will be printed to the screen.
 * 
 * 
 */

import java.io.*;
import java.util.*;

public class ReadingGeneFile {
	//empty hash map so we can store the family data in file using strings and lists
	private static Map<String, List<String>> geneTree = new HashMap<>();
	
	public static void main(String args[]) throws FileNotFoundException {
		// scan used for user input
		Scanner scan = new Scanner(System.in);
			
			//input file path here
			File file = new File("C:\\Users\\devin\\OneDrive\\Eclipse_workplace\\data.txt");
			Scanner fileScan = new Scanner(file);
			
			// the total number of people in the file stated in the top
			int N = fileScan.nextInt();
			fileScan.nextLine();
			
			// loop through each line of our file and begin making the family tree of given geneaology
			for (int i = 0; i< N; i++) {
				try {
				
				// makes string of current line scan is on
				String line = fileScan.nextLine();
				//splits line into an array 
				String[] splitLine = line.split(" ");
				
				//first part of array is name 
				String name = splitLine[0];
				//converts second part of string which is num of children current perosn has into integer
				int numChild = Integer.parseInt(splitLine[1]);
				
				// if the person actually has children make a list for them
				if (numChild > 0) {
					List<String> children = new ArrayList<>();
					
					// adds the children to the list
					for (int j = 2; j < splitLine.length; j++) {
						children.add(splitLine[j]);
					}
					// updates gene tree with key name and value children
					geneTree.put(name,  children);
					
				}
				else {
					geneTree.put(name,  new ArrayList<>());
				}
				}
				catch (NumberFormatException nfe) {
					
				}
			}
			//end for loop
			
			//Main Interface of code to ask user for family member and return the path
				System.out.print("Enter 1st family member and 2nd family memeber: ");
				String[] inFamMember = scan.nextLine().split(" ");
				
				String Member1 = inFamMember[0];
				String Member2 = inFamMember[1];
				
				// use getPath to find the chian of members from 1 to 2
				List<String> path = getPath(Member1,Member2);
				
				//if a path exists then print path if else state no path availible
				if (path != null) {
					System.out.println("Path: " + String.join(", ",path));
				}
				
				else {
					System.out.println(Member2 + " Is not a descendant of " + Member1);
				}
				
			
			
	scan.close();
	fileScan.close();		
	}
	//end main
	
	//recursive method used for finding paths along families requested X being member 1 and Y being member 2
	private static List<String> getPath(String X, String Y) {
		//if names inputed from user are not in gene tree return null and end
		if (!geneTree.containsKey(X) || !geneTree.containsKey(Y)) {
			return null;
		}
		
		//uses list interface called path to be an ArrayList to store the path we are making that the user requested in a resizable array
		List<String> path = new ArrayList<>();
		// adds member 1 to the path since it is orgin of path
		path.add(X);
		
		// retruns path if memebr 1 and memebr 2 are same person
		if (X.equals(Y)) {
			return path;
		}
		
		// retrieves the list of children for the member 1 aka orgin member
		List<String> children = geneTree.get(X);
		
		//uses for each loop to iterate through each child in children and recursivley call the get path function to search for our member 2
		for(String child: children) {
			List<String> childPath = getPath(child, Y);
			
			// when path is found add the child and thier path  to the current  path and return
			if (childPath != null) {
				path.addAll(childPath);
				return path;
			}
		}
		return null;
	}	
}
// end class