# DRF todoList
그날 수업한 내용은 매일 커밋됩니다.

## ⚙️ 개발 환경

- Python 3.12.3
- Django 5.2.3
- 가상환경: venv 사용

## ▶️ 실행 방법

1. GitHub 저장소 클론
```bash
git clone https://github.com/likelion-python-16/todoList_DRF.git
```

2. 프로젝트 디렉토리로 이동
```bash
cd todoList_DRF
```

3. 가상환경 생성
```bash
python -m venv venv
```

4. Mac/Linux (bash/zsh):
```bash
source venv/bin/activate
```

5. requirements.txt
```bash
pip install -r requirements.txt
```

6. 마이그레이션 (DB 생성)
```bash
python manage.py migrate
```

7. 슈퍼유저 생성 (관리자 페이지용)
```bash
python manage.py createsuperuser
```

8. 서버 실행
```bash
python manage.py runserver
```