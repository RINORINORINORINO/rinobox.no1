
while True:
    num1 = float(input("첫 번째 숫자를 입력하세요"))
    operator = input("연산자를 입력하세요 (+,-, *, /)")
    num2 = float(input("두 번째 숫자를 입력하세요"))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "0으로 나눌 수 없습니다."
    else:
        result = "연산자를 잘못 입력하셨습니다."

    print("결과: ", result)

    exit_choice = input("계속하시겠습니까? (y/n)")
    if exit_choice.lower() != "y":
        print("프로그램을 종료합니다.")
        break
