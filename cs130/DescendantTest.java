import java.io.*;
import java.util.*;

public class DescendantTest {
    private static Map<String, List<String>> familyTree = new HashMap<>(); // create an empty HashMap to store the family tree

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // create a scanner to read user input

        try {
            File file = new File("C:\\Users\\devin\\OneDrive\\Eclipse_workplace\\data.txt"); // open the file containing the genealogy information
            Scanner fileScanner = new Scanner(file);

            int n = fileScanner.nextInt(); // read the number of people in the file
            fileScanner.nextLine(); // consume newline after integer

            // loop through each line in the file and construct the family tree
            for (int i = 0; i < n; i++) {
            	
                String line = fileScanner.nextLine();
                String[] splitLine = line.split(" ");
                

                String name = splitLine[0];
                
                int numChildren = Integer.parseInt(splitLine[1]);

                if (numChildren > 0) {
                    List<String> children = new ArrayList<>();

                    for (int j = 2; j < splitLine.length; j++) {
                        children.add(splitLine[j]);
                    }

                    familyTree.put(name, children);
                } else {
                    familyTree.put(name, new ArrayList<>());
                }
            
              
            }

            // loop indefinitely and prompt the user for pairs of names to check if Y is a descendant of X
            while (true) {
                System.out.print("Enter X and Y (separated by a space): ");
                String[] input = sc.nextLine().split(" ");

                String x = input[0];
                String y = input[1];

                List<String> path = getPath(x, y); // call the getPath method to find a path from X to Y

                // print the result of the path search
                if (path != null) {
                    System.out.println("Yes, " + y + " is a descendant of " + x + ".");
                    System.out.println("Path: " + String.join(" -> ", path));
                } else {
                    System.out.println("No, " + y + " is not a descendant of " + x + ".");
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + e.getMessage());
        }
          
    }

    // recursive method to find a path from X to Y in the family tree
    private static List<String> getPath(String x, String y) {
        if (!familyTree.containsKey(x) || !familyTree.containsKey(y)) { // if either name is not in the family tree, return null
            return null;
        }

        List<String> path = new ArrayList<>(); // create an empty list to store the path
        path.add(x); // add X to the path

        if (x.equals(y)) { // if X and Y are the same person, return the path with only X in it
            return path;
        }

        List<String> children = familyTree.get(x); // get the list of children for X

        // loop through each child and recursively call getPath on them to search for Y
        for (String child : children) {
            List<String> childPath = getPath(child, y);

            if (childPath != null) { // if a path is found, add the child's path to the current path and return it
                path.addAll(childPath);
                return path;
            }
        }

        return null;
    }
}