# coding=utf8
from django.shortcuts import render
from .models import Image, Guest
from .form import UploadImageForm
from django.contrib.auth import authenticate, logout, login
from aip_ocr_imageClassify import aipocr
from aip_ocr_imageClassify import aipImageClassify
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .serializer import UserSerializer, UserSignSerializer, UserManageSerializer
from rest_framework import viewsets, filters
import json


# Create your views here.
class UserManageSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = UserManageSerializer


@csrf_exempt
def sign(request):
    if request.method == 'POST':
        data = request.body
        str1 = str(data.decode())
        data = eval(str1)

        print(data)
        serializer = UserSignSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.errors
        serializer.validated_data
        serializer.save()
        return render(request, "home.html")
    else:
        return HttpResponse("error!")


@csrf_exempt
def login(request):
    message = {'message': "验证错误", 'error_num': 1}
    if request.method == 'POST':
        data = request.body
        data = json.loads(data)
        username = data['username']
        password = data['password']

        user = authenticate(request, username=username, password=password)

        list = Guest.objects.filter(username=username).values('level')
        level = list[0]['level']

        data = {'username': username, 'level': level, 'error_num': 0}

        if user is not None:
            login(request, user)
            return JsonResponse(message, safe=False)
        else:
            return JsonResponse(data, safe=False)
    # return JsonResponse(message, safe=False)


def logout(request):
    logout(request)
    return render(request, 'home.html')


@csrf_exempt
# @login_required
def ocr(request):
    '''图像文字识别(上传图片方式)'''
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)

        picture = Image(photo=request.FILES['file'])
        picture.save()

        result = aipocr.image_text_recognize(picture.photo.url.encode("utf-8"))

        return JsonResponse(result, safe=False)
    else:
        form = UploadImageForm()

        return render(request, 'home.html', {'form': form})


@csrf_exempt
# @login_required
def ocr_url(request):
    if request.method == 'POST':
        '''图像文字识别(url方式)'''

        data = request.body

        data = str(data, encoding="utf8")
        image_url = data.splitlines()[3]
        print("image_url:", image_url)

        result = aipocr.image_text_recognize_url(image_url)

        return JsonResponse(result, safe=False)

    else:
        return render(request, 'home.html')


@csrf_exempt
# @login_required
def imageClassify(request):
    '''图像物体识别(上传图片方式)'''
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)

        picture = Image(photo=request.FILES['file'])
        picture.save()

        image = picture.photo.url

        result = aipImageClassify.imageClassify(image)

        return JsonResponse(result, safe=False)
    else:
        form = UploadImageForm()

        return JsonResponse({"error": "error"}, safe=False)


@csrf_exempt
# @login_required
def imageClassify_url(request):
    '''图像物体识别(url方式)'''
    if request.method == 'POST':
        data = request.body

        # print(data)
        data = str(data, encoding="utf8")
        # print("data:",data)
        image_url = data.splitlines()[3]
        print("image_url:",image_url)

        result = aipImageClassify.imageClassify_url(image_url)

        return JsonResponse(result, safe=False)
    else:
        return render(request, 'home.html')

@csrf_exempt
def manage_guest(request):
    message = {'message': 'message'}
    return JsonResponse(message, safe=False)
