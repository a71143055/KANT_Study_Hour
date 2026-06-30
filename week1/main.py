import pandas as pd
import numpy as np
import os


# ========================
# 기능 1: 데이터 불러오기
# ========================
def load_data(file_path):
    """
    CSV 파일을 불러와 DataFrame으로 반환합니다.
    
    Parameters:
    -----------
    file_path : str
        로드할 CSV 파일 경로
    
    Returns:
    --------
    pd.DataFrame
        불러온 데이터 프레임
    """
    if not os.path.exists(file_path):
        print(f"❌ 오류: '{file_path}' 파일을 찾을 수 없습니다.")
        exit()
    
    try:
        df = pd.read_csv(file_path, encoding="utf-8-sig")
        print(f"✓ 데이터 로드 완료: {df.shape[0]}행 × {df.shape[1]}열")
        return df
    except UnicodeDecodeError:
        print("❌ 인코딩 오류: utf-8-sig로 실패, cp949로 재시도합니다.")
        df = pd.read_csv(file_path, encoding="cp949")
        print(f"✓ 데이터 로드 완료: {df.shape[0]}행 × {df.shape[1]}열")
        return df


# ========================
# 기능 2: 데이터 구조 확인
# ========================
def explore_structure(df):
    """
    DataFrame의 기본 구조를 파악하고 출력합니다.
    
    Parameters:
    -----------
    df : pd.DataFrame
        분석할 데이터 프레임
    """
    print("\n" + "="*60)
    print("[ 데이터 구조 확인 ]")
    print("="*60)
    
    # 1. 행/열 수
    print(f"\n📊 데이터 크기")
    print(f"  - 행(Row) 수: {df.shape[0]}개")
    print(f"  - 열(Column) 수: {df.shape[1]}개")
    
    # 2. 컬럼명 및 자료형
    print(f"\n📋 컬럼명 및 자료형")
    print(df.dtypes.to_string())
    
    # 3. 상위 5행
    print(f"\n👀 상위 5행 데이터")
    print(df.head().to_string())
    
    # 4. 추가 정보
    print(f"\n📌 추가 정보")
    print(df.info())


# ========================
# 기능 3: 기술통계 출력
# ========================
def show_statistics(df):
    """
    수치형 컬럼의 기술통계를 출력합니다.
    
    Parameters:
    -----------
    df : pd.DataFrame
        분석할 데이터 프레임
    """
    print("\n" + "="*60)
    print("[ 기술통계 ]")
    print("="*60)
    
    print("\n📈 기술통계 요약")
    print("  - count: 결측치를 제외한 데이터 개수")
    print("  - mean: 평균값")
    print("  - std: 표준편차 (데이터가 평균에서 얼마나 흩어져 있는지)")
    print("  - min: 최솟값")
    print("  - 25%/50%/75%: 사분위수 (25%, 50%, 75% 기준값)")
    print("  - max: 최댓값")
    
    print("\n📊 기술통계 테이블")
    print(df.describe().to_string())
    
    # 각 컬럼의 평균값
    print("\n🔢 컬럼별 평균값")
    numeric_df = df.select_dtypes(include="number")
    for col in numeric_df.columns:
        mean_val = df[col].mean()
        print(f"  - {col:20s}: {mean_val:8.4f}")


