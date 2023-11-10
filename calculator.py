#2023.11.10(금) calculator Version.4

#연산자 함수 add, sub, mul
def calculate(inputNum):
    def add(inputNum):
        sum=inputNum[0]
        for i in range (2, len(inputNum),2):
            sum += inputNum[i]
        return sum

    def sub(inputNum):
        sum = inputNum[0]
        for i in range(2, len(inputNum),2):
            sum -= inputNum[i]
        return sum

    def mul(inputNum):
        sum = inputNum[0]
        for i in range (2, len(inputNum),2):
            sum *= inputNum[i]
        return sum

    if inputNum[1]=='+':
        result = add(inputNum)

    elif inputNum[1]=='-':
        result = sub(inputNum)

    elif inputNum[1]=='*':
        result = mul(inputNum)

    print(result)
    print("--------------")
    inputNum.clear()
            
            
# 이스터에그 함수
def easterEgg(inputNum):

    easter1 = [63, '-', 430, '-', 3428]
    easter2 = [112, '+', 119]
    easter3 = [1577, '-', 1577]

    easterDict = {
        7534: "=> HELP!",
        777: "=> JACKPOT!",
        404: "=> 404 NOT FOUND",
        100: "=> Perfect score!",
        0: "=> ZERO",
        2023: "=> 2023년은 계묘년, 검은 토끼의 해입니다.",
        20231019: "=> 소프트웨어공학(2분반) 중간고사 날짜입니다."
    }

    if inputNum[-1] in easterDict:
        print(easterDict[inputNum[-1]])

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

# ERROR 메시지 출력 후 이전까지의 입력값을 보여주는 함수
def printList(inputLine):
    print("<진행 중인 연산>")
    for e in inputLine:
        print(e, end=" ")
    if len(inputLine) != 0 : print(" ")

# main 함수
def main():
    inputLine = []
    print("계산기 시작 (프로그램을 종료하려면 exit를 입력하세요)")
    while True:
        line = input()

        # 루프 종료 조건
        if line == "exit" : break
        
        # 입력이 연산자인 경우
        elif line in ['+', '-', '*','=']:
            # 첫번째 입력이 연산자인 경우 & 연산자가 연속 2번 입력된 경우
            if len(inputLine) == 0 or inputLine[-1] in ['+', '-', '*']:
                print("ERROR: 연산자가 아닌 숫자를 입력하세요")
                print("--------------")
                printList(inputLine)
                continue
            # 입력이 '='인 경우
            elif line in '=':
                # 숫자가 하나만 있는 경우 (ex, 3 = 이 들어오면 3 출력)
                if len(inputLine) == 1:
                    print(inputLine[0])
                    print("--------------")
                    inputLine.clear()
                    continue
                # 결과 출력 
                else:
                    calculate(inputLine)
                    inputLine.clear()
                    continue
            # 입력된 연산자가 처음 입력된 연산자와 다른 경우
            elif len(inputLine) > 2 and line != inputLine[1]:
                print("ERROR: 한 가지 종류의 연산자만 입력하세요")
                print("--------------")
                printList(inputLine)
                continue
            # 위 경우에 걸리지 않는 경우 - 정상
            else:
                inputLine.append(line)
                continue
        
        # 입력이 숫자 혹은 그 외의 경우
        else:
            # 정수 입력의 경우
            try:
                num = int(line)
                if len(inputLine) == 0:
                    inputLine.append(num)
                    easterEgg(inputLine)
                    continue
                # 숫자가 연속 2번 들어온 경우
                elif type(inputLine[-1]) is int:
                    print("ERROR: 잘못된 값이 입력되었습니다. 연산자를 입력하세요")
                    print("--------------")
                    printList(inputLine)
                    continue
                # 숫자가 임계값을 넘어간 경우
                elif num > 100000:
                    print("ERROR: 입력된 수가 임계값 100000을 넘었습니다.")
                    print("--------------")
                    printList(inputLine)
                    continue
                # 첫번째 입력이 숫자인 경우 & 이전 입력이 연산자인 경우 -> 정상
                else: 
                    inputLine.append(num)
                    easterEgg(inputLine)
                    continue

            # 잘못된 입력의 경우 (연산자 또는 정수가 아님)
            except ValueError:
                print("ERROR: 잘못된 값이 입력되었습니다. 정수 또는 연산자(+,-,*)를 입력하세요")
                print("--------------")
                printList(inputLine)
                continue

main()
