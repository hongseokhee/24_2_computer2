import module1, module2

def isvalid(year, subject):
    yearfalse, subjectfalse = 0,0
    if year not in df:
        yearfalse = 1
    if subject not in df:
        subjectfalse = 1
    return (yearfalse, subjectfalse)

df = module1.save_data('.csv')

while True:
    wanna_know_year = int(input("연도를 입력하세요 : "))
    wanna_know_subject = input("과목을 입력하세요 : ")
    valid_data = isvalid(wanna_know_year, wanna_know_subject)
    if 1 not in valid_data:
        module2.draw_graph(wanna_know_year, wanna_know_subject)
        break
    else:
        print(["", f"데이터에 {wanna_know_year}년이 존재하지 않습니다."][valid_data[0]], ["", f"데이터에 {wanna_know_subject} 과목은 없습니다."][valid_data[1]])
