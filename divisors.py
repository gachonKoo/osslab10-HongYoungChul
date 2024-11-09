import sys

def find_divisors(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return divisors

if __name__ == "__main__":
    try:
        # sys.stdin을 사용하여 모든 입력 읽기
        num = int(sys.stdin.read().strip())
        print(", ".join(map(str, find_divisors(num))))
    except ValueError:
        print("Please enter a valid integer.")
