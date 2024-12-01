import eunsun, ujin

def isvalid(year, realm):
    yearfalse, realmfalse = 0,0
    if year != 2023:
        yearfalse = 1
    if realm not in df:
        realmfalse = 1
    return (yearfalse, realmfalse)

def subject(realm):
    temp = []
    possible_list = list(set(df[realm]))
    return possible_list

df = eunsun.save_data('20231231.csv')

while True:
    wanna_know_year = int(input("시험 시행년도를 입력하세요(데이터 상 존재하는 연도 : 2023) : "))
    wanna_know_realm = input("영역을 입력하세요(데이터 상 존재하는 영역: 국어, 수학, 사회탐구, 과학탐구, 직업탐구) : ")
    valid_data = isvalid(wanna_know_year, wanna_know_realm)
    if 1 not in valid_data:
        temp = ", ".join(subject(wanna_know_realm))
        wanna_know_subject = input(f"과목을 입력하세요. 과목은 다음과 같습니다. ({temp}) : ")
        if wanna_know_subject not in df[wanna_know_realm]:
            print(f"{wanna_know_subject} 과목은 존재하지 않습니다.")
        else:
            ujin.draw_graph(df, wanna_know_realm, wanna_know_subject)
            break
    else:
        print(["", f"데이터에 {wanna_know_year}년이 존재하지 않습니다."][valid_data[0]], ["", f"데이터에 {wanna_know_realm} 영역은 없습니다."][valid_data[1]])
