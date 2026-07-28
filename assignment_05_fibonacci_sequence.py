# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_fibonacci_terms(n):
    """Print the first n terms of the Fibonacci sequence."""
    if n <= 0:
        print("Error: Please enter a positive integer.")
        return
    
    fib_sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    
    print("Fibonacci sequence:", " ".join(map(str, fib_sequence)))


def is_fibonacci_number(num):
    """Check if a number belongs to the Fibonacci sequence."""
    if num < 0:
        return False
    
    a, b = 0, 1
    
    while a < num:
        a, b = b, a + b
    
    return a == num


def check_fibonacci_number(num):
    """Check and print whether a number is a Fibonacci number."""
    if is_fibonacci_number(num):
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")


def main():
    """Main function to run the Fibonacci program."""
    while True:
        print("\n" + "="*40)
        print("FIBONACCI SEQUENCE")
        print("="*40)
        print("1. Print first N terms")
        print("2. Check if a number is a Fibonacci number")
        print("3. Quit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            try:
                n = int(input("How many terms? "))
                print_fibonacci_terms(n)
            except ValueError:
                print("Error: Please enter a valid integer.")
        
        elif choice == "2":
            try:
                num = int(input("Enter a number to check: "))
                check_fibonacci_number(num)
            except ValueError:
                print("Error: Please enter a valid integer.")
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1-3.")


if __name__ == "__main__":
    main()


