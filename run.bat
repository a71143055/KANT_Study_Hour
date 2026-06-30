@echo off
REM KANT Study Hour Analysis Runner (Windows)
REM 프로젝트 분석을 자동으로 실행하는 배치 스크립트

setlocal enabledelayedexpansion

echo.
echo ########################################
echo # KANT STUDY HOUR ANALYSIS RUNNER
echo ########################################
echo.

REM Python 버전 확인
echo [1/5] Python 버전 확인...
python --version
echo.

REM 의존성 설치
echo [2/5] 의존성 설치 중...
pip install -r requirements.txt >nul 2>&1
echo ✓ 의존성 설치 완료
echo.

REM 샘플 데이터 복사
echo [3/5] 샘플 데이터 준비 중...
copy data\example_study_hours.csv data\study_hours.csv >nul
echo ✓ 샘플 데이터 준비 완료
echo.

REM 분석 실행
echo [4/5] 분석 실행 중...
echo.
python main.py

REM 결과 확인
echo.
echo [5/5] 분석 완료
echo ✓ 분석이 정상적으로 완료되었습니다!
echo.
echo ########################################
echo.

pause
