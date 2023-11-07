def Sub(input):
    # unit test를 위한 주석
    #input = [13, '-', 2, '-', 4, '-', 2]
    
    result = input[0]   # 초기 결과값을 0번지로 초기화
    for i in range(1, len(input)):  # 0번지로 이미 초기화 했기 때문에 1부터 시작(뺄셈 때문에)
        if input[i] != '-':
            result = result - int(input[i])

    print(result)
