from django.shortcuts import render,redirect
from users.models import User
from django.core.urlresolvers import reverse
import re

# Create your views here.

def register(request):
    '''显示用户注册页面'''
    return render(request,'users/register.html')

def register_handle(request):
    '''进行用户注册处理'''
    #接收数据
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    #进行数据校验
    if not all([username,password,email]):
        #有数据为空
        return render(request,'users/register.html',{'errmsg':'参数不能为空'})
    #判断邮箱是否合法
    if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$',email):
        return render(request,'users/register.html',{'errmsg':'邮箱不合法！'})

    #进行业务处理：注册，向账户系统中添加账户
    passport = User.objects.add_one_passport(username=username,password=password,email=email)

    #注册完，还是返回注册页
    return redirect(reverse('user:login'))

def login(request):
    username = ''
    checked = ''
    context = {
        'username' : username,
        'checked' : checked,

    }
    return render(request,'users/login.html',context)

def login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('pwd')
    # remember = request.POST.get('remember')
    passport = User.objects.get_one_passport(username=username,password=password)

    if  passport:
        return redirect(reverse('books:index'))
    else:
        p = User.objects.get_one_passport(username=username)
        if not p:
            return render(request,'users/login.html',{'errmsg':'用户名不存在'})
        return render(request,'users/login.html',{'errmsg':'密码不正确'})

def logout(request):
    '''用户退出登录'''
    request.session.flush()
    return redirect(reverse('books:index'))
