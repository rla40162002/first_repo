# Airbnb Clone
Cloning Airbnb with Python, Django, Tailwind and more...

# 프로젝트를 실행하기 위해서
1. 프로젝트 파일 안 db.sqlite3 삭제

2. pip install --user pipenv

3. pipenv가 설치된 경로를 path에 추가

4. pipenv install

5. pipenv shell

6. python manage.py makemigrations

7. python manage.py migrate

8. admin계정 생성<br>
    python manage.py createsuperuser 
9. Fake Data 생성
    1) python manage.py seed_users --number (생성할 데이터 개수)
    2) python manage.py seed_photos
    3) python manage.py seed_amenities
    3) python manage.py seed_facilities
    4) python manage.py seed_houseRules
    5) python manage.py seed_roomType
    6) python manage.py seed_rooms --number (생성할 데이터 개수)
    7) python manage.py seed_reservations --number (생성할 데이터 개수)
10. python manage.py runserver

# 갖고 있는 기능
* 회원가입
* 메일인증
* 로그인(깃허브, 카카오), 로그아웃
* 사용자 정보 페이지
* 사용자 정보 수정
