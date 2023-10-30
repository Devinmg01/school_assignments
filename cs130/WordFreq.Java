/*Devin Grace 05/09/23
 * The main goal of this program is to accept a file of text. Use a hash map to go through a file and assign keys and value pairs to hash map of the word
 * and number times that word appears. then print all that info in two columns displaying word and repition number.
 * 
 * 
 * 
 */

import java.io.File;
import java.util.*;
import java.io.FileNotFoundException; 

public class WordFreq {

	
	
	// main driving method
	public static void main(String Args[]) throws FileNotFoundException {
		
		WordFreq main = new WordFreq();
		// enter file PATH name here
		main.WordCounter("C:\\Users\\devin\\OneDrive\\Eclipse_workplace\\UrgentMessage.txt");
		
	}// end main
	
	// method used in main to gather words and number of words with parameter of users file name
	public void WordCounter(String filename) throws FileNotFoundException {
		
		// scanner to pull file name from method call
		Scanner file = new Scanner(new File(filename));
		//Make a hash map to store all words in the file with key value being the word and value being mapped is the amount of times said word appears
		Map<String,Integer> wordList = new HashMap<String,Integer>();
		
		// while loop to go through whole file word by word
		while (file.hasNext()) {
			//assigns current word to variable 
			String word = file.next();
			// gets the amount of times said word has appeared and assigns it to count
			Integer count = wordList.get(word);
			
			//if else statement to determine if first time seeing word or not
			if (count != null)
				count++;
			else 
				count = 1;
			//uses put to insert key and value pair into our hashmap wordlist
			wordList.put(word,count);
		}
		file.close();
		
		//Use a Sorted set to help align words in alphabetical order
		//Tree set uses the set of keys from wordList as the type of elements maintained by this set
		SortedSet<String> set = new TreeSet<>(wordList.keySet());
		//for loop to go through set and print 
		for(String curr:set) {
			System.out.println(curr +" "+wordList.get(curr));
		}//end for loop
		
	}// end WordCounter
	
	
}
