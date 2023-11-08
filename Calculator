#연산자 함수 Add, Sub, Mul

def calculate(inputNum):
    def Add(inputNum):
        sum=inputNum[0]
        for i in range (1, len(inputNum)):
            if i % 2 == 0:
                sum += inputNum[i]
        return sum


    def Sub(inputNum):
        sum = inputNum[0]
        for i in range(1, len(inputNum)): 
            if i % 2 == 0:
                sum -= inputNum[i]
        return sum

    def Mul(inputNum):
        sum = inputNum[0]
        for i in range (1, len(inputNum)):
            if i % 2 == 0:
                sum *= inputNum[i]
        return sum


    if inputNum[1]=='+':
        result = Add(inputNum)

    elif inputNum[1]=='-':
        result = Sub(inputNum)

    elif inputNum[1]=='*':
        result = Mul(inputNum)

    print(result)
    print("--------------")
    inputNum.clear()
            
            

# 이스터에그 함수

def easterEgg(inputNum):

    easter1 = [63, '-', 430, '-', 3428]
    easter2 = [112, '+', 119]
    easter3 = [1577, '-', 1577]

    easter_dict = {
        7534: "=> HELP!",
        777: "=> JACKPOT!",
        404: "=> 404 NOT FOUND",
        100: "=> Perfect score!",
        0: "=> ZERO",
        2023: "=> 2023년은 계묘년, 검은 토끼의 해입니다.",
        20231019: "=> 소프트웨어공학(2분반) 중간고사 날짜입니다."
    }

    if inputNum[-1] in easter_dict:
        print(easter_dict[int(inputNum[-1])])

    for i in range(len(inputNum) - len(easter1) + 1):
        if inputNum[i:i+len(easter1)] == easter1:
            print("=> 정종욱 교수")
            print("소프트웨어 인터랙션 연구실")
            print("공대 7호관 503호")
            print("Email: jwjeong55@jbnu.ac.kr")
            print("전화번호: 063 - 270 - 3428")
    
    for i in range(len(inputNum) - len(easter2) + 1):
        if inputNum[i:i+len(easter2)] == easter2:
            print("=> 폭력, 밀수, 학대, 미아, 해킹 등 범죄 112")
            print("구조·구급, 해양·전기·가스사고, 유해물질 유출 119")

    for i in range(len(inputNum) - len(easter3) + 1):
        if inputNum[i:i+len(easter3)] == easter3:
            print("=> 앞뒤가 똑같은 전화번호 (1577)")
            print("앞뒤가 똑같은 전화번호")
            print("1577 1577")
            print("앞뒤가 똑같은 대리운전 (1577)")
            print("앞뒤가 똑같은 번호 1577")
            print("대리운전 1577")
            


# error 함수

def error(inputNum):
    # 1. 리스트의 첫 번째 원소부터 홀수 번째에 정수가 입력되었는지 확인_정환(main)
    # 2. 리스트의 짝수 번째에 +, -, * 연산자가 입력되었는지 확인_정환(main)
    
    # 3. 입력된 연산자가 한 가지 종류의 연산자만 입력되었는지 확인
    operators = set(inputNum[1::2])
    operators.discard(inputNum[-1])

    if len(operators) != 1:
        print("ERROR: 한 가지 종류의 연산자만 입력하세요")
        print("--------------")
        inputNum.clear()
        return 0

    # 4. 입력된 수가 임계값을 넘었는지 확인
    for i in range(0, len(inputNum), 2):
        if inputNum[i] >= 100000:
            print("ERROR: 입력된 수가 임계값 100000을 넘었습니다.")
            print("--------------")
            return 0
        #inputNum.clear()
    return 1


# 음수를 숫자로 판별하는 메서드

def is_negative_numeric(input_string): 
    try: 
        int(input_string) # 문자열을 정수로 변환하려 시도 
        return True # 변환이 성공하면 True를 반환 
    except ValueError: 
        return False # 변환이 실패하면 False를 반환



# main 함수

def main():
    inputNum = []
    print("계산기 시작 (프로그램을 종료하려면 exit를 입력하세요)")
    while True:
        line = input()

        # 입력이 연산자인경우
        if line in ['+', '-', '*','=']:
            # 마지막 입력이 연산자 혹은 첫 입력이 연산자인 경우
            if len(inputNum) == 0 or inputNum[-1] in ['+', '-', '*']:
                print("ERROR: 연산자가 아닌 숫자를 입력하세요")
                print("--------------")
                inputNum.clear()
                continue
            else: # 그 전 입력이 숫자인 경우
                inputNum.append(line) # 연산자 추가
                
                # 여기서 부턴 = 에 대한 연산 진행
                if line == '=':
                    # 에러 함수에 값 전달
                    # if 에러가 없으면: 연산자 함수에 값 전달 후 아래 내용 진행
                    if error(inputNum)==1:
                        calculate(inputNum)
                    else:
                        inputNum.clear
                    continue

        elif line == 'exit':
            break

        else:  # 현재 입력이 숫자일 경우
            if is_negative_numeric(line):
                inputNum.append(int(line))
                easterEgg(inputNum) 
                continue

            else:
                try:
                    int(line)    #문자열을 정수로 변환하려 시도 - 실패시 except 
                    # 전 입력 값이 숫자가 아닌 경우
                    if len(inputNum) !=0 and not type(inputNum[-1]) is int:
                        inputNum.append(int(line))
                        continue

                    elif len(inputNum) == 0:
                        inputNum.append(int(line))
                        continue

                    else:
                        print("ERROR: 잘못된 값이 입력되었습니다. 숫자를 입력하세요")
                        print("--------------")
                        inputNum.clear()
                        continue
                except ValueError: # 연산자 아닌데 숫자도, =도 아니거나 그 전값이 숫자인 경우
                    print("ERROR: 잘못된 값이 입력되었습니다. 정수 또는 연산자(+,-,*)를 입력하세요")
                    print("--------------")
                    inputNum.clear()
                    continue
            
main()
