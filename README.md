# 🍀 다회용기 캠페인 후기들이 궁금하다면 용기낸 사람들
![image](https://user-images.githubusercontent.com/55770848/132479866-83b5d1e9-545e-43f4-8a4a-516c0b034aca.png)

![image](https://user-images.githubusercontent.com/55770848/132479981-ef1a9c51-3ec1-4b28-9efa-8d6b5395a3e8.png)



## 프로젝트 소개 🔎

#### 용기 낸 사람들은 다회용기 캠페인과 관련된 사용자 후기 기반 커뮤니티 애플리케이션 입니다.
#### 일회용품을 줄이기 위한 운동으로 '용기내 캠페인'이 유행하고 있습니다.
#### 그러나 혼자서 이러한 캠페인에 참여하기는 쉽지 않습니다.
#### 어떤 크기의 용기를 가져가야 하는지 확실하지 않고 막상 가져가도 가게에서 거절할 수 도 있습니다.

#### 용기 낸 사람들 애플리케이션은 이러한 다회용기 캠페인에 관련된 정보를 어플을 통해 쉽게 찾아볼 수 있도록 기획되었습니다.
#### 사용자는 가게에 대해 다회용기 포장한 경험을 후기로 작성하여 다른 캠페인 참여자와 공유할 수 있고
#### 지도를 활용하여 주변에 다회용기 캠페인에 참여하는 가게들을 볼 수 도 있습니다.
#### 가게 사장님들은 자신의 가게를 어플에 등록하여 다회용기 캠페인과 관련된 공식 정보를 게시 할 수 있습니다.

<br/>

## 시스템 구성도 🖥️
![KakaoTalk_20211106_185103695](https://user-images.githubusercontent.com/55652627/140609866-bcad0030-ddbf-43fb-8b86-308a8ce00ce7.png)

<br/>

## 프로젝트 Server 기술 Stack ⚙️
![python badge](https://img.shields.io/badge/Python-v3.8-4479A1?style=flat-square&logo=Python&logoColor=white)
![django badge](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white)
![mysql badge](http://img.shields.io/badge/MySQL-v8.0.21-4479A1?style=flat-square&logo=MySQL&logoColor=white)
![aws badge](http://img.shields.io/badge/AWS-EC2-FF9900?style=flat-square&logo=AmazonAWS&logoColor=white)
![aws badge](http://img.shields.io/badge/AWS-RDS-blue?style=flat-square&logo=AmazonAWS&logoColor=white)
![aws badge](http://img.shields.io/badge/AWS-S3-red?style=flat-square&logo=AmazonAWS&logoColor=white)

<br/>

### API 명세: https://github.com/Courageous-Developer/courageous-people-server/wiki

![캡처](https://user-images.githubusercontent.com/55652627/140618412-08a29f20-ad4b-4bf7-bc49-2e1c031d3f3b.JPG)

#### 프로젝트 폴더 구성은 account, board, config 총 3개로 나뉘어 있습니다.
#### account는 사용자 인증 관련 API들이며
#### board는 Store 게시판, Review 게시판 관련 API 입니다.
#### config는 공통된 부분과 설정 등이 정의된 폴더입니다.

<br/>

## Server 실행 방법
```
conda create -n "가상환경이름" python=3.8
```
```
conda activate "가상환경이름"
```
```
cd Courageous-Developer-Server
```
```
pip install -r requirements.txt
```
```
cd server
```
```
python manage.py runserver
```
※SERCRET_KEY와 DB 정보등은 base.py에 있는 그대로 사용하지말고 처음 django project 만들때 있던 정보로 넣어주어야 합니다.

<br/>

### Postman을 활용한 API 테스트
```
http://localhost:8000
```
![postman2](https://user-images.githubusercontent.com/55652627/140618647-e5b94b73-d116-4c88-bd0e-f9dbaf64224e.JPG)

