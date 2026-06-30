# Setup Guide - KANT Study Hour Analysis

프로젝트 설정 및 실행 가이드입니다.

## 빠른 시작 (Quick Start)

### 1. 환경 설정

```bash
# 프로젝트 디렉토리로 이동
cd KANT_Study_Hour

# 가상 환경 생성 (선택사항이지만 권장)
python -m venv venv

# 가상 환경 활성화
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 필요한 패키지 설치
pip install -r requirements.txt
```

### 2. 데이터 준비

#### Option A: 예제 데이터로 테스트
```bash
# 예제 데이터로 이름을 변경하여 실행
cp data/example_study_hours.csv data/study_hours.csv
python main.py
```

#### Option B: 직접 데이터 준비
1. `data/study_hours.csv` 파일 생성
2. 다음 형식으로 데이터 입력:
   ```
   student_id,name,study_hours,subject
   1,Name,7.5,Subject
   ...
   ```

### 3. 분석 실행

```bash
python main.py
```

## 데이터 형식

필수 컬럼:
- `study_hours`: 숫자형 (float or int)

선택 컬럼:
- `student_id`: 학생 ID
- `name`: 학생 이름
- `subject`: 과목

## 예상 출력

```
##################################################
# KANT STUDY HOUR ANALYSIS
##################################################

✓ Data loaded successfully from data/study_hours.csv

==================================================
DATA STRUCTURE ANALYSIS
==================================================

📊 Shape: (15, 4)
   Rows: 15, Columns: 4

📋 Data Types:
student_id      int64
name           object
study_hours   float64
subject        object
dtype: object

👀 First 5 rows:
   student_id        name  study_hours      subject
0           1  Kim Min-jun           5.5  Mathematics
...
```

## 문제 해결 (Troubleshooting)

### "File not found" 에러
- `data/study_hours.csv` 파일이 존재하는지 확인
- 파일 경로가 올바른지 확인

### "Column not found" 에러
- CSV 파일에 `study_hours` 컬럼이 있는지 확인
- 컬럼명이 정확히 `study_hours`인지 확인

### 패키지 설치 실패
```bash
# pip 업그레이드
python -m pip install --upgrade pip

# 다시 설치
pip install -r requirements.txt
```

## 커스터마이징

`config.py`에서 설정을 수정할 수 있습니다:

```python
# 데이터 경로 변경
DATA_PATH = 'custom_data.csv'

# 분석 기준값 변경 (예: 8시간 이상)
STUDY_HOUR_THRESHOLD = 8

# 열 이름 변경
STUDY_HOUR_COLUMN = 'hours'
```

그 후 `main.py`를 실행합니다.

## 추가 정보

- 더 자세한 정보는 README.md를 참조하세요
- 문제 발생 시 issue를 제출해주세요
