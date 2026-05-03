# My First FastAPI Project

## Tech Stack
- **Framework**: Fash API
- **Environment**: venv (Python 가상환경)
- **Tools**: Homebrew, Git

## 4/30 터미널과 Github 연동
1. 터미널 열자마자 해야할 것
- 폴더 이동: cd ~/Desktop/python_ME(파일명)
- 가상환경 활성화: source venv/bin/activate -> 성공 시 줄 맨 앞에 (venv)가 옴
- 서버 실행: uvicorn main:app --reload
- github과 맥의 내용을 동기화시켜서 충돌 방지: git pull origin main

2. VS에서 열심히 코딩하기
- main.py 수정

3. GitHub에 올리기
- Terminal에서 Control+C로 잠깐 서버 종료 (터미널 앱을 종료하는게 아니라서 다시 켜도 여전히 venv, python_ME 안에 있음)
- git add .
- git commit -m "메시지"
- git push
- 위 3가지를 진행하면 수정본이 github에 업로드된다!

## 5/1 FastAPI 구조와 Git 트러블슈팅
1. FastAPI 코드 한줄의 의미
- from fastapi import FastAPI: 사용할 도구 가져오기
- app = FastAPI(): 서버 객체 생성 (집 짓기)
- @app.get("/"): 주소창에 /가 입력되면 아래 함수 실행
- return {"message": "~~~"}: 브라우저에 데이터 전달
- safari에 localhost:8000 치고 들어가면 return값이 뜸.

2. Git 트러블슈팅(온라인과 내 컴퓨터의 기록이 꼬였을 떄 발생하는 전형적인 에러)
- README.md를 깃헙에서 수정해서 발생.. 왠만하면 vs에서 수정하자. git이 vs보다 앞서나가면 이렇게 오류 발생
- git merge --abort: 일단 없던 일로 초기화
- git add .
- git commit -m "~~" : 일단 맥북내용저장
- git pull origin main --no-rebase: github에 있는 내용 맥북으로 가져오기. 이때 영어글자꽉차면 :wq enter
- git push: 다시 깃헙으로 보내기
- 애초에 이런 일이 생기지않도록 README는 VS에서 수정하고, VS키기전에 터미널에서 깃헙이랑 맥 내용 동기화부터 시키자











