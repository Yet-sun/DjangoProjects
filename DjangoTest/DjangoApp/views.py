from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Event, Guest


def index(request):
    return render(request, "home.html")


def login_action(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        response = HttpResponseRedirect('/event_manage/')
        request.session['user'] = username
        return response
    else:
        return render(request, "home.html", {'error': 'username or password error!'})


@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response


# 会议列表
@login_required
def event_manage(request):
    # username = request.COOKIES.get('user', '')# 读取浏览器cookie
    username = request.session.get('user', '')
    events = Event.objects.all()

    return render(request, 'event_manage.html', {"user": username, "events": events})


# 参会人员列表
@login_required
def guest_manage(request):
    guest_list = Guest.objects.get_queryset().order_by('id')
    username = request.session.get('username', '')
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果页数不是整数，取第一页
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果页数超过查询范围，取最后一页
        contacts = paginator.page(paginator.num_pages)

    return render(request, "guest_manage.html", {"user": username, "guest": contacts})


# 会议搜索
@login_required
def search_name(request):
    username = request.session['user']
    search_name = request.GET.get("name", "")
    event_list = Event.objects.filter(name_contains=search_name)

    return render(request, 'event_manage.html', {'user': username, 'event': event_list})


# 签到界面
@login_required
def sign_index(request, eid):
    event = get_object_or_404(Event, id=eid)
    return render(request, 'sign_index.html', {'user': event})


# 签到功能
@login_required
def sign_index_action(request, eid):
    event = get_object_or_404(Event, id=eid)
    phone = request.POST.get('phone', '')
    # print(phone)
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(result, 'sign_index.html', {'event': event, 'hint': 'phone error.'})

    result = Guest.objects.filter(phone=phone, event_id=eid)
    if (not result) or (len(result) > 1):
        return render(request, 'sign_index.html', {'event': event, 'hint': 'event id or phone error.'})

    result = Guest.objects.filter(phone=phone, event_id=eid)
    # print(result)
    if result[0].sign:
        return render(result, 'sign_index.html', {'event': event, 'hint': 'user has sign in.'})
    else:
        result[0].sign = 1
        return render(result, 'sign_index.html', {'event': event, 'hint': 'sign in success!.', 'guest': result[0]})
