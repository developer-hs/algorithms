def solution(s):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    alpha = ["zero", "one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine"]
    string = ""
    answer_li = []
    answer = ""
    for i in s:
        string += i
        if string in alpha:
            answer_li.append(string)
            string = ""
        elif string in numbers:
            answer_li.append(i)
            string = ""
    for a in answer_li:
        if a in numbers:
            answer += a
        else:
            answer += str(alpha.index(a))

    return int(answer)


print(solution("one4seveneight"))
