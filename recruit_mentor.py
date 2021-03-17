# 2021 세명대학교 컴퓨터학부 멘토링 프로그램 멘토 모집
# Written by ypkim@semyung.ac.kr 

# 기본 역할: 파이썬 스터디 구성 및 진행 (10주), 매주 스터디 활동 내용 보고 (email or ZOOM)
# 선택 역할: 대면기간 프로그래밍기초 실습 수업 보조 (9주-11주, 주당2시간, 기본 4인 선발. 인원은 필요시 조정)
# 멘토 자격: 아래 recruit_mentor.py 프로그램 참고
# 모집 기한: 2021-03-26 (금) 18:00 까지 (한국표준시)
# 혜택: 장학금 (기본 15만원, 선택 보조시 최대 6만원)
# 신청 및 문의: 학부 조교 (043-649-1700)

def Nothing():
    for i in range(80):
        print("*", end='')
    print("")
    
def Purpose():
    print("소규모 그룹 스터디를 통해 파이썬 프로그래밍 동기 증진 및 학습 보완")
    print("선후배간 교류 증진을 원하는 스터디 멘토를 모집합니다!!")

def Qualification():
    a_year = int(input("몇 학년 입니까?"))
    if (a_year <= 1 or a_year > 4):
        return False    
    ans1 = input("프로그래밍기초 수업을 수강했고, 학점이 A이상입니까? (Y/N)")
    if (ans1 == "Y" or ans1 == "y"):
        return True
    else:
        ans2 = input("파이썬 프로그래밍 스터디 멘토링이 가능합니까? (Y/N)")
        if (ans2 == "Y" or ans2 == "y"):
            return True
    return False

def Target():
    print("1학년 프로그래밍 기초 수강생 중 멘티 지원자")

if __name__ == "__main__":
    while True:
        Nothing()
        Purpose()
        Nothing()
        Target()
        if (Qualification() == True):
            break
    print("당장! 지원하십시오!")
