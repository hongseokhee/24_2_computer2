import numpy as np
import matplotlib.pyplot as plt
import pickle

# 터미널에서 폰트 미리 설치해야 됨
# sudo apt-get install -y fonts-nanum
# sudo fc-cache -fv
# rm ~/.cache/matplotlib -rf
from matplotlib import rcParams
plt.rc('font', family='NanumGothic')
rcParams['axes.unicode_minus'] = False

def draw_graph(data, domain, category):
    data_for_graph = data[domain][category]
    standard = data_for_graph[0]
    male = data_for_graph[1]
    female = data_for_graph[2]

    plt.figure(figsize=(8, 6))

    plt.plot(standard, male, label='남', color='blue')
    plt.plot(standard, female, label='여', color='orange')

    plt.title(f"2024 수능 {category} 과목 분포", fontsize=14)
    plt.xlabel("표준점수", fontsize=12)
    plt.ylabel("명수", fontsize=12)
    plt.legend(fontsize=10)

    plt.grid(alpha=0.3)

    plt.savefig(f"{domain}_{category}_graph.png", dpi=300)
    print(f"{domain}_{category}_graph.png라는 파일명으로 그래프 저장됨")

    plt.close()

if __name__ == "__main__":
    with open('suneung.pkl', 'rb') as f:
	    data = pickle.load(f)
    
    draw_graph(data, '사회탐구', '생활과 윤리')