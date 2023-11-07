import functools
import operator

#input = '  3/4/2 '


def Div(input):
    # 앞뒤 공백 삭제 후 연산자를 공백으로 교체
    modified_str = input.strip().replace("/"," ")

    # 문자열을 공백 기준으로 분리하여 정수로 변환
    numbers = list(map(int, modified_str.split()))

    # 숫자들의 나눗셈 계산
    result = functools.reduce(operator.truediv, numbers)
    print(result)
