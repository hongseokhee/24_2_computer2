import numpy as np
import csv

def save_data(csv_path):
    data_structure = {}
    
    with open(csv_path, 'r', encoding='euc-kr') as file:
        reader = csv.reader(file)
        header = next(reader)  # 첫 번째 행 건너뛰기
        
        for row in reader:
            domain = row[0]  # 영역
            category = row[1]  # 유형
            standard = float(row[2])  # 표준점수
            male = int(row[3])  # 남자
            female = int(row[4])  # 여자
            
            if domain not in data_structure:
                data_structure[domain] = {}
            
            if category not in data_structure[domain]:
                data_structure[domain][category] = []
            
            data_structure[domain][category].append([standard, male, female])
    
    result = [[domain, [[category, values] for category, values in categories.items()]] for domain, categories in data_structure.items()]
    
    return np.array(result, dtype=object)

if __name__ == "__main__":
    path = "20231231.csv" 
    result_ndarray = save_data(path)
    print(result_ndarray)
