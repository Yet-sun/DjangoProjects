# coding=utf8
from django.shortcuts import render
from .models import Image
from .form import UploadImageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from aip_ocr_imageClassify import aipocr
from aip_ocr_imageClassify import aipImageClassify
import json
import time


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        data = {'username': username, 'password': password}

        if user:
            login(request)
            return render('home.html', {'data': json.dumps(data)})
        else:
            return render(request, 'login.html,{}')
    return render(request, 'login.html')


def logout(request):
    logout(request)
    return render(request, 'home.html')


@login_required
def ocr(request):
    '''图像文字识别(上传图片方式)'''
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)

        if form.is_valid():
            picture = Image(photo=request.FILES['image'])
            picture.save()

            result = aipocr.image_text_recognize(picture.photo.url.encode("utf-8"))
            data = json.dumps(list(result))

            return render(request, 'home.html', {'pictures': picture, 'text': data})
    else:
        form = UploadImageForm()

        return render(request, 'home.html', {'form': form})


@login_required
def ocr_url(request):
    if request.method == 'POST':
        '''图像文字识别(url方式)'''
        image_url = request.POST.get('image_url')
        result = aipocr.image_text_recognize_url(image_url)
        data = json.dumps(list(result))

        return render(request, 'ocr.html', {'data': data})
    else:
        return render(request, 'home.html')


@login_required
def imageClassify(request):
    '''图像物体识别(上传图片方式)'''
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)

        if form.is_valid():
            picture = Image(photo=request.FILES['image'])
            picture.save()

            image = picture.photo.url
            # d = os.path.dirname(image)
            # ext = os.path.splitext(image)[1]
            # str2 = time.strftime('%Y%M%D%H%S')
            # name = str2 + '_%d' % random.randint(0, 100)
            # path = d + '/' + name + ext

            # image_name=os.listdir('./upload')
            # for temp in image_name:
            #     num=temp.rfind(']')
            #     os.rename(,path)

            result = aipocr.image_text_recognize(image)
            data = json.dumps(list(result))

        return render(request, 'imageClassify.html', {'pictures': picture, 'result': data})
    else:
        form = UploadImageForm()

        return render(request, 'home.html', {'form': form})


@login_required
def imageClassify_url(request):
    '''图像物体识别(url方式)'''
    if request.method == 'POST':
        image_url = request.POST.get('image_url')
        result = aipImageClassify.imageClassify_url(image_url)
        data = json.dumps(list(result))

        return render(request, 'imageClassify.html', {'result': data})
    else:
        return render(request, 'home.html')
