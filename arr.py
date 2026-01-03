import os
import sys

def parse(s):
    nums = []
    for x in s.replace(",", " ").split():
        try:
            nums.append(float(x))
        except ValueError:
            print(f"Warning: skipping non-numeric token: {x}")
    return nums

def read_scores():
    if len(sys.argv) > 1:
        return parse(" ".join(sys.argv[1:]))
    
    scores_env = os.getenv("SCORES")
    if scores_env:
        return parse(scores_env)
    
    if os.path.isfile("scores.txt"):
        with open("scores.txt", "r") as f:
            return parse(f.read())
    
    try:
        user_input = input("Enter scores separated by spaces or commas: ")
        return parse(user_input)
    except EOFError:
        return []

def main():
    scores = read_scores()
    if not scores:
        print("No valid scores provided.")
        sys.exit(1)

    print("=== main/master branch output ===")
    print(f"Count of scores: {len(scores)}")
    print(f"Sum: {sum(scores)}")
    print(f"Average: {sum(scores)/len(scores):.2f}")

if __name__ == "__main__":
    main()