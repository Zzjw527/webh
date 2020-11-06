import json

from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#学生界面获取总题目
from django.views import View

from mainForStu.models import ProblemsContent, ProblemTestData


class GetDataListView(View):

    def get(self, request):
        print("------get--------")

        #判断用户是否登录
        # result = request.session.get('username', 'null')
        # if result == 'null':
        #     print(result)
        if 'username' in request.session:
            print("------test--------")
            print(request.session['username'])
            ret = {"code": "200", "msg": "用户登录"}

            #存储数据
            # examples_data = []
            data = []

            # test = ProblemsContent.objects.values("problemId", "problemTitle")[0:1]
            # test.filter()
            # problemsList = ProblemsContent.objects.filter()
            dataList = ProblemTestData.objects.filter()
            print(dataList)
            for i in range(len(dataList)):
                print(dataList[i])
                #将model转化为字典
                problem_dict = model_to_dict(dataList[i])
                print(problem_dict)
                data.append(dataList[i])
            ret = {"code": "200", "msg": "成功获取", "data": data}
            return HttpResponse(json.dumps(ret, ensure_ascii=False))

        ret = {"code": "400", "msg": "用户未登录"}
        return HttpResponse(json.dumps(ret, ensure_ascii=False))


    # def post(self, request):
    #     print("------post--------")
    #     ret = {"code": False, "error": "用户名或密码错误"}
    #     return HttpResponse(json.dumps(ret, ensure_ascii=False))
    #     # return render(request, "test.html", {})
