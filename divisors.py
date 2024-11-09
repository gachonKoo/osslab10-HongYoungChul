import sys

def find_divisors(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return divisors

if __name__ == "__main__":
    try:
        # 여러 줄 입력을 받아 각 줄을 처리
        for line in sys.stdin:
            num = int(line.strip())
            print(", ".join(map(str, find_divisors(num))))
    except ValueError:
        print("Please enter a valid integer.")
