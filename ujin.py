import numpy as np
import matplotlib.pyplot as plt
# import pickle

# 터미널에서 폰트 미리 설치해야 됨
# sudo apt-get install -y fonts-nanum
# sudo fc-cache -fv
# rm ~/.cache/matplotlib -rf
from matplotlib import rcParams
plt.rc('font', family='NanumGothic')
rcParams['axes.unicode_minus'] = False

def draw_graph(data, domain, category, data_type):
    data_for_graph = data[domain][category]
    standard = data_for_graph[0]
    if data_type == 1:
        male = data_for_graph[1]
        female = data_for_graph[2]
    elif data_type == 2:
        male = data_for_graph[3]
        female = data_for_graph[4]

    plt.figure(figsize=(8, 6))

    plt.scatter(standard, male, label='남학생', color='blue', alpha=0.6, s=10, marker='s') # marker 모양을 square로 바꿈.
    plt.scatter(standard, female, label='여학생', color='orange', alpha=0.6, s=10, marker='o') # marker 모양을 circle로 바꿈.  

    plt.title(f"2024 수능 {category} 과목 분포", fontsize=14)
    plt.xlabel("표준점수", fontsize=12)
    plt.ylabel("명수" if data_type == 1 else "퍼센트", fontsize=12)
    plt.legend(fontsize=10)

    plt.grid(alpha=0.3)

    plt.show()

    plt.savefig(f"{domain}_{category}_scatter_graph_{'numbers' if data_type == 1 else 'percentages'}.png", dpi=300)
    print(f"{domain}_{category}_scatter_graph.png라는 파일명으로 그래프 저장됨")

    plt.close()

# if __name__ == "__main__":
#     with open('suneung.pkl', 'rb') as f:
# 	    data = pickle.load(f)