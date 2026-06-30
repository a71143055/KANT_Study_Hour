#!/bin/bash
# KANT Study Hour Analysis Runner
# 프로젝트 분석을 자동으로 실행하는 스크립트

echo "########################################"
echo "# KANT STUDY HOUR ANALYSIS RUNNER"
echo "########################################"
echo ""

# Python 버전 확인
echo "[1/5] Python 버전 확인..."
python --version
echo ""

# 의존성 설치
echo "[2/5] 의존성 설치 중..."
pip install -r requirements.txt > /dev/null 2>&1
echo "✓ 의존성 설치 완료"
echo ""

# 샘플 데이터 복사
echo "[3/5] 샘플 데이터 준비 중..."
cp data/example_study_hours.csv data/study_hours.csv
echo "✓ 샘플 데이터 준비 완료"
echo ""

# 분석 실행
echo "[4/5] 분석 실행 중..."
echo ""
python main.py
RESULT=$?
echo ""

# 결과 확인
echo "[5/5] 분석 완료"
if [ $RESULT -eq 0 ]; then
    echo "✓ 분석이 정상적으로 완료되었습니다!"
else
    echo "✗ 분석 중 오류가 발생했습니다. (코드: $RESULT)"
fi
echo ""
echo "########################################"
