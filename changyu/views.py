from django.shortcuts import render

# Create your views here.
def index(request):
    # 首页
    return render(request, 'changyu/index.html')

def service(request):
    # 服務項目
    return render(request, 'changyu/service.html')

def projectshare(request):
    # 業務實績
    return render(request, 'changyu/projectshare.html')

def csr(request):
    # 企業社會責任
    return render(request, 'changyu/csr.html')

def contact(request):
    # 聯絡我們
    return render(request, 'changyu/contact.html')