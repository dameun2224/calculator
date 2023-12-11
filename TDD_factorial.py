import unittest
from calculator import factorial, main
from unittest.mock import patch
from io import StringIO
#import sys

#팩토리얼 정상 작동 테스트
class TestFactorialMethod(unittest.TestCase):
    def test_fac(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        
    #팩토리얼 경계 값 테스트
    def test_boundaryValue(self):
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        
#팩토리얼 예외처리
class TestMainExceptionMethods(unittest.TestCase):
    
    def capture_output(self, input_sequence):
        with patch('builtins.input', side_effect=input_sequence), \
             patch('sys.stdout', new_callable=StringIO) as captured_output:
            main()
            return captured_output.getvalue()

    #팩토리얼 음수 입력된 경우      
    def test_factorial_negative_error(self):
        input_sequence = ['-1','!', 'exit']
        expected_output = "[ERROR] Out Of Range\n"
        output = self.capture_output(input_sequence)
        self.assertIn(expected_output, output)

    # 팩토리얼 숫자 중복 입력
    def test_factorial_consecutive_error(self):
        input_sequence = ['3', '5', '!', 'exit']
        expected_output = "[ERROR] Input Error\n"
        output = self.capture_output(input_sequence)
        self.assertIn(expected_output, output)

if __name__ == '__main__':
    unittest.main()
