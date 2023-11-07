def error(list):
    # 1. 리스트의 첫 번째 원소부터 홀수 번째에 정수가 입력되었는지 확인
    for i in range(0, len(list), 2):
        if not isinstance(list[i], int):
            return 0

    # 2. 리스트의 짝수 번째에 +, -, * 연산자가 입력되었는지 확인
    operators = set(['+', '-', '*'])
    for i in range(1, len(list), 2):
        if list[i] not in operators:
            return 0

    # 3. 입력된 연산자가 한 가지 종류의 연산자만 입력되었는지 확인
    if len(set(list[1::2])) != 1:
        return 0
    

    # 4. 입력된 수가 임계값을 넘었는지 확인
0
    for i in range(0, len(list), 2):
        if list[i] > 100000:
            return 0

    return 1
