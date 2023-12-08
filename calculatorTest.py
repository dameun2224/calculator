import unittest
from calculator import calculate, easterEgg, main # 팩토리얼 추가 import 해야함
from unittest.mock import patch
from io import StringIO
import sys

# 테스트케이스 상속 받는 테스트 클래스 생성
class TestCalculateMethods(unittest.TestCase):
    def capture_output_calculate(self, input_data, expected):
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function
        calculate(input_data)

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Check the output
        self.assertIn(expected, captured_output.getvalue().strip())
        
    def test_add_case(self):
        self.capture_output_calculate([1, '+', 2], "3\n--------------")
        self.capture_output_calculate([3, '+', -2], "1\n--------------")
    def test_sub_case(self):
        self.capture_output_calculate([1, '-', 2], "-1\n--------------")
        self.capture_output_calculate([3, '-', -2], "5\n--------------")
        self.capture_output_calculate([3, '-', 2], "1\n--------------")
    def test_mul_case(self):
        self.capture_output_calculate([1, '*', 2], "2\n--------------")
        self.capture_output_calculate([2, '*', 3], "6\n--------------")
        self.capture_output_calculate([2, '*', -4], "-8\n--------------")
        self.capture_output_calculate([3, '*', 0], "0\n--------------")
        
        
# class TestFactorialMethod(unittest.TestCase):
#     def test_fac(self):
#         self.assertEqual(factorial(5), 120)
#         self.assertEqual(facorial(10), 3628800)
#         self.assertEqual(factorial(0), 1)
#         self.assertEqual(factorial(1), 1)
#         # more case       
        
class TestEasterEggMethods(unittest.TestCase):
   def test_easter_egg_output(self):
    # Test data and expected output
    test_cases = [
        ([7534], "[EVENT] => HELP!"),
        ([777], "[EVENT] => JACKPOT!"),
        ([404], "[EVENT] => 404 NOT FOUND"),
        ([100], "[EVENT] => Perfect score!"),
        ([0], "[EVENT] => ZERO"),
        ([2023], "[EVENT] => 2023년은 계묘년, 검은 토끼의 해입니다."),
        ([20231019], "[EVENT] => 소프트웨어공학(2분반) 중간고사 날짜입니다."),
        ([63, '-', 430, '-', 3428], "[EVENT] => 정종욱 교수\n소프트웨어 인터랙션 연구실\n공대 7호관 503호\nEmail: jwjeong55@jbnu.ac.kr\n전화번호: 063 - 270 - 3428"),
        ([112, '+', 119], "[EVENT] => 폭력, 밀수, 학대, 미아, 해킹 등 범죄 112\n구조·구급, 해양·전기·가스사고, 유해물질 유출 119"),
        ([1577, '-', 1577], "[EVENT] => 앞뒤가 똑같은 전화번호 (1577)\n앞뒤가 똑같은 전화번호\n1577 1577\n앞뒤가 똑같은 대리운전 (1577)\n앞뒤가 똑같은 번호 1577\n대리운전 1577"),
        ([1015], "[EVENT] 전북대 개교기념일입니다.")
    ]

    for input_data, expected in test_cases:
        #각 subTest는 테스트 케이스의 일부분으로, 실패하더라도 다른 서브테스트의 실행에 영향을 주지 않음. 이를 통해 여러 데이터 세트 또는 조건들에 대한 테스트를 한 테스트 케이스 내에서 수행
        with self.subTest(input_data=input_data):
            # Capture the output
            captured_output = StringIO()
            sys.stdout = captured_output

            # Call the function
            easterEgg(input_data)

            # Reset stdout
            sys.stdout = sys.__stdout__

            # Check the output
            self.assertIn(expected, captured_output.getvalue().strip())

class TestMainExceptionMethods(unittest.TestCase):
    
    def capture_output(self, input_sequence):
        with patch('builtins.input', side_effect=input_sequence), \
             patch('sys.stdout', new_callable=StringIO) as captured_output:
            main()
            return captured_output.getvalue()
        
    # 첫번째 입력이 연산자인 경우
    def test_operator_first_error(self):
        input_sequence = ['+', 'exit']
        expected_output = "계산기 시작 (프로그램을 종료하려면 exit를 입력하세요)\n" + \
                          "[SYSTEM] ERROR: 연산자가 아닌 숫자를 입력하세요\n" + \
                          "--------------\n" + \
                          "<진행 중인 연산>\n"
        output = self.capture_output(input_sequence)
        self.assertIn(expected_output, output)
    # 연산자 2번 입력
    def test_consecutive_operators_error(self):
        input_sequence = ['3', '+', '-', 'exit']
        expected_output = "계산기 시작 (프로그램을 종료하려면 exit를 입력하세요)\n" + \
                          "[SYSTEM] ERROR: 연산자가 아닌 숫자를 입력하세요\n" + \
                          "--------------\n" + \
                          "<진행 중인 연산>\n"
        output = self.capture_output(input_sequence)
        self.assertIn(expected_output, output)
    # 임계값 에러
    def test_threshold_exceeded_error(self):
        input_sequence = ['100001', 'exit']
        expected_output = "계산기 시작 (프로그램을 종료하려면 exit를 입력하세요)\n" + \
                          "[SYSTEM] ERROR: 입력된 수가 임계값 100000을 넘었습니다.\n" + \
                          "--------------\n" + \
                          "<진행 중인 연산>\n"
        output = self.capture_output(input_sequence)
        self.assertIn(expected_output, output)
    # 숫자 중복 입력
    def test_consecutive_numbers_error(self):
        input_sequence = ['3', '4', 'exit']
        output = self.capture_output(input_sequence)
        self.assertIn("[SYSTEM] ERROR: 잘못된 값이 입력되었습니다. 연산자를 입력하세요", output)
    # 잘못된 값 입력
    def test_invalid_input_error(self):
        input_sequence = ['abc', 'exit']
        expected_output = "계산기 시작 (프로그램을 종료하려면 exit를 입력하세요)\n" + \
                          "[SYSTEM] ERROR: 잘못된 값이 입력되었습니다. 정수 또는 연산자(+,-,*)를 입력하세요\n" + \
                          "--------------\n" + \
                          "<진행 중인 연산>\n"
        output = self.capture_output(input_sequence)
        self.assertIn(expected_output, output)
    # 정상 입력
    def test_normal_operation(self):
        input_sequence = ['3', '+', '5', '=', 'exit']
        expected_output = "계산기 시작 (프로그램을 종료하려면 exit를 입력하세요)\n" + \
                          "8\n" + \
                          "--------------\n"
        output = self.capture_output(input_sequence)
        self.assertIn(expected_output, output)
        
if __name__ == '__main__':
    unittest.main()
