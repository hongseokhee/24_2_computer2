##### 데이터 파일은 반드시 yyyy1231.csv 형태로 저장할 것 #####

import eunsun, ujin

def isvalid(realm):
    realmfalse = 0
    if realm not in df:
        realmfalse = 1
    return realmfalse

def subject(realm):
    temp = []
    possible_list = list(set(df[realm]))
    return possible_list

while True:
    wanna_know_year = (input("시험 시행년도를 입력하세요(데이터 상 존재하는 연도 : 2020, 2021, 2022, 2023) : "))
    try:
        year = int(wanna_know_year)
    except ValueError:
        print(f"{wanna_know_year}는 연도가 아닙니다.")
        continue
    wanna_know_year = int(wanna_know_year)
    if wanna_know_year > 2023 or wanna_know_year < 2020:
        print(f"데이터 상에 {wanna_know_year}년은 없습니다.")
        continue
    df = eunsun.save_data(f'{wanna_know_year}1231.csv')
    wanna_know_realm = input("영역을 입력하세요(데이터 상 존재하는 영역: 국어, 수학, 사회탐구, 과학탐구, 직업탐구) : ")
    valid_data = isvalid(wanna_know_realm)
    if valid_data != 1:
        temp = ", ".join(subject(wanna_know_realm))
        wanna_know_subject = input(f"과목을 입력하세요. 과목은 다음과 같습니다. ({temp}) : ")
        if wanna_know_subject not in df[wanna_know_realm]:
            print(f"{wanna_know_subject} 과목은 존재하지 않습니다.")
        else:
            data_type = int(input("그래프를 그리는 데 사용할 데이터의 종류를 선택해주세요. 1) 명수 2) 비율 (1 또는 2 입력): "))
            if data_type == 1 or data_type == 2:
                ujin.draw_graph(df, wanna_know_realm, wanna_know_subject, data_type)
                break
            else:
                print(f"{data_type}라는 데이터 종류는 없습니다.")
    else:
        print(f"데이터에 {wanna_know_realm} 영역은 없습니다.")