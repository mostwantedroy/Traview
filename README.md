# 딥러닝 기반 여행지 추천 서비스

<img src="https://github.com/radiantprism/Traview/blob/master/traview_architecture.PNG">

1. Django 활용 웹앱 백엔드 개발
- Nginx, Gunicorn 활용 WAS 서버 개발
- 어플 서비스를 위한 REST API 개발

2. 여행 리뷰 데이터 기반 NER 모델 개발
- 세계 최대 여행지 리뷰 사이트 TripAdvisor에서 리뷰 데이터 크롤링(Selenium)
- 리뷰 데이터에 존재하는 여행지의 분위기, 가격, 평가 정보를 추출하는 Bi-LSTM 모델 훈련(사전 기반 BIO Tagging)

3. 사용자 취향 맞춤 여행지 추천 시스템 개발
- 방문한 여행지에 대한 추천(협엽 필터링)
- 여행지의 특징 기반 추천(컨텐츠 기반 필터링)

전체 Portfolio : https://github.com/radiantprism/Traview/blob/master/introduction/Project_proposal_Traview.pdf
