import java.util.Scanner;

public class PalindromeChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a word or phrase: ");
        String input = scanner.nextLine();
        
        if (isPalindrome(input)) {
            System.out.println("Yes, it's a palindrome!");
        } else {
            System.out.println("No, it's not a palindrome.");
        }
        
        scanner.close();
    }

    static boolean isPalindrome(String str) {
        str = str.replaceAll("[^a-zA-Z]", "").toLowerCase(); // Remove non-alphabetic characters and convert to lowercase
        int left = 0;
        int right = str.length() - 1;

        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
