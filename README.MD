# TIL (Today I learned)  
  
==================================

# 250901
- lily llm rag 시스템 ocr 연동 확장

# 250831
- 컨텍스트 메모리 요약 전용 llm 모델 교체 테스트 

# 250830
- 안드로이드 apk 리패키징, 릴리즈 버전 fix, css fix, 라이브러리 의존성 문제 fix

# 250829
- app store 등록 준비 및 테스트

# 250828 v0.99.5
- android apk package build complete, adb 연결, deubg & release virsion test

# 250827
- cloudflare, freedns, duckdns, 서브도메인 매핑, netlify-github 연동 reverse proxy 시도

# 250826
- cloudtype migrate, supabase db 연결 계층적 메모리 테스트
- 로컬 db postgrsql 추가

# 250825
- lily 컨텍스트 메모리 supabase 데이터베이스 연결

# 250824
- 계층적 메모리 구조 통합 리팩토링, 장기, 중기, 단기

# 250823
- 컨텍스트 매니저, lora, rag 시스템, 문서 요약 + 컨텍스트 확장 시스템 통합 

# 250822
- polyglot 1.3b lora 파라메터 조절, 응답 품질 향상

# 250821
- polyplot 5.8b 응답 속도 개선, 모델별 tokenizer config settings json 변수 명시적으로 기입

# 250820
- lily llm kanana 3b 멀티모달 개선, polyglot 1.3b, 5.8b 응답 품질 개선

# 250818 v0.99.31
- media 파일 serve 문제 해결, 화상 채팅 기능 개선, 모바일 화면 개선

# 250818
- 배열 강제 코드의 적용 범위 조절, 웹소켓 메시지 출력 순서 꼬임 문제 해결, 로컬서버 내부 IP 기기 테스트 모드 개선, 커스텀 회원가입 뷰 추가, 이미지 다중 첨부 오류 수정, 즐겨찾기 오류 수정

# 250817
- 서버 이전 작업 및 기능 추가, 모듈 분리 등으로 인한 오류들 fix, 부분 리팩토링링

# 250816
- fly io migrations 완료, 메인 앱과 redis 서버는 nrt(도쿄), postgres db 서버는 syd(시드니(호주))

# 250815 v0.99.2
- fly io migrations, redis 서버 분리, 4개 서버 각각 환경별 테스트, redis tls off test -> success

# 250814
- render github ci/cd 에서 배포방식 변경경(github actions, dockerhub image import), fly.io 서버 이전

## 250813
- 1:1 화상채팅 p2p 웹소켓 연결, 테스트 완료. 

## 250812
- camera 목록 출력, 기존 webcam 외에 가상카메라나 아바타 화면 등 출력 가능, globalinput 입력창 카메라 촬영 후 자르기 선택 박스 수정(react-easy-crop -> react-image-crop)

# 250811
- hearth chat railway 서버 + render 서버 추가 마이그레이션, 자동 ci/cd 파이프라인 추가

# 250810
- modeling 과 app_v2.py 리팩토링으로 cpu 환경에서 hearth chat 에서 전송한 메시지의 fast api 응답시간 620초 -> 30초 감소

## 250809
- 허깅페이스 fast_api 서버와 연결, fallback 문제 해결

# 250808
- FAST API 리팩토링 : HEARTH CHAT 통합 서비스 안정화 목표

# 250807
- 허깅페이스 Gradio 멀티모달 AI 파일첨부 시 '무한 로딩' 현상 디버깅

# 250806
- langchain system, lag system, 문서 기반 텍스트 검색, LaTeX-OCR

# 250805
- hearth chat 사이트 AI 선택 옵션에 Lily LLM 모델 추가, Lily LLM 멀티모달 이미지, PDF, DOC 응답 테스트

# 250804
- kanana b3 모델링 전체 리팩토링 후 텍스트 처리 시간 감소, 이미지 처리 속도 증가(cpu 환경)

# 250803
- 멀티모달 다중 이미지 테스트, glob, pillow image 사용해서 첨부한 다중 이미지 파일리스트 작성 후 처리, 혹은 db 경로 참조

# 250802 
- 멀티모달 이미지+텍스트 테스트 generate 함수 중복 호출 수정, 동기-비동기 구조 개선

## 250801
- Kanana-1.5-v-3b-instruct image-to-text generate 모델, 멀티모달(이미지+텍스트) 응답 확인

