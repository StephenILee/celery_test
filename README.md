# celery_test
celery를 이용한 서비스간 통신 테스트

# 필수 패키지 및 컨테이너 설치
## Django
```
# 각 프로젝트별 venv 활성화 상태에서 아래 명령어 실행
$ pip install -r requirements.txt
```

## Redis
```
$ docker run -d -p 6379:6379 redis
```

# 모듈 구동/중지
## server
```
# 시작
$ python manager.py runserver
```

## client
```
# 시작
$ celery -A client worker --loglevel=info --detach

# 종료
$ pkill -f "client worker"
```

# 테스트
```
$ curl -XPOST http://localhost:8000/foo/index -H 'Content-Type: application/json' -d '{"x": 1, "y":29}' -w "%{http_code}"
```
