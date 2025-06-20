from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ContactMessage

from django.views.decorators.csrf import csrf_protect
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

def charity(request):
    # 企業社會責任
    return render(request, 'changyu/charity.html')

def contact(request):
    # 聯絡我們
    return render(request, 'changyu/contact.html')

@csrf_protect  # 确保CSRF保护
def contact_submit(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        category = request.POST.get('category')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # 这里可以添加简单校验（视情况添加）

        contact = ContactMessage.objects.create(
            category=category,
            name=name,
            gender=gender,
            phone=phone,
            email=email,
            message=message
        )
        return JsonResponse({'success': True, 'message': '感謝您的聯絡，我們會盡快回覆您。'})
    return JsonResponse({'success': False, 'message': '請使用正確的方式提交表單。'})