import pandas as pd
import numpy as np
from pathlib import Path


def load_data(filepath='data/study_hours.csv'):
    """
    데이터 불러오기
    Load study hours data from CSV file
    """
    try:
        df = pd.read_csv(filepath)
        print(f"✓ Data loaded successfully from {filepath}")
        return df
    except FileNotFoundError:
        print(f"✗ Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"✗ Error loading data: {e}")
        return None


def explore_structure(df):
    """
    데이터 구조 확인
    Explore and display data structure
    """
    print("\n" + "="*50)
    print("DATA STRUCTURE ANALYSIS")
    print("="*50)
    
    print(f"\n📊 Shape: {df.shape}")
    print(f"   Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    
    print(f"\n📋 Data Types:")
    print(df.dtypes)
    
    print(f"\n👀 First 5 rows:")
    print(df.head())


def show_statistics(df):
    """
    기술통계 출력
    Display descriptive statistics
    """
    print("\n" + "="*50)
    print("DESCRIPTIVE STATISTICS")
    print("="*50)
    print(df.describe())


def check_missing(df):
    """
    결측치 현황 파악
    Check and display missing data information
    """
    print("\n" + "="*50)
    print("MISSING DATA ANALYSIS")
    print("="*50)
    
    missing_count = df.isnull().sum()
    missing_percent = (df.isnull().sum() / len(df)) * 100
    
    missing_df = pd.DataFrame({
        'Column': missing_count.index,
        'Missing_Count': missing_count.values,
        'Missing_Percent': missing_percent.values
    })
    
    print(missing_df.to_string(index=False))
    
    total_missing = df.isnull().sum().sum()
    if total_missing == 0:
        print("\n✓ No missing values found!")
    else:
        print(f"\n⚠ Total missing values: {total_missing}")


def numpy_stats(df, study_hour_column='study_hours', threshold=6):
    """
    NumPy 통계량 계산
    Calculate statistics using NumPy and filter by study hours threshold
    
    Parameters:
    -----------
    df : DataFrame
    study_hour_column : str
        Column name containing study hours
    threshold : int
        Minimum study hours threshold (default: 6)
    """
    print("\n" + "="*50)
    print("NUMPY STATISTICS")
    print("="*50)
    
    if study_hour_column not in df.columns:
        print(f"✗ Error: '{study_hour_column}' column not found")
        return
    
    study_data = df[study_hour_column].dropna().values
    
    print(f"\n📈 Statistics for '{study_hour_column}':")
    print(f"   Mean: {np.mean(study_data):.2f}")
    print(f"   Std Dev: {np.std(study_data):.2f}")
    print(f"   Median: {np.median(study_data):.2f}")
    print(f"   Min: {np.min(study_data):.2f}")
    print(f"   Max: {np.max(study_data):.2f}")
    
    # 조건 필터링: 6시간 이상 공부하는 학생 수
    students_above_threshold = np.sum(study_data >= threshold)
    total_students = len(study_data)
    percentage = (students_above_threshold / total_students) * 100
    
    print(f"\n🎓 Students studying {threshold}+ hours:")
    print(f"   Count: {students_above_threshold} out of {total_students}")
    print(f"   Percentage: {percentage:.1f}%")


def main():
    """
    Main execution function
    """
    print("\n" + "#"*50)
    print("# KANT STUDY HOUR ANALYSIS")
    print("#"*50)
    
    # 1. 데이터 불러오기
    df = load_data('data/study_hours.csv')
    if df is None:
        print("\n✗ Analysis stopped: Unable to load data")
        return
    
    # 2. 데이터 구조 확인
    explore_structure(df)
    
    # 3. 기술통계 출력
    show_statistics(df)
    
    # 4. 결측치 현황 파악
    check_missing(df)
    
    # 5. NumPy 통계량 계산
    numpy_stats(df, study_hour_column='study_hours', threshold=6)
    
    # 6. 결과 출력 종료
    print("\n" + "#"*50)
    print("# ANALYSIS COMPLETE")
    print("#"*50 + "\n")


if __name__ == "__main__":
    main()
