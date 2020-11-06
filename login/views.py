import json

from django.contrib.auth import login, logout
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from login.models import User


# Create your views here.

class RegisterView(View):

    def get(self, request):
        print("------get--------")
        return render(request, "register.html", {})

    def post(self, request):
        print("------post--------")
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        name = request.POST.get("name", "")
        print(username, password, name, email, phone)
        user = User()
        user.userName = username
        user.userPassWord = password
        user.userNickName = name
        user.userEmail = email
        user.userPhone = phone
        user.isAdmin = 0
        user.save()
        # obj = User.objects.filter(username=username, password=password)
        ret = {"code": "200", "msg": "注册成功"}
        return HttpResponse(json.dumps(ret, ensure_ascii=False))
        # return redirect(reverse('login'))
        # return render(request, "login.html", {})


class LoginView(View):

    def get(self, request):
        print("------get--------")
        return render(request, "login.html", {})


    def post(self, request):
        print("------post--------")
        ret = {"code": "400", "msg": "用户名或密码错误"}

        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        isAdmin = request.POST.get("isAdmin", "")
        isAdmin = 0
        print(username, password)

        try:
            obj = User.objects.filter(userName=username, userPassWord=password, isAdmin=isAdmin)
            print(obj)
        except:
            return render(request, "login.html", {})

        if len(obj) != 0:
            print(obj[0].userName)
            login(request, obj[0])
            print(request.user.userName)
            request.session['username'] = username
            # request.session['user'] = obj[0]
            ret = {"code": "200", "msg": "登录成功"}

        return HttpResponse(json.dumps(ret, ensure_ascii=False))
        # return render(request, "main.html", {})



class LoginForTeacher(View):

    def get(self, request):
        print("------get--------")
        return render(request, "login.html", {})


    def post(self, request):
        print("------post--------")
        ret = {"code": "200", "msg": "登陆成功"}

        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        print(username, password)

        try:
            obj = User.objects.filter(userName=username, userPassWord=password, isAdmin=1)
            print(obj)
        except:
            return render(request, "login.html", {})
        if len(obj) == 0:
            ret = {"code": "400", "msg": "用户名或密码错误"}

        return HttpResponse(json.dumps(ret, ensure_ascii=False))
        # return redirect(reverse('login.html'))
        # return render(request, "login.html", {})


class LogoutView(View):

    def get(self, request):
        print("------get--------")
        logout(request)
        request.session.flush()
        return render(request, "login.html", {})


# 用于注册时实时判断该数据是否存在
class JudgeInfo(View):

    def post(self, request):
        print("------post--------")
        ret = {"code": "200", "msg": "注册成功"}
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        print(username, email, phone)

        try:

            if username != '':
                obj = User.objects.filter(userName=username)
                ret = {"code": "400", "msg": "用户名已存在"}
            elif email != '':
                obj = User.objects.filter(userEmail=email)
                ret = {"code": "400", "msg": "邮箱已存在"}
            elif phone != '':
                obj = User.objects.filter(userPhone=phone)
                ret = {"code": "400", "msg": "手机号已存在"}
            print(obj)
        except:
            return render(request, "login.html", {})
        if len(obj) == 0:
            ret = {"code": "200", "msg": "符合要求"}

        return HttpResponse(json.dumps(ret, ensure_ascii=False))
        # return render(request, "login.html", {})



class ModifyInformation(View):

    def get(self, request):
        print("------get--------")
        ret = {"code": "200", "msg": "跳转成功"}

        # result = request.session.get('username', 'null')
        if request.session.get('username', 'null') == 'null':
            ret = {"code": "400", "msg": "用户未登录"}
            return HttpResponse(json.dumps(ret, ensure_ascii=False))

        username = request.session.get('username')
        print(username)

        try:
            obj = User.objects.filter(userName=username, isAdmin=0)
            print(obj)
        except:
            ret = {"code": "400", "msg": "系统出错"}
            return HttpResponse(json.dumps(ret, ensure_ascii=False))

        if len(obj) == 0:
            ret = {"code": "400", "msg": "用户名或密码错误"}

        problem_dict = model_to_dict(obj[0])
        data = [problem_dict]
        ret = {"code": "200", "msg": "跳转成功", "data": data}
        return HttpResponse(json.dumps(ret, ensure_ascii=False))
        # return render(request, "login.html", {})


    def post(self, request):
        print("------post--------")
        ret = {"code": "200", "msg": "修改成功"}

        username = request.POST.get("username", "")
        nickname = request.POST.get("nickname", "")
        password = request.POST.get("password", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        print(username, nickname, password, email, phone)

        try:
            obj = User.objects.filter(userName=username, isAdmin=0).update(userNickName=nickname, userEmail=email, userPhone=phone)
            print(obj)
        except:
            ret = {"code": "400", "msg": "修改失败"}
            return HttpResponse(json.dumps(ret, ensure_ascii=False))

        return HttpResponse(json.dumps(ret, ensure_ascii=False))
        # return redirect(reverse('login.html'))
        # return render(request, "login.html", {})