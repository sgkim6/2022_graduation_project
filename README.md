# 2022_graduation_project

프로젝트명 :  네이버 영화평 분석을 활용한 한글 문장 감성 분석기

프로젝트 목표 : 구글에서 개발한 Pre-Trained 모델인 BERT를 기반으로 하는 영화 리뷰 분석기를 개발한다.
네이버에서 제공하는 영화 리뷰 긍정/부정 데이터셋인 NSMC와 자체적으로 크롤링한 최신 영화 리뷰를 학습 데이터로
모델을 훈련시키며, 결과적으로 유저가 어떤 한글 문자열을 입력하면 그 문장이 긍정 문장인지 부정 문장인지 출력하는 프로그램을 개발하는 것이 목표이다.

개발 환경 : Python(TensorFlow4, Django), Sqlite3(유저 입력 데이터 관리)

# 로컬 실행 시 manage.py와 동일한 디렉토리에 모델 폴더(nsmc_model)가 존재해야 함

모델 다운로드 링크 : https://drive.google.com/drive/folders/1-Fcfe73Y6emwbLm9knWlUpGZ3irnBWTJ?usp=sharing

# 실행방법 : 콘솔 - python manage.py runserver
