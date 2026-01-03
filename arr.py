import os
import sys

def parse(s):
    """Convert a string of numbers separated by spaces or commas into a list of floats."""
    nums = []
    for x in s.replace(",", " ").split():
        try:
            nums.append(float(x))
        except ValueError:
            print(f"Warning: skipping non-numeric token: {x}")
    return nums

def read_scores():
    """Read scores from command-line arguments, environment variable, file, or user input."""
    if len(sys.argv) > 1:
        return parse(" ".join(sys.argv[1:]))

    scores_env = os.getenv("SCORES")
    if scores_env:
        return parse(scores_env)

    if os.path.isfile("scores.txt"):
        with open("scores.txt", "r") as f:
            return parse(f.read().strip())

    try:
        user_input = input("Enter scores separated by spaces or commas: ")
        return parse(user_input)
    except EOFError:
        return []

def main():
    """Main function to process and display score statistics."""
    scores = read_scores()
    if not scores:
        print("No valid scores provided.")
        sys.exit(1)

    print("=== main/master branch output ===")
    print(f"Count of scores: {len(scores)}")
    print(f"Sum: {sum(scores)}")
    print(f"Average: {sum(scores)/len(scores):.2f}")

    print("\n=== local branch output (max & min) ===")
    print(f"Maximum: {max(scores)}")
    print(f"Minimum: {min(scores)}")

if __name__ == "__main__":
    main()