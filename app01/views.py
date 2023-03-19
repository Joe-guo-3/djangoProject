from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")

def user_list(request):
    # 去app目录下的templates目录找user_list.html(根据app的注册顺序，逐一去他们的templates的目录下找)
    return render(request, "user_list.html")

def user_add(request):
    return render(request, "user_add.html")

def tpl(request):
    name = "郭兆博"
    roles = ["ceo","cfo","ooo"]
    user_info = {"name":"果汁","salary":10000,'role':"CTP"}
    data_list = [{"name":"果汁","salary":10000,'role':"CTP"},
                 {"name": "apple", "salary": 10000, 'role': "CTP"},
                 {"name": "banana", "salary": 10000, 'role': "CTP"},

    ]
    return render(request,'tpl.html',{"n1":name,"n2":roles,'n3':user_info,'n4':data_list})

def news(req):
    import requests
    res = requests.get()

def something(request):

    # 1.request 是一个对象，封装了用户发来的所有数据
    print(request.method)

    # 2.在url上传递的值
    print(request.GET)

    # 3.在请求体中提交数据
    print(request.POST)

    # 4返回文本
    # return HttpResponse("返回内容")


    # 返回页面
    # return render(request,'something.html',{"tittle":"来了"})

    # 【响应】让浏览器重定向到其他的页面
    return redirect("https://www.baidu.com/")