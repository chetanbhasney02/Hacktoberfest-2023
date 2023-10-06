// Palindrome Checker in Rust Lang. ...
// Developer: Saksahm093 ...

use std::io;

fn clean_sentence(sentence: &str) -> String {
    // Remove punctuation and spaces...
    let cleaned: String = sentence.chars()
                                  .filter(|&c| !c.is_whitespace() && !c.is_ascii_punctuation())
                                  .collect();
    cleaned.to_lowercase()
}

fn check_palindrome(value: &str) {
    if value == value.chars().rev().collect::<String>() {
        println!("Your sentence is a palindrome.");
    } else {
        println!("Sentence is not a palindrome.");
    }
}

fn main() {
    println!("Enter sentence to check if palindrome: ");

    let mut sentence = String::new();
    io::stdin().read_line(&mut sentence).expect("Failed to read line");

    let cleaned_sentence = clean_sentence(&sentence);
    check_palindrome(&cleaned_sentence);
}
