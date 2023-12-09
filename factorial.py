import unittest

def factorial(inputNum):
    num = 1
    if inputNum == 0: # 0이 들어오는 경우 (0! = 1을 처리하기 위함)
        return 1
    else: # 그외의 나머지 계산
        for i in range(1,inputNum+1):
            num *= i
        return num

class test_first_letter(unittest.TestCase):
    def test_capitalize_first_letter(self):
        self.assertEqual(factorial(3),6)
        self.assertEqual(factorial(0),1)

if __name__ == "__main__":
    unittest.main(exit=False)
