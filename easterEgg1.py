git commit -m "KAN-35 <message>"

# 이스터에그 함수 1
# 이스터에그 조건에 맞아 출력이 있는 경우 return 0
# 이스터에그 조건에 맞지 않아 출력이 없는 경우 return 1
def easterEgg1(arr):
    flag = 1

    # 모든 입력이 '*'인 경우 "STAR!" 출력
    if all(x == '*' for x in arr):
        print("STAR!")
        flag = 0

    # 하나의 입력이 들어왔고, 입력이 "777"인 경우 "JACKPOT!" 출력
    elif len(arr) == 1 and arr[0] == "777":
        print("JACKPOT!")
        flag = 0

    # 하나의 입력이 들어왔고, 입력이 "404"인 경우 "404 NOT FOUND" 출력
    elif len(arr) == 1 and arr[0] == "404":
        print("404 NOT FOUND")
        flag = 0

    # 하나의 입력이 들어왔고, 입력이 "100"인 경우 "Perfect score!" 출력
    elif len(arr) == 1 and arr[0] == "100":
        print("Perfect score!")
        flag = 0

    if(flag == 1) : return 1
    else : return 0

# 계산 함수
def calculator(arr):
    # 계산 함수 구현
    result = 0

    # **마지막 결과 출력 부분에 추가해주세요**
    # 결과가 0인 경우 0이 아닌 "ZERO" 출력
    if(result == 0):
        print("ZERO")
    else:
        print(result)

    return 0;

def main():

    return 0;
