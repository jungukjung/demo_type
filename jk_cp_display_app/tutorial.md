 ** 타임라인 ** 
 ** https://fontawesome.com/v5.15/icons?d=gallery&p=2 == > lcon site
 [ 2021-11-26 ] [github] 연결방법 정리 
 [ 2021-11-26 ] [venv]   가상환경 설치 
 [ 2021-11-26 ] [venv]   가상환경 설치방법 
 [ 2021-11-26 ] [venv]   가상환경에 pip 파일을 설치하기 전 준비단계 
 [ 2021-11-26 ] [django] 설치 ! 
 [ 2021-11-27 ] [django] 새로운 프로젝트 생성 및 실행
 [ 2021-11-27 ] [django] 초기 html 적용순서
 [ 2021-11-27 ] [django] startapp 생성방법
 [ 2021-11-27 ] [django] startproject 와 startapp 연결방법 
 [ 2021-11-27 ] [django] css,js,fonts,외부파일 분리하기  
 [ 2021-11-27 ] [django] [util.css참조] css 약어로 간소화 
 [ 2021-11-27 ] [django] [side_bar] 만들기  - > html 파일 생성 
 [ 2021-11-27 ] [django] [side_bar] 만들기  - > 상단 로고, 회사명, 반전 스위치 생성 
 [ 2021-11-28 ] [django] [side_bar] 만들기  - > 메뉴 등록 , 메뉴마다 아이콘 생성, 배치 조정 
 [ 2021-11-29 ] [django] [side_bar] 만들기  - > 메뉴바 숨김 상태일 때 생성, 숨겨질 때 나올 때 js 작동 완료 
 [ 2021-11-29 ] [django] [side_bar] 만들기  - > js -- > ts로 업글 
 [ 2021-11-29 ] [django] [side_bar] 만들기  - > 슬라이드 효과 적용 ! 

 

 [[ 2021-11-26 ] github 연결방법 정리]
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


 [[ 2021-11-26 ] venv 가상환경 설치 , [ 2021-11-26 ] venv 가상환경 설치방법]
 ** venv 가상환경 설치 방법 **
 1. vscode에서 cmd 창을 연다.
 2. [cmd창에서] python -m venv '폴더 명'
 3. [cmd창에서] 접속 방법 - cd '폴더명'/Scripts                 
 4. [cmd창에서] Activate 입력 왼쪽에 (폴더명)이 뜬다면 적용 완료
 5. [cmd창에서] 가상환경 빠져 나오기 deActivate  


[ [ 2021-11-26 ] venv 가상환경에 pip 파일을 설치하기 전 준비단계 ]
 ** 본격적인 가상환경 안에 파일을 설치 하기전 준비단계 **
 1. [cmd창에서] pip list 입력하여 현재 설치된 pip 파일들을 확인한다.
 2. [cmd창에서] 입력 후 [ You should consider upgrading via the 
                        'c:\users\wjddn\onedrive\바탕 화면\demo_type\total_lib_box\scripts\python.exe -m pip install --upgrade pip' command. ]
                        이러한 문구가 뜬다면 [cmd창에서] pip install --upgrade pip 입력을 한 후 다시 pip list을 입력해 보자 ( 문구가 사라져 있음 )


[ [ 2021-11-26 ] django 설치 !]
** 장고 설치 **
1. [cmd창에서] 가상환경에서 pip install Django 입력 후 잘 깔렸는지 pip list로 확인해 보자


[ [ 2021-11-27 ] django 새로운 프로젝트 생성 및 실행 ]
** django 새로운 프로젝트 생성 및 실행 **
1. 가상환경 폴더 밖으로 빠져 나온다 [..cd]
2. django-admin startproject '생성할 프로젝트 이름'
3. 생성된 폴더로 접근한다 [정확이는 manage.py 파일이 있는 폴더까지 접근한다, 
                           여기서 manage.py 파일은 django 파일을 실행시키기 위한 스위치 같은 기능을 가지고 있다.]
