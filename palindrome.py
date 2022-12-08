def is_palindrome(s: str) -> bool:
    s = "".join(character for character in s.lower() if character.isalnum())
    return s == s[::-1]


if __name__ == "__main__":
    s = input("Please enter a string to see if it is a palindrome\n ")
    if is_palindrome(s):
        print(f"'{s}' is a palindrome.")
    else:
        print(f"'{s}' is not a palindrome.")