# ========================
# 기능 4: 결측치 현황 파악
# ========================
def check_missing(df):
    """
    각 컬럼의 결측치 수와 비율을 계산하고 심각도를 표시합니다.
    
    Parameters:
    -----------
    df : pd.DataFrame
        분석할 데이터 프레임
    
    Returns:
    --------
    dict
        컬럼별 결측치 정보를 담은 딕셔너리
    """
    print("\n" + "="*60)
    print("[ 결측치(Missing Value) 현황 ]")
    print("="*60)
    
    missing_dict = {}
    total_rows = len(df)
    
    print(f"\n결측치 심각도 기준:")
    print(f"  - 낮음: 5% 미만")
    print(f"  - 주의: 5% 이상 ~ 20% 미만")
    print(f"  - 높음: 20% 이상")
    
    print(f"\n📊 컬럼별 결측치 현황")
    has_missing = False
    
    for col in df.columns:
        missing_count = df[col].isnull().sum()
        
        # 결측치가 없으면 건너뜀
        if missing_count == 0:
            continue
        
        has_missing = True
        missing_ratio = (missing_count / total_rows) * 100
        
        # 심각도 판정
        if missing_ratio < 5:
            severity = "낮음"
        elif missing_ratio < 20:
            severity = "주의"
        else:
            severity = "높음"
        
        missing_dict[col] = {
            "count": missing_count,
            "ratio": missing_ratio,
            "severity": severity
        }
        
        print(f"\n  [{col}]")
        print(f"    - 결측치 수: {missing_count}개")
        print(f"    - 결측치 비율: {missing_ratio:.2f}%")
        print(f"    - 심각도: {severity}")
    
    if not has_missing:
        print("\n✓ 결측치가 없습니다.")
    
    return missing_dict


# ========================
# 기능 5: NumPy로 통계량 계산
# ========================
def numpy_stats(df, column):
    """
    NumPy를 사용하여 직접 통계량을 계산합니다.
    
    Parameters:
    -----------
    df : pd.DataFrame
        분석할 데이터 프레임
    column : str
        대상 컬럼명
    """
    print("\n" + "="*60)
    print(f"[ NumPy 통계량 계산: {column} ]")
    print("="*60)
    
    # 결측치 제거 후 NumPy 배열로 변환
    arr = df[column].dropna().values
    
    print(f"\n📐 NumPy 함수로 직접 계산")
    
    # 평균
    mean_val = np.mean(arr)
    print(f"  - 평균 (np.mean): {mean_val:.4f}")
    
    # 표준편차 (표본표준편차, ddof=1 사용)
    std_val = np.std(arr, ddof=1)
    print(f"  - 표준편차 (np.std, ddof=1): {std_val:.4f}")
    
    # 중앙값
    median_val = np.median(arr)
    print(f"  - 중앙값 (np.median): {median_val:.4f}")
    
    # 최솟값
    min_val = np.min(arr)
    print(f"  - 최솟값 (np.min): {min_val:.4f}")
    
    # 최댓값
    max_val = np.max(arr)
    print(f"  - 최댓값 (np.max): {max_val:.4f}")
    
    # pandas와 비교
    print(f"\n📊 pandas describe() 결과와 비교")
    describe_result = df[column].describe()
    print(f"  - pandas 평균: {describe_result['mean']:.4f} (NumPy: {mean_val:.4f})")
    print(f"  - pandas 표준편차: {describe_result['std']:.4f} (NumPy: {std_val:.4f})")
    
    # 조건 필터링: 6시간 이상
    if column == "study_hours":
        count_above_6 = len(arr[arr >= 6])
        percentage = (count_above_6 / len(arr)) * 100
        print(f"\n🎯 조건 필터링 결과 ({column})")
        print(f"  - 6시간 이상 공부하는 학생: {count_above_6}명 ({percentage:.2f}%)")


# ========================
# 메인 함수
# ========================
def main():
    """
    모든 기능을 순서대로 실행하는 메인 함수입니다.
    """
    print("\n" + "="*60)
    print("[ 과제 1: 데이터 불러오기 및 기초 탐색 ]")
    print("="*60)
    
    # 파일 경로 상수
    FILE_PATH = "data/student_habits.csv"
    
    # 기능 1: 데이터 불러오기
    df = load_data(FILE_PATH)
    
    # 기능 2: 데이터 구조 확인
    explore_structure(df)
    
    # 기능 3: 기술통계 출력
    show_statistics(df)
    
    # 기능 4: 결측치 현황 파악
    missing_info = check_missing(df)
    
    # 기능 5: NumPy로 통계량 계산
    numpy_stats(df, "study_hours")
    
    print("\n" + "="*60)
    print("[ 분석 완료 ]")
    print("="*60)
    print("\n✓ 모든 분석이 완료되었습니다!")


# ========================
# 프로그램 실행
# ========================
if __name__ == "__main__":
    main()
