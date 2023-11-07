def main():
    inputNum = []
    print("프로그램 종료 : exit")
    while True:
        line = input()
        # 입력이 연산자인경우
        if line in ['+', '-', '*','=']:
            # 마지막 입력이 연산자 혹은 첫 입력이 연산자인 경우
            if len(inputNum) == 0 or inputNum[-1] in ['+', '-', '*']:
                print("Invalid input. Please try again.")
                continue
            # 그 전 입력이 숫자인 경우
            else:
                inputNum.append(line) # 연산자 추가
                
                # 여기서 부턴 = 에 대한 연산 진행
                if line == '=':
                    # 에러 함수에 값 전달
                    # if 에러가 없으면: 연산자 함수에 값 전달 후 아래 내용 진행
                    print(inputNum) # 디버깅 위해 추가 추후 삭제
                    inputNum.clear() # 다음 연산을 위해 리스트 비움
                    continue
                    # else : # 에러 있으면 리스트 비우고 다시 연산 진행
                    # inputNum.clear()
                    # continue
               
        # 입력 exit 면 종료
        elif line == 'exit':
            break
        # 현재 입력이 연산자 아닐경우 (숫자)
        else:
            # 음수인지 확인
            try: 
                int(line) # 문자열을 정수로 변환하려 시도 - 만약 여기서 안돼면 except 
                if len(inputNum) !=0 and not type(inputNum[-1]) is int:
                    inputNum.append(int(line))
                    # 이스터 에그 값인지 확인
                    # 이스터에그 함수에 값 전달
                elif len(inputNum) == 0:
                    inputNum.append(int(line))
                    # 이스터 에그 값인지 확인
                    # 이스터에그 함수에 값 전달
                # 전 입력 값이 숫자인 경우라 중복으로 숫자 입력 및 저장 거부
                else: 
                    print("Invalid input. Please try again.")
                    continue
            # 만약에 정수 변환 과정에서 숫자가 아니라 int 변환이 안된경우
            except ValueError:
                print("Invalid input. Please try again.")
                continue    
main()

