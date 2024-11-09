def find_divisors(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return divisors

if __name__ == "__main__":
    try:
        # 표준 입력으로 숫자를 받기
        num = int(input())
        # 약수를 쉼표로 구분하여 출력
        print(", ".join(map(str, find_divisors(num))))
    except ValueError:
        print("Please enter a valid integer.")
