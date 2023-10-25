def calculate_incident_rate():
    while True:
        try:
            num_incidents = int(input("재해자수를 입력하세요: "))
            num_employees = int(input("상시 근로자수를 입력하세요: "))

            if num_employees <= 0:
                print("상시 근로자수는 0 이상의 값이어야 합니다. 다시 입력하세요.")
                continue  # 다시 입력하도록 함
            else:
                incident_rate = (num_incidents / num_employees) * 100
                return incident_rate

        except ValueError:
            print("유효한 숫자를 입력해야 합니다. 다시 입력하세요.")

if __name__ == "__main__":
    print("환산 재해율 계산기")

    while True:
        result = calculate_incident_rate()
        if isinstance(result, str):
            print(result)
        else:
            print(f"환산 재해율: {result:.2f}%")

        while True:
            another_calculation = input("다시 계산하시겠습니까? (y/n): ").lower()
            if another_calculation in ["y", "n"]:
                break
            else:
                print("올바른 입력을 하십시오. 'y' 또는 'n' 중 하나를 입력하세요.")

        if another_calculation == "n":
            break
