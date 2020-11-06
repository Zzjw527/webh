from django.shortcuts import HttpResponse,render,redirect
# Create your views here.
from django.urls.base import *
from test_verify import models
from test_verify import tests
from functools import wraps
def index_zjw(request):
    return render(request,'index_zjw.html')

def login_required(func):
    @wraps(func)
    def inner(request,*args,**kwargs):
        print(request.COOKIES)
        is_login = request.get_signed_cookie('is_login',salt='zjw',default='')
        if is_login !='':
            return redirect('/login/?url={}'.format(request.path_info))
        ret=func(request,*args,**kwargs)
        return ret
    return inner


@login_required
def xiusj(request):

    if request.method =='POST' :
        if 'user' in request.POST:
            getemail =request.POST.get('user')
            print(getemail)
            if models.User_zjw.objects.filter(phone=getemail):
                getcode=tests.Mobileauthentication(getemail)
                print(getcode)
                return render(request, 'xiusj.html', {'success': '已发送短信'})
            else:
                return render(request,'xiusj.html',{'error':'没有查找到用户存在该手机'})
        if 'pwd' in request.POST:
            # getc = request.POST.get('user')
            # if (getc==getcode):
            #     return redirect('/index/')
            pass
    return render(request,'xiusj.html')
@login_required
def xiuyx(request):

    if request.method =='POST' :
        if 'user' in request.POST:
            getemail =request.POST.get('user')
            print(getemail)
            if models.User_zjw.objects.filter(email=getemail):
                getcode=tests.Emailauthentication(getemail)
                print(type(getcode))
                print(getcode["code"])
                print(getcode["time"])
                if(getcode["code"]==1):
                    global captcha
                    captcha=getcode['captcha']
                    print(getcode['captcha'])
                    return render(request, 'xiusj.html', {'success': '已发送邮件'})
                else:
                    return render(request, 'xiusj.html', {'success': '邮件发送错误'})
            else:
                return render(request,'xiusj.html',{'error':'没有查找到用户存在该手机'})
        if 'pwd' in request.POST:
            getc = request.POST.get('user')
            # if (getc==captcha):
            #     return redirect('/index/')
            if (getc==123):
                return redirect('/index/')
            pass
    return render(request,'xiuyx.html')
def tq(request):
    all_que=models.teacherquestion.objects.all()
    return render(request,'zhanshi.html',{'all_que':all_que})
def tq_add(request):
    if request.method=='POST':
        que = request.POST.get('geque')
        det = request.POST.get('gedet')
        aut = request.POST.get('geaut')
        models.teacherquestion.objects.create(question=que,detail=det,author=aut)
    return render(request,'zhanshi.html')
def tq_del(request):
    if request.method=='POST':
        id = request.POST.get('geid')
        models.teacherquestion.objects.get(pk=id).delete()
    return render(request,'zhanshi.html')
def tq_xiu(request):
    pk=request.GET.get('pk')
    xiu_obj=models.teacherquestion.objects.get(pk=pk)

    if request.method=='POST':
        xiuname=request.POST.get('xiuname')
        xiu_obj.author=xiuname
        xiu_obj.save()
        return render(request, 'zhanshi.html')
def login_zjw(request):
    if request.method =='POST':
        print('ok')
        user =request.POST.get('user')
        pwd =request.POST.get('pwd')
        if models.User_zjw.objects.filter(username=user,password=pwd):
            url=request.GET.get('url')
            if url:
                return_url = url
            else:
                return_url ='/index/'
            ret =redirect(return_url)
            ret.set_signed_cookie("is_login",'1',salt='zjw')

            return ret
            # return redirect('http://acm.hdu.edu.cn/status.php')
    return render(request,'login.html')