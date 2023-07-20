# Travelers

## 1. 목표와 기능

### 1.1 목표
- 처음 django 프로젝트를 진행하는 것이며, MVT패턴을 최대한 이해하는 방향으로 구현
- 이 웹사이트의 목표는 사용자간의 여행정보를 주고받고 커뮤니케이션을 할 수 있는 환경 구축
- 이 웹사이트의 기능적 목표는 사용자가 회원가입한 로그인을 통해 게시글을 생성,수정,삭제할 수 있고 각 게시글마다 댓글을 생성,삭제하는 기능을 구현

### 1.2 구현 목표 기능과 진행상황

1. 회원가입(구현완료)
2. 로그인(구현완료)
3. 로그인 데코레이터(구현완료)
4. 게시판 글 작성(구현완료)
5. 게시판 글 목록 출력(구현완료)
6. 게시판 글 상세보기(구현완료)
7. 게시판 글 삭제(구현완료)
8. 게시판 글 수정(구현완료)
9. 게시판 글 조회수(구현완료)
10. 댓글 작성(진행중)
11. 댓글 삭제

## 2. 개발 환경 및 배포 URL
### 2.1 개발 환경
- Django
- html
- css

### 2.2 배포 URL

## 3. 데이터베이스 ERD


![데이터베이스ERD](https://github.com/k2h2j3/Orme_djangoproject/assets/74819625/95091afb-3194-4093-955a-735381fdd837)


## 4. 프로젝트 구조

```bash
myapp
|
|
+---app
|   |
|   +---media
|
+---board
|   |
|   +---migrations
|   |
|   +---templates
|   |   \---board
|
+---home
|   |
|   +---migrations
|   |
|   +---templates
|   |   \---home
|   
|
+---media
|   \---django-summernote
|
+---static
|   +---css
|   |
|   \---img
|
\---user
    |   
    |         
    |
    +---migrations
    |   
    |       
    |
    +---templates
       \---user
```

## 5. UI

1. 비 로그인 상태에서 글 작성 시도시 로그인 페이지로 이동

   
![1](https://github.com/k2h2j3/Orme_djangoproject/assets/74819625/03409500-339f-4226-8d08-ad472433f62f)


2. 회원가입 에러메시지 출력

   
![화면 캡처 2023-07-20 162906](https://github.com/k2h2j3/Orme_djangoproject/assets/74819625/ac356f45-5a5b-4613-a21b-acc6cf8564d3)




![화면 캡처 2023-07-20 162935](https://github.com/k2h2j3/Orme_djangoproject/assets/74819625/8534b88c-7532-4b2e-9cfb-1b4d8df47e83)




3. 로그인


![3](https://github.com/k2h2j3/Orme_djangoproject/assets/74819625/08e446e2-8e05-40f4-a5fb-28b286fb8ac9)


3-1. 로그아웃시 로그인 회원가입 목록이 뜸


![3-1](https://github.com/k2h2j3/Orme_djangoproject/assets/74819625/e906ffd0-270e-45cb-979c-32429a346612)


4. 로그인 상태에서 자유게시판에 글 작성


![4](https://github.com/k2h2j3/Orme_djangoproject/assets/74819625/d767ed6b-27af-49f5-b90f-6e446aed39dd)


5. 이미지 파일 올리기 가능


![5](https://github.com/k2h2j3/Orme_djangoproject/assets/74819625/ed212b2f-5968-43f5-9c58-ba304fde8650)


6.게시글 상세보기기


![6](https://github.com/k2h2j3/Orme_djangoproject/assets/74819625/d9644af4-f227-4917-bf72-150fb09d8b76)


6-1 게시글 수정


![6-1](https://github.com/k2h2j3/Orme_djangoproject/assets/74819625/256dce40-9b68-4def-8903-bc6d4057b8c2)


6-2  게시글 삭제


![6-2](https://github.com/k2h2j3/Orme_djangoproject/assets/74819625/43d4dacf-1f92-4c19-9d80-fb25578f1e21)


7. 조회수 오르는 장면


![7](https://github.com/k2h2j3/Orme_djangoproject/assets/74819625/e7e90977-7a1c-4903-841f-5be3f24966a4)



## 6. 메인 기능
- 회원가입
- 로그인
- 게시글 생성,수정,삭제

## 7. 추가 기능
- 조회수

## 8. 개발하며 배운 점

로그인 기능을 만들 때 생각보다 고려해야할 점이 많다는 것을 느꼈다. 사용자가 입력한 로그인과 비밀번호가 일치하는지, 유효성 검사를 통과했는지도 확인해야하지만 로그인을 성공했을 때, 로그인 세션정보에 어떤 정보를 넣어야할지 고려해야한다. 로그인 세션 정보는 사용자를 나타낼 수 있는 특정성과 유일성을 가진 데이터이어야 하므로 유저의 pk, 아이디, 이메일 주소와 같이 중복되지 않은 데이터로 넣어주었다.<br>
로그인 세션정보는 영구적으로 보관할 수 없다. 서버가 시간이 지날수록 쌓이는 세션정보를 감당할 수 없기 때문이다. 그렇기 떄문에 만료기간도 따로 설정해주어야한다. <br>


![화면 캡처 2023-07-20 165833](https://github.com/k2h2j3/Orme_djangoproject/assets/74819625/e35cef94-62e4-47f6-9841-e1d9ee169f1a)


따라서 로그인함수에 request.session.set_expiry(0) 를 넣어 만료기간을 정해주었다(0을 넣으면 세션쿠키 삭제 + DB에 세션데이터 14일간 유지된다)<br>

로그인에 성공 했을 때, 세션이 생성되는 것을 확인할 있다


![session](https://github.com/k2h2j3/Orme_djangoproject/assets/74819625/28a655cf-b4da-408e-9ea7-42dd38eef745)


로그아웃 기능을 만들 때도 고려해야하는 점이 있다. 로그아웃을 할 때는 로그인을 하기 이전상태로 돌아가게 해야한다. 단순히 session_key만 삭제하는 방법도있다. 브라우저 강제종료를 하는것이 대표적인 예다. 그러나 이 방법은 다른 사용자가 삭제된 session_key값을 알고있으면 접근할 수 있기때문에 보안에 취약하다. 따라서 DB 세션 저장소의 로그인 session에 관한 데이터를 전부 삭제해야한다. django는 이러한 로그아웃 메서드를 가지고 있다.<br>
request.session.clear는 session_data를 초기화해주는 메서드이다.<br>
request.session.flush는 session_data 자체를 지워버린다.(본인은 이 방법을 사용했다.)<br>
이렇게 세션데이터에 대해 이해하게되었고 로그아웃을 할 때 강제종료가 보안성에 취약한지도 알게되었다.

로그인이 진행되는 과정


![로그인세션](https://github.com/k2h2j3/Orme_djangoproject/assets/74819625/4c682183-92d4-4585-ade9-fc36b01348b7)


## 9. 느낀 점

Django 프로젝트를 시작할 때, 처음에는 Model-Template-View 연결도 쉽지않아서 막막했지만 그래도 개념을 어느정도 잡고 진행하면서 여기까지 구현했다는 것에 뿌듯함을 느꼈다. <br>
MTV, 로그인개념, 장고 템플릿문법을 확실하게 짚어서 다음 프로젝트 때는 헤매는 시간을 줄이고 그 줄인 시간만큼 추가 기능구현과 css적용을 해보는것까지 도전해보고싶다.





