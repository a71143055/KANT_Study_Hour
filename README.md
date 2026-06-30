# KANT Study Hour Analysis

학생들의 공부 시간을 분석하는 데이터 분석 프로젝트입니다.

## Project Overview

This project analyzes student study hour patterns using pandas and NumPy.

## Project Structure

```
KANT_Study_Hour/
├── main.py                 # Main analysis script
├── data/
│   └── study_hours.csv    # Study hours dataset (to be added)
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation
```

## Analysis Flow

```
main()
  ↓
데이터 불러오기 (load_data)
  ↓
데이터 구조 확인 (explore_structure)
  ├── shape
  ├── dtypes
  └── head
  ↓
기술통계 출력 (show_statistics)
  ↓
결측치 현황 파악 (check_missing)
  ├── 컬럼별 결측치 수
  └── 결측치 비율 (%)
  ↓
NumPy 통계량 계산 (numpy_stats)
  ├── 평균, 표준편차, 중앙값, 최솟값, 최댓값
  └── 조건 필터링 (6시간 이상 공부하는 학생 수)
  ↓
결과 출력 종료
```

## Features

- **Data Loading**: Load study hours data from CSV
- **Data Exploration**: Check shape, data types, and preview
- **Descriptive Statistics**: Display summary statistics
- **Missing Data Analysis**: Identify and report missing values
- **NumPy Statistics**: Calculate mean, std dev, median, min/max
- **Conditional Filtering**: Count students studying 6+ hours

## Requirements

- Python 3.7+
- pandas >= 1.3.0
- numpy >= 1.21.0

## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. Prepare your data file at `data/study_hours.csv`
2. Run the analysis:

```bash
python main.py
```

## Data Format

Your CSV file should include a column named `study_hours` containing the number of hours studied.

Example:
```
student_id,name,study_hours
1,Student A,5.5
2,Student B,7.2
3,Student C,6.0
...
```

## Output

The script outputs:
- Data structure information (shape, types, preview)
- Descriptive statistics
- Missing data summary
- NumPy statistics (mean, std dev, median, min, max)
- Number of students studying 6+ hours

## Functions

### `load_data(filepath='data/study_hours.csv')`
Loads CSV data from the specified filepath.

### `explore_structure(df)`
Displays data shape, types, and first 5 rows.

### `show_statistics(df)`
Shows descriptive statistics for all numeric columns.

### `check_missing(df)`
Identifies and reports missing values by column.

### `numpy_stats(df, study_hour_column='study_hours', threshold=6)`
Calculates NumPy statistics and filters students by study hour threshold.

### `main()`
Orchestrates the complete analysis workflow.

## Author

a71143055

## License

MIT License
