import sys

def find_divisors(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return divisors

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
        print(", ".join(map(str, find_divisors(num))))
    else:
        print("Please provide a number as a command line argument.")
