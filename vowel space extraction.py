import pandas as pd
import matplotlib.pyplot as plt
import os
import math
from matplotlib.table import Table
import matplotlib.font_manager as fm

# 폰트 경로 설정 - 맑은 고딕 사용
font_path = r'C:\Windows\Fonts\malgun.ttf'  # Windows의 경우 맑은 고딕 폰트 경로

# 폰트 속성 설정
font_prop = fm.FontProperties(fname=font_path)
plt.rc('font', family=font_prop.get_name())

# CSV 파일 경로 설정 (각 파일에 대해 개별 경로 지정)
csv_folder_path = r'C:\Users\user\Desktop\FastTrack-master\FastTrack-master\Fast Track\csvs'
csv_files = {
    'a': os.path.join(csv_folder_path, r'아.csv'),
    'i': os.path.join(csv_folder_path, r'이.csv'),
    'u': os.path.join(csv_folder_path, r'우.csv')
}

# 모음별 안정적인 값 추출
f1_values = []
f2_values = []
vowel_labels = ['a', 'i', 'u']

for vowel, file_path in csv_files.items():
    try:
        # CSV 파일 읽기
        df = pd.read_csv(file_path)
        
        # 필요한 열이 있는지 확인 (열 이름이 'f1' 및 'f2'인지 확인)
        if 'f1' not in df.columns or 'f2' not in df.columns:
            print(f"Error: CSV 파일에 'f1' 또는 'f2' 열이 없습니다. 파일: {file_path}")
            exit()
        
        # F1, F2 열을 float 형식으로 변환 (필요시)
        df['f1'] = pd.to_numeric(df['f1'], errors='coerce')
        df['f2'] = pd.to_numeric(df['f2'], errors='coerce')
        
        # 결측치 제거
        df = df.dropna(subset=['f1', 'f2'])

        # F1, F2 값에서 가장 빈번한 값 (모드)과 중앙값 (중간 값) 찾기
        f1_mode = df['f1'].mode()[0]
        f2_mode = df['f2'].mode()[0]
        f1_median = df['f1'].median()
        f2_median = df['f2'].median()

        # 모드와 중앙값 비교 후 안정적인 값 선택
        f1_stable = f1_mode if abs(f1_mode - f1_median) < 50 else f1_median
        f2_stable = f2_mode if abs(f2_mode - f2_median) < 100 else f2_median

        f1_values.append(f1_stable)
        f2_values.append(f2_stable)

    except FileNotFoundError:
        print(f"Error: CSV 파일을 찾을 수 없습니다. 경로를 확인해 주세요: {file_path}")
        exit()

# 정상 기준 모음 삼각도 좌표 설정
normal_vowel_labels = ['i', 'a', 'u']
normal_f1_values = [270, 730, 300]
normal_f2_values = [2290, 1090, 870]

# VSA (Vowel Space Area) 계산 (Heron's 공식 사용)
def calculate_vsa(f1_values, f2_values):
    a = math.sqrt((f1_values[1] - f1_values[0])**2 + (f2_values[1] - f2_values[0])**2)
    b = math.sqrt((f1_values[2] - f1_values[1])**2 + (f2_values[2] - f2_values[1])**2)
    c = math.sqrt((f1_values[2] - f1_values[0])**2 + (f2_values[2] - f2_values[0])**2)
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# 실험 대상자 및 정상 기준 VSA 계산
participant_vsa = calculate_vsa(f1_values, f2_values)
normal_vsa = calculate_vsa(normal_f1_values, normal_f2_values)

# 그래프 그리기
fig, ax = plt.subplots(figsize=(8, 9))  # Figure 크기 고정

# 각 모음을 점으로 그리기 (실험 대상자)
for label, f1, f2 in zip(vowel_labels, f1_values, f2_values):
    ax.scatter(f2, f1, label=f'Participant {label}', color='blue')
    ax.text(f2 + 20, f1, label, fontsize=12)

# 실험 대상자 삼각형 그리기
f1_values.append(f1_values[0])  # 삼각형을 닫기 위해 첫 번째 점 추가
f2_values.append(f2_values[0])  # 삼각형을 닫기 위해 첫 번째 점 추가
ax.plot(f2_values, f1_values, linestyle='-', color='black', linewidth=1)

# 정상 기준 모음 삼각도 그리기
for label, f1, f2 in zip(normal_vowel_labels, normal_f1_values, normal_f2_values):
    ax.scatter(f2, f1, label=f'Normal {label}', color='red')
    ax.text(f2 + 20, f1, f'Normal {label}', fontsize=12)

# 정상 기준 삼각형 그리기
normal_f1_values.append(normal_f1_values[0])  # 삼각형을 닫기 위해 첫 번째 점 추가
normal_f2_values.append(normal_f2_values[0])  # 삼각형을 닫기 위해 첫 번째 점 추가
ax.plot(normal_f2_values, normal_f1_values, linestyle='--', color='red', linewidth=1)

