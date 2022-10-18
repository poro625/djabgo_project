from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login as loginsession
from django.shortcuts import get_object_or_404

# Create your views here.
def signup(request):
    if request.method =='GET': #데이터 조회
        return render(request, 'signup.html')

    elif request.method == 'POST': # 데이터 수정, 내부에 바디가 있다 
        username = request.POST.get('username') #signup.html안에 있는것중 POST로 받은 바디안에 있는 것중 username를 get하라는 의미다
        password = request.POST.get('password')
        passwordcheck = request.POST.get('passwordcheck')
        if password == passwordcheck:
            User.objects.create_user(username = username, password = password) # User.objects.get의 뜻은 User의 DB(objects)에 있는 테이블에서 .create_user를 새로 만들어라라는 뜻 그냥 create는 메소드 명령어이다
            return HttpResponse('회원가입 완료')
        else :
            return HttpResponse('비밀번호 확인 틀렸습니다')

        
    else :
         # 좋은 코드 아님
         return HttpResponse('허용되지 않은 메소드 입니다')

def login(request):
    if request.method =='GET': #데이터 조회
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:  # if user라고 해도됨 
            loginsession(request, user) # 장고문서에서 확인한것으로 login as loginsession에서 login을 활용하였기에 이름만 커스컴마이징을 한것
            return redirect('users:user') # redirect는 다른 url로 가라는 뜻
            #  return HttpResponse('users:user')로 안되나?라고 생각할 수 있다 이 되면 redirect랑 주소창도 달라지며, HttpResponse이것이 더 많은 로직들이 작성되어있다 redirect를 사용하자
        else:
            return HttpResponse('로그인 실패')

def user(request):
    #print(request.user) # username = request.POST.get('username')이러한 형태가 아닌 print(request.user)이러한 형태인 것은 장고가 알아서 편리하게 보낸 requet에서 쿠키를 검사해서 쿠키안에 우리랑 session 동일한거 있으면 user값 보여줄게
    return HttpResponse(request.user)
    # return render('user.html')

def profile(request, username): #같이 들어온 인자 값이 있기 때문에 username을 쓴다.
                                # 그래서 urls.py에서 <str:username>로 유저네임을 받으면 유저네임을 보여주도록 프로필페이지를 작성할 수 있다.
    user = User.objects.get( username = username ) 
    user = get_object_or_404(User, username=username)  
    context = {
        'user' : user

    }
    return render(request, 'profile.html', context)
