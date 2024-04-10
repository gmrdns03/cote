"""
프로그래머스
코딩테스트 연습 > 코딩테스트 입문 > 옹알이 (1)
"""

def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    answer = 0
    for b in babbling:
        for w in words:
            b = b.replace(w, " ")

        if len(b.strip()) == 0 :
            answer += 1
    return answer

if __name__ == "__main__":
    # 첫번째 답 1
    # 두번째 답 3
    first = ["aya", "yee", "u", "maa", "wyeoo"]
    second = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
    answer_1 = solution(first)
    print(answer_1)
    answer_2 = solution(second)
    print(answer_2)
