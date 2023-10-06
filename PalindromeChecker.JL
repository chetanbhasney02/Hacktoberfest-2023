# Palindrome Checker in Julia Lang. ...
# Developer: Saksahm093 ...

function clean_sentence(sentence::String)::String
    # Remove punctuation, spaces, and convert to lowercase...
    cleaned = filter(x -> isascii(x) && isletter(x), lowercase(sentence))
    return cleaned
end

function check_palindrome(value::String)
    if value == reverse(value)
        println("Your sentence is a palindrome.")
    else
        println("Sentence is not a palindrome.")
    end
end

function main()
    println("Enter sentence to check if palindrome: ")
    sentence = readline()
    cleaned_sentence = clean_sentence(sentence)
    check_palindrome(cleaned_sentence)
end

main()
