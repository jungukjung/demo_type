 ** 타임라인 ** 
 [ 2021-11-26 ] github 연결방법 정리 
 [ 2021-11-26 ] venv 가상환경 설치 
 [ 2021-11-26 ] venv 가상환경 설치방법 
 
 ** github 프로젝트 올리는 방법 **
 0. gitbash 설치  
 1. github에 접속해서 새로운 프로젝트를 생성한다. 
 2. cmd 창을 열어서 - git config --global user.name '이름'                
                    - git config --global user.email 'github email' 입력한다.
 3. 프로젝트를 시작할 폴더 경로를 cmd창으로 접근한다. 
 4. github 사이트에서 생성한 프로젝트 경로를 복사 붙여넣기 해준다.
                    - git clone "복사한 경로" ( 여기까지 하면 해당 폴더와 github가 연결이 됨 )
 5. 임시 파일을 하나 생성해서  연결된 폴더 안에 쏙 집어 넣어준다.
 6. [cmd창에서] git add '해당 파일 이름'
 7. [cmd창에서] git commit -m "저장하면서 적을 내용"   


 ** venv 가상환경 설치 방법 **
 1. vscode에서 cmd 창을 연다.
 2. [cmd창에서] python -m venv '폴더 명'
 3. [cmd창에서] 접속 방법 - cd '폴더명'/Scripts                 
 4. [cmd창에서] Activate 입력 왼쪽에 (폴더명)이 뜬다면 적용 완료
 5. [cmd창에서] 가상환경 빠져 나오기 deActivate  
 