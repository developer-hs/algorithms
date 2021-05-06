from collections import defaultdict


def solution(record):
    new_record = [i.split() for i in record]
    visited = defaultdict(str)
    answer = []
    for r in new_record[::-1]:
        if not visited[r[1]] and r[0] != "Leave":
            visited[r[1]] = r[2]

    for r in new_record:
        if r[0] == "Enter":
            answer.append(f"{visited[r[1]]}님이 들어왔습니다.")
        elif r[0] == "Leave":
            answer.append(f"{visited[r[1]]}님이 나갔습니다.")
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
      "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