## 250731 
- 프로필 로직 변경 후 kanana-v-3b-instruct 추가 테스트, 비동기 로직 제거, 응답 속도 향상

## 250730
- parameter finetuning, training 반복 및 test, 카카오톡 AI 모델 kanana-1.5-v-3b-instruct, kanana-1.5-2.1b-instruct-2505, kanana-nano-2.1b-instruct 추가

## 250729 
- LLM Project(Lily Generate), Mistral-7B Base, EleutherAIpolyglot-ko-1.3b, KoAlpaca-Polyglot-5.8B, DialoGPT-medium-0.8GB 모델 추가

## 250728
- 소셜 로그인 단계 간략화, utility 함수 컴포넌트 사용(코드 재사용성 향상, 하드코딩 리팩토링), AI API 문서 parsing 출력 구조화

## 250727 
- 메시지 코드 Virtuoso 방식으로 전체 리팩토링 (백엔드 API 포함), 무한 스크롤 문제 해결

## 250726
- 관리자 페이지 미디어 파일 멀티 삭제, 썸네일 모달창, 페이지네이션 추가

## 250725
- media 파일 추가 시 별도 정적 파일 서버/스토리지 사용, 관리자 페이지 미디어 파일 업로드, 파일 목록 관리 탭 추가

## 250724 
- 가상화 메시지 react-virtuoso 로 리팩토링 : react-virtual 에서 DOM 에서 estimate 요소를 찾지 못하는 문제

## 250723 
- 가상화 메시지 react-virtual + ResizeObserver 으로 리팩토링 : react-window 메시지 중첩 문제

## 250722 
- pmx2vrm 아바타 모형 추가, 인터넷 배포 pmx 파일의 경우 커스텀 모델로 추가 확장 가능, 아바타 pose 리셋  

## 250721 v0.92  
- 이미지 첨부 문제 해결, css 리뉴얼, app.js 전역 함수 리팩토링 

## 250720  
- 메시지 입력창 전역으로 변경, 대화방 상태가 아니라도 입력창에 메시지 입력후 전송 시 AI 질문 자동 답변 진행, 입력창 왼쪽에 새로운 대화방 개설 버튼 추가, short 클릭 시 자동 개설, long 시 대화방 개설 모달창

## 250719  
- headerBar title 출력 문제 해결 -> app.js 전역 관리 fetch 로 setRoomId 갱신

## 250718
- virtualized message 구현을 위해 채팅창 리뉴얼, autosize 로 부모창의 사이즈 자동감지해서 가상화 메시지 창 제어, 검색 결과창 즐겨찾기 연동

## 250717 v0.8
- 검색 속도 향상을 위한 db 로직 개선, 지연시간 조절, csrf 인증 문제 해결

## 250716 v0.7 
- css 리뉴얼, 목록 사이드바, 검색창, 알림 메뉴 추가, 회원탈퇴, 정규식 검색, 검색 결과 하이라이트 애니메이션 효과 추가

## 250715
- 설정창 오류 수정, railway 실시간 채팅 환경 테스트  

## 250714
- 실시간 양방향 전송 websocket 구현을 위해 ubuntu(wsl) redis-server 구동, 설정 창 추가, AI 응답기능 ON/OFF 추가

## 250713 v0.6
- 대화방 기능 추가, 개인, 공개 모드, 1:1, AI 채팅, 그룹 화상(or 아바타) 채팅 모드 

## 250712  
- 이메일, 소셜 계정(구글. 카카오, 네이버, Github) 가입, 로그인, 계정 연동

## 250711  
- mount 용 로컬 doker image 생성, 아바타 ON/OFF 모드 추가, 페이지 로드 설계 리팩토링, 마크다운, LaTex, Charts 적용