# 축 반전 설정
ax.invert_yaxis()  # F1 축 반전
ax.invert_xaxis()  # F2 축 반전 (좌우 반전)

# 그래프 레이블 설정
ax.set_xlabel('F2 (Hz)')
ax.set_ylabel('F1 (Hz)')
ax.set_title('Vowel Triangle with Stable Formants (Normal vs Participant)')
ax.legend()
ax.grid(True)

# VSA 및 F1, F2 값 표 출력
data = [
    ["F1 (a)", 730, round(f1_values[0], 2), round(f1_values[0] - 730, 2)],
    ["F2 (a)", 1090, round(f2_values[0], 2), round(f2_values[0] - 1090, 2)],
    ["F1 (i)", 270, round(f1_values[1], 2), round(f1_values[1] - 270, 2)],
    ["F2 (i)", 2290, round(f2_values[1], 2), round(f2_values[1] - 2290, 2)],
    ["F1 (u)", 300, round(f1_values[2], 2), round(f1_values[2] - 300, 2)],
    ["F2 (u)", 870, round(f2_values[2], 2), round(f2_values[2] - 870, 2)],
    ["Area of Vowel Triangle (VSA)", round(normal_vsa, 2), round(participant_vsa, 2), round(participant_vsa - normal_vsa, 2)]
]

# 표 그리기
columns = ["Metric", "Person A (Normal)", "Person B (Participant)", "A - B"]

# 그래프 내에 표 추가
table = ax.table(cellText=data, colLabels=columns, cellLoc='center', loc='bottom', bbox=[0.0, -0.44, 1.0, 0.3])
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(columns))))

# 해석 텍스트 도출
def generate_interpretation():
    interpretations = []
    
    # /i/ 모음 F2 값 해석
    if f2_values[1] - 2290 > 100:
        interpretations.append("실험 대상자의 /i/ 모음의 F2 값은 정상 기준에 비해 높습니다. 이는 혀가 전방화되었음을 의미합니다.")
    elif f2_values[1] - 2290 < -100:
        interpretations.append("실험 대상자의 /i/ 모음의 F2 값은 정상 기준에 비해 낮습니다. 이는 혀가 후방화되었음을 의미합니다.")
    else:
        interpretations.append("/i/ 모음의 F2 값은 정상 범위에 있습니다.")

    # /u/ 모음 F2 값 해석
    if f2_values[2] - 870 > 100:
        interpretations.append("실험 대상자의 /u/ 모음의 F2 값은 정상 기준에 비해 높습니다. 이는 혀가 지나치게 전방화되었음을 의미합니다.")
    else:
        interpretations.append("/u/ 모음의 F2 값은 정상 범위에 있습니다.")

    # /a/ 모음 F1 값 해석
    if f1_values[0] - 730 > 100:
        interpretations.append("실험 대상자의 /a/ 모음의 F1 값은 정상 기준에 비해 높습니다. 이는 혀가 더 낮게 움직였음을 의미합니다.")
    elif f1_values[0] - 730 < -100:
        interpretations.append("실험 대상자의 /a/ 모음의 F1 값은 정상 기준에 비해 낮습니다. 이는 혀가 더 높게 움직였음을 의미합니다.")
    else:
        interpretations.append("/a/ 모음의 F1 값은 정상 범위에 있습니다.")

    # VSA 해석
    vsa_diff = participant_vsa - normal_vsa
    if vsa_diff < -10000:
        interpretations.append(f"실험 대상자의 모음 삼각도 면적은 정상 기준에 비해 {abs(vsa_diff):.2f}만큼 작습니다. 이는 혀의 움직임 범위가 줄어들어 발음의 명확도가 감소할 가능성이 있음을 의미합니다.")
    elif vsa_diff > 10000:
        interpretations.append(f"실험 대상자의 모음 삼각도 면적은 정상 기준에 비해 {vsa_diff:.2f}만큼 큽니다. 이는 혀의 움직임이 증가하여 발음의 명확도가 높아졌음을 의미합니다.")
    else:
        interpretations.append("모음 삼각도 면적(VSA)은 정상 범위에 있습니다.")

    return "\n".join(interpretations)

# 해석 텍스트 추가 (위치 고정 및 왼쪽 정렬, 들여쓰기 적용)
x_pos = 0.125  # x축 위치 (세부 조정)
y_pos = 0.1  # y축 위치 (세부 조정)
interpretation_text = generate_interpretation()
plt.figtext(x_pos, y_pos, interpretation_text, wrap=True, horizontalalignment='left', fontsize=10)

# 그래프 출력 (서브플롯 조정)
plt.subplots_adjust(left=0.105, bottom=0.44, right=0.86, top=0.92, wspace=0.2, hspace=0.2)
plt.show()
