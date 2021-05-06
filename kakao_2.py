from itertools import permutations
import re


def solution(expression):
    answer = 0
    operators = ["-", "+", "*"]
    sep_expression = re.compile("(\D)").split(expression)
    for operator in permutations(operators, 3):
        express = sep_expression
        for oper in operator:
            idx = 0
            while idx < len(express):
                if express[idx] == oper:
                    if oper == "-":
                        cal = int(express[idx-1]) - int(express[idx+1])
                    elif oper == "+":
                        cal = int(express[idx-1]) + int(express[idx+1])
                    else:
                        cal = int(express[idx-1]) * int(express[idx+1])
                    express = express[:idx-1] + \
                        list(str(cal).split()) + express[idx+2:]
                else:
                    idx += 1
        else:
            answer = max(answer, abs(int(express[0])))
    return answer


print(solution("100-200*300-500+20"))
