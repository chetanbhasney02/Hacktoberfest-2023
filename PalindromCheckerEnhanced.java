import java.util.Scanner;

public class PalindromCheckerEnhanced {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Loop to continuously prompt the user for input until they decide to exit.
        while (true) {
            System.out.print("Enter a word or phrase (or 'exit' to stop): ");
            String input = scanner.nextLine();
            
            // Check if the user wants to exit the program.
            if ("exit".equalsIgnoreCase(input)) {
                break;
            }

            // Check if the provided string is a palindrome.
            if (isPalindrome(input)) {
                System.out.println("Yes, it's a palindrome!");
            } else {
                System.out.println("No, it's not a palindrome.");
            }
        }
        
        System.out.println("Thanks for using the palindrome checker!");
        scanner.close();
    }

    /**
     * Check if a string is a palindrome. A palindrome reads the same forwards and backwards.
     *
     * @param str the string to check.
     * @return true if the string is a palindrome, false otherwise.
     */
    static boolean isPalindrome(String str) {
        // Clean the string by removing unwanted characters and converting to lowercase.
        str = cleanString(str);
        int left = 0;
        int right = str.length() - 1;

        // Loop to compare the characters of the string from the outside in.
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
    
    /**
     * Clean the string by removing non-alphanumeric characters and converting to lowercase.
     *
     * @param str the string to clean.
     * @return the cleaned string.
     */
    static String cleanString(String str) {
        return str.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
    }

}
