import numpy as np
import csv
# import pickle

def save_data(csv_path):
    data_structure = {}
    
    with open(csv_path, 'r', encoding='euc-kr') as file:
        reader = csv.reader(file)
        header = next(reader)  # 첫 번째 행 건너뛰기
        
        for row in reader:
            domain = row[0]  # 영역
            category = row[1]  # 유형
            standard = int(row[2])  # 표준점수
            male = float(row[3])  # 남자
            female = float(row[4])  # 여자
            
            if domain not in data_structure:
                data_structure[domain] = {}
            
            if category not in data_structure[domain]:
                data_structure[domain][category] = [[], [], [], [], []]
            
            data_structure[domain][category][0].append(standard)
            data_structure[domain][category][1].append(male)
            data_structure[domain][category][2].append(female)

    print("과목명 / 남자 총 응시자수 / 여자 총 응시자수")
    for domain, categories in data_structure.items():
        for category, lists in categories.items():
            male_tot = sum(data_structure[domain][category][1])
            female_tot = sum(data_structure[domain][category][2])
            data_structure[domain][category] = [np.array(l) for l in lists]
            data_structure[domain][category][3] = data_structure[domain][category][1]/male_tot*100
            data_structure[domain][category][4] = data_structure[domain][category][2]/female_tot*100
            print(f"{category}: {male_tot}, {female_tot}")    
    return data_structure

# #if __name__ == "__main__":
#     path = "20231231.csv" 
#     result = save_data(path)
#     print(result)

#     with open('suneung.pkl', 'wb') as f:
# 	    pickle.dump(result, f, protocol=pickle.HIGHEST_PROTOCOL)