4. python manage.py runserver 입력 후 나온 [http://127.0.0.1:8000/] 주소 창을 인터넷 창에 입력하고 접근해 본다.
                                           [The install worked successfully! Congratulations! 문구가 뜬다면 성공 ! ]


[ [ 2021-11-27 ] django 초기 html 적용순서 ]
**[django] 초기 html 적용순서 **
1. 최상위 위치에서 templates 폴더를 생성한다.
2. 기본 base가 될  html 파일을 생성한다. 
3. project 폴더에 있는 settings.py 파일을 열고 [ TEMPLATES = [] ] 구간에 있는 곳에서 생성한 templates 폴더 경로를 적어준다.
                                                                            - os.path.join(BASE_DIR,'templates') 적어주기 

[ [ 2021-11-27 ] [django] startapp 생성방법 ]
** [django] startapp 생성방법 **
1. django-admin startapp '생성할 폴더이름'
2. [생성한 폴더] 안에 urls.py 만들어주기   -- > 해당 폴더가 가지고 있는 역활 갯 수
                                           -- > path('view/  [이동할 경로]',total_view_app_vi [이동한 후 보여 줄 내용물],name='view'),
                                           -- > app_name = 'total_view_app' [함수형 호출][페이지이동시]   --> 해당 폴더의 경로를 담아둔다 추후 가독성과 적어야 하는 url 길이가 단축된다.

3. [생성한 폴더] templates 폴더 만들어주기 -- >  url 경로가 변경 될 때마다 해당 url이 담고 있는 html 파일 생성하기
                                           -- >  만드는 형식은 
                                           -- >  1.templates 폴더 생성
                                           -- >  2.templates 폴더 안에다가 생성한 startapp 폴더명으로으로 폴더 하나를 더 생성
                                           -- >  templates 
                                                   - total_view_app

4. html 파일 생성    -- >  templates 
                            - total_view_app
                               - '작명'.html


[ [ 2021-11-27 ] [django] startproject 와 startapp 연결방법 ]
** django startproject 와 startapp 연결방법 **
1. settings.py 파일을 열어서 생성한 startapp 폴더를 등록해주기  -- > INSTALLED_APPS = [] 에 '생성한 폴더명'
2. startproject에 있는 urls.py에 가서 경로 이어주기             -- > path('total_view_app/  [경로] ',include("total_view_app.urls")[url분할],name='total_view_app'),
3. startapp에 views.py을 열어서 기존에 [ [ 2021-11-27 ] [django] startapp 생성방법 ]에 2번 내용적은 [이동한 후 보여 줄 내용물]을 만들어준다.
                                                                -- > def total_view_app_vi [함수명](request):[요청]

                                                                        context ={}[보내면서 같이 보낼 데이터 박스]

                                                                        return render(request[요청],'total_view_app/view.html'[뿌려질 화면],context[데이터])
4. 3번에서 만든 내용물 [urls.py]로 가서 import 해준다.  -- > from .views import total_view_app_vi
5. 최상위에 있는 [templates] 폴더에 있는 [base.html] 파일을 분할한다.    -- > 1. <head></head> 태그 부분을 잘라내기 한다.
                                                                         -- > 2. [templates] 폴더에 새로운 head.html 파일 생성 후 잘라낸 태그부분을 붙여넣기 한다.
                                                                         -- > 3. [base.html] 파일에서 잘라낸 위치에다가 {% include 'head.html' %}를 써주면 
                                                                             [base.html] 과 [head.html]이 연결이 된다. 
                                                                         -- > 4. [base.html]에서 <body></body> 부분에  {% block '작명' %}{% endblock %}  써준다
                                                                                 그러면 startapp폴더 안에 있는 html과 연결 준비가 끝이다. 
                                                                         -- > 5. [ [ 2021-11-27 ] [django] startapp 생성방법 ]에 4번에 만든 html 파일로 가서 
                                                                                 base.html 파일을 불러오고  -- > {% extends 'base.html' %}를 써주면 불러와 진다.
                                                                                 {% block '작명' %}{% endblock %}를 그대로 적어준다.
                                                                         -- > 6. {% block '작명' %}
                                                                                   <div>초기설정 완료!</div>
                                                                                 {% endblock %}
                                                                                 를 적어준다.
                                                                         -- > 7. 실행하기   터미널창에 python manage.py runserver를 입력한 뒤 
                                                                                 http://127.0.0.1:8000/total_view_app/view/ 경로로 접속하여 본다.
                                                                         -- > 8. 최종적으로 [초기설정 완료!] 문구가 적힌걸 볼 수가 있다.


 [ 2021-11-27 ] [django] css,js,fonts,외부파일 분리하기 
 ** css,js,fonts,외부파일 분리하기 **
 1. settings.py을 열어서 멘 밑에        -- > STATIC_URL = '/static/'
                                        -- > STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
                                        -- > STATICFILES_DIRS = [ BASE_DIR / "static"] 
                                        -- > 기재한다.
 2. 최상위 폴더에 static 폴더를 만들고 다시 css, js, fonts 풀더를 만든다. 
 3. css 폴더에 base.css 파일을 만들고   -- >  div {font -size}를 해서 기존에 만든 div 속성 값을 주어 연결이 잘 됬는지 확인한다.
 4. 최상위 폴더에 있는 templates 폴더를 열고 head.html 파일에 생성한 파일 경로를 적어준다.
                                        -- >  <link rel="stylesheet" href="{% static 'css/base.css' %}">
 5. 서버를 키고 잘 적용됬는지 확인한다.



 [ 2021-11-27 ] [util.css참조] css 약어로 간소화
 1. 현재 적용된 약어               ** font-size [px] ** 
                                   -- >  .fs-1~100 [font-size:0px~100px]
                                   ** padding [px] **
                                   -- >  .p-t-0~250 [padding-top:0px~250px]
                                   -- >  .p-b-0~250 [padding-bottom:0px~250px]
                                   -- >  .p-l-0~250 [padding-left:0px~250px]
                                   -- >  .p-r-0~250 [padding-right:0px~250px]
                                   ** margin [px] **
                                   -- >  .m-t-0~250 [margin-top:0px~250px]
                                   -- >  .m-b-0~250 [margin-bottom:0px~250px]
                                   -- >  .m-l-0~250 [margin-left:0px~250px]
                                   -- >  .m-r-0~250 [margin-right:0px~250px]
                                   -- >  .m-l-r-auto[margin-left:auto;margin-right:auto;]
                                   -- >  .m-l-auto[margin-left:auto;]
                                   -- >  .m-r-auto[margin-right:auto;]
                                   ** text ** 
                                   .text-white[color:white;]
                                   .text-black[color:black;]
                                   .text-center[text-align:center]
                                   .text-left[text-align:left]
                                   .text-right[text-right:right]
                                   ** 줄간격 **
                                   -- >  .lh-1-0~2.9[line-height:1.0~2.9;]
                                   ** display ** 
                                   .dis-[none,block,inline,inline-block,flex]
                                   ** position ** 
                                   .pos-[relative,absolute,fixed]
                                   ** float ** 
                                   .float-[l,r]


[ 2021-11-27 ] [django] [side_bar] 만들기  - > html 파일 생성
1. 최상위 폴더에서 [side.html]파일 생성하기 
2. base.html 파일에서 {% block content %}{% endblock %} 블럭 위에다가 {% include 'side_bar.html' %} 적어주기
3. <div>side바 작업 구간 입니다.</div> 라는 문구를 적고 서버를 돌려 잘 작동하는지 확인해 본다.
4. base.css로 가서 [ *{padding:0;,margin:0;} ] 기본적으로 들어가 있는 padding , margin을 초기화 시킨다.


 [ 2021-11-27 ] [django] [side_bar] 만들기  - > 상단 로고, 회사명, 반전 스위치 생성 
 1. margin 적용시 부모 태그도 같이 딸려서 이동된다면 부모 태그에 [display:fixed] 속성을 적용시킨다.



[ 2021-11-28 ] [django] [side_bar] 만들기  - > 메뉴 등록 , 메뉴마다 아이콘 생성, 배치 조정
1. display : fiex 속성을 이용하자!   --  flex-direction: column;



[ 2021-11-29 ] [django] [side_bar] 만들기  - > 메뉴바 숨김 상태일 때 생성, 숨겨질 때 나올 때 js 작동 완료 
1. head.html 파일에 js 파일 생성 후 [js폴더에서] 등록 ! [등록 할 때는 link가 아닌 <script src="경로"></script>]
2. function side_bar_up() {} 기본 형식 , $("#side_bar_up" [html태그 접근 할 때]).css("display","block" [속성변경 할 때])



 [ 2021-11-29 ] [django] [side_bar] 만들기  - > js -- > ts로 업글 
 1. node.js 최신버전으로 설치한다. 
 2. 터미널에서 npm install -g typescript 설치 
 3. ts 폴더를 만들고 .ts 파일과 tsconfig.json 파일을 만들어 준다 [설정파일]
 4. 다시 터미널에서 tsc -w 입력 -- > 터미널 창 끄지말기 [끄면 자동변환 안해줌]
 5. 만약 에러가 뜬다면 vscode를 닫고 관리자 모드로 다시 열어서 터미널 창에 [Get-ExecutionPolicy]  [Set-ExecutionPolicy RemoteSigned] 순서대로 입력 ! 




  [ 2021-11-29 ] [django] [side_bar] 만들기  - > 슬라이드 효과 적용 ! 
  1. visibility, transition 활용 !

                                            


                            
                                                      



 