## 250710  
- 이미지+텍스트 멀티모달 응답 기능 추가, 수신 정상 확인, Railway 서버 구동 (url : https://hearthchat-production.up.railway.app)

## 250709  
- CSS 리팩토링, TTS 기능 보강, 채팅 로그에 날짜 시간 표시, 이미지 첨부 버튼 추가, 이미지 첨부 후 전송 시 채팅로그에 출력  

## 250708
- 음성인식, 사용자 3D 아바타 트래킹 구현, CSS 리팩토링, TTS 기능 보강  

## 250707  
- vrm 모델 세팅 - vroid, vmagicmirror, warudo 작동법 숙지 -> hearth chat 에 모델 컨버팅, 음성인식 기능 추가  

## 250706 
- glb 모델 아바타 적용, 감정 포착 코드 삭제, gemini 에 TTS 적용

## 250706 
- 감정 포착 코드 삭제, TTS 적용, glb 모델 아바타 적용 -> 표정 인식 확인  

## 250705  
- google gemini api 로 변경, LLM AI 채팅 베이스 완성, 실시간 대화 내역 DB에 저장 추가 

## 250704  
- AI 채팅 프로젝트, django 보일러 세팅, open ai api 

## 250703  
- 메이커스 모델링 stl 파일 3d 프린터 출력 확인  

# 250702  
- arduino 프로젝트 정리 및 포트폴리오 작성, TOEIC HACKERS 기출 테스트    

# 250701  
- arduino 프로젝트 최종 마무리, SW 코딩자격 1급 예상 문제 회독    

# 250630  
- arduino 자이로스코프 센서, 및 온도/습도 센서 종합 테스트 및 프론트 출력 테스트, SQL 서버 테스트    

# 250629  
- arduino hurskey lens test : 탐색 한계, 정확도, threshold 테스트  

# 250628  
- AICE 정리, sns.get_dataset_names(), .data_loadset() 이용해서 필요한 데이터 로딩(분류:'titanic'(생존자 분류) / 회귀:'diamonds'(가격 예측))  

## 250627  
- AICE 샘플 테스트 / arduino - mblock 연동 시 milli() 함수로 비동기 구현  

# 250626  
- ML XGBoost LightGBM / DL callbacks, history, best_model  

# 250625  
- AICE TEST 샘플문항 풀이 연습 : 전처리, ML, DL

# 250624  
- 자동차 과속/주차 경고음, 아날로그 슬라이드 센서(0~1023)-OLED 연동, SONAR(0~1023) 센서와 FND 연동  

# 250622  
- AICE, 정처기 실기 기출 정리, SCRATCH ADUINO mega 2356 블록코딩

## 250621  
- 빅데이터 실기 모의 다시 - 합동분산 추정량, ttest_ind, f-검정, scipy.stat 이용 -> help, dir  

## 250620  
- 빅데이터 실기 기출변형 3~6회 : 등분산성 levene(), 정규성 shapiro(), 독립성 검정 chi2_contingency(), 적합도 검정 chisqure()  
  
## 250619 
빅데이터분석기사 실기 대비 : 데이터구름 예제 복습 : 유형1~유형3, 회귀 유의한 or 유의하지 않은 변수 선택에 따른 상수항 추가/제외  

## 250618  
빅데이터분석기사 실기 대비 : 데이터구름 예제 복습 : 유형1~유형3, 다중분류 데이터 불균형에 따른 stratify 사용여부 판단   
  
## 250617  
빅데이터분석기사 실기 대비 : 유형1-유형3 캐글 데이터 분석 문제 - get_dummies() X_train, X_test 컬럼수 차이 문제 해결()  
  
## 250616  
빅데이터분석기사 실기 대비 : 전처리 100문제 - 이상치 처리, IQR, ANOVA 분산, 비정규성 윌콕슨  
  
## 250615  
빅데이터분석기사 실기 대비 : 유형3 분석 - f검정 t검정, 합동분산, p-value, ttest_ind(), 유형 1 분석 - 전처리, 결측치 제거, 4분위수 (quntaile)  
  
## 250614  
빅데이터분석기사 실기 대비 : 유형2 실기 문제풀이 - 데이터 전처리, 훈련, 모델 성능 테스트, 랜덤포레스트 적용  
  
## 231028  
프로젝트 개선점 탐구, 개선점 적용, 반성점 기재, 토이 프로젝트 구상  
  
## 230926  
SQL LOAD_FILE()  
  
## 230925  
SQL  
  
## 230924  
python  
  
## 230923  
python  
  
## 230922  
SQL UPDATE, INSERT, SELECT, GROUP BY, ORDER BY, HAVING, SQL JOIN  
  
## 230921  
0910~1800 취업특강 : 학과 습, 개발자에게 유용한 각종 사이트와 툴, bootstrap  
1900-2300 git 충돌관련 예제 study  
