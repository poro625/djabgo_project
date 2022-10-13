from django.http import HttpResponse
from django.shortcuts import render
from .models import User

# Create your views here.
def signup(request):
    if request.method =='GET': #데이터 조회
        return render(request, 'signup.html')

    elif request.method == 'POST': # 데이터 수정, 내부에 바디가 있다 
        username = request.POST.get('username') #signup.html안에 있는것중 POST로 받은 바디안에 있는 것중 username를 get하라는 의미다
        password = request.POST.get('password')
        passwordcheck = request.POST.get('passwordcheck')
        if password == passwordcheck:
            User.objects.create_user(username = username, password = password)
            return HttpResponse('회원가입 완료')
        else :
            return HttpResponse('비밀번호 확인 틀렸습니다')

        
    else :
         # 좋은 코드 아님
         return HttpResponse('허용되지 않은 메소드 입니다')