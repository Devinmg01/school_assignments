/* Devin Grace
 * CS130 Lab Assignment 2	
 * 02/20/23
 * 
 * This program will take an array and use a linear search algorithm,  a binary search algorithm and a selection sort algorithm 
 * keeping track of the number of comparisons it makes subsequently giving a description of Big Oh for each algorithm
 * 
 */



public class SearchingAndSorting {

	public static void main(String args [] ) {
		
		// Array that will be searched and sorted consisting of 25 integers
		int myArray[] = {10, 2, 8, 15, 12, 20, 28, 66, 5, 3, 99, 17, 16 
						 ,6, 47, 76, 45, 32, 11, 21, 55, 69, 13, 18, 23};
		int sortedArray[];
		
		
		//call linear search method	for unsorted array			
		LinearSearch(myArray, 10);
		System.out.println("");
		//call sort method 
		sortedArray = sort(myArray);
		System.out.println("");
		//Linear search method on sorted array
		LinearSearch(sortedArray, 10);
		System.out.println("");
		//call binary search method
		BinarySearch(sortedArray, 15);
		
			
		  
    }
	//end main
	
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	// method for Linear search
	public static int LinearSearch(int arr[], int want) {
		int aLength = arr.length;
		
		//for loop to go through array one element at a time 
		for (int pointer = 0; pointer < aLength; pointer++) {
			
			//statement to see if wanted variable is found
			if (arr[pointer] == want) {
				
				// Check if big O is best case 
				if(pointer == 0) {

					System.out.println("==================Linear search======================== ");
					System.out.println("Comparisons needed: " + (pointer + 1));
					System.out.println("Wanted Value present at index: " + pointer);
					System.out.println("Best case therefore Time complexity = O(1)");
					return pointer;
				}
				
				// for linear search pointer is what we are looking for and # of comparisons taken
				System.out.println("==================Linear search======================= ");
				System.out.println("Comparisons needed: " + (pointer + 1));
				System.out.println("Wanted Value present at index: " + pointer);
				System.out.println("Not best case therefore time complexity = O(N)");
				return pointer;
				
			}
			
		}
		//end loop
		//flag
		return -1;	
	}
	//end Linear search
	
	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	
	//Recursive method for Binary search
	public static int BinarySearch(int arr[], int want) {
		
		
		// sets our low value to first element of array and high to array length
		int low = 0, high = arr.length -1;
		// counter tracks how many comparisons are needed to find the wanted value
		int counter = 0;
		
		//while loop to ensure array is valid then sets our mid variable
		while (low <= high) {
			int mid = low + (high - low) / 2;
			counter++;
			
			//auto return mid value if it is what we want
			if (arr[mid] == want) {
				System.out.println("==================Binary search========================");
				System.out.println("Comparisons needed: " + counter);
				System.out.println("Watned value is present at index: " + mid);
				System.out.println("Time complexity of big O = O(log n) because we are dividing the array in the loop");
				return mid;
			}
			//makes the new low the one element to the right if wanted value is located on the right half of mid
			if (arr[mid] < want) {
				low = mid + 1;
			
			}
			
			// makes the new high one element to the left if wanted value is located on the left half of mid
			else 
				high = mid - 1;
				
				
			
		}
		//end while loop
		
		// flag if in valid array or non present element
		return -1;
		
	}
	//end Binary search
	
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	
	// Selection sort method
	public static int[] sort(int arr[]) {
	
		 
		int size = arr.length;
		  
        // for loop goes through array one at a time moving until hitting biggest element
        for (int pointer = 0; pointer < size-1; pointer++)
        {
            // checker is one element ahead being compared to pointer to find min
			// if a min is found minVal equals new min
            int minVal = pointer;
            for (int checker = pointer + 1; checker < size; checker++)
                if (arr[checker] < arr[minVal])
                    minVal = checker;
  
            //holds a temp value to swap min value with first element
            int temp = arr[minVal];
            arr[minVal] = arr[pointer];
            arr[pointer] = temp;
        }
        //end loop
    
        System.out.println("==================Selection sort======================= ");
		for(int i = 0; i < arr.length;i++) 
			System.out.print(arr[i]+", ");
		
		System.out.println();
		System.out.println("Time complexity = O(n^2) due to a nested for loop making it not as efficent on bigger lists");
		return arr;
		
		
	  
	}
	//end sort
	
	///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
}
//end class
