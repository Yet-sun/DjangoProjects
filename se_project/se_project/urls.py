"""se_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from imageupload import views
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.conf.urls import include
from imageupload.urls import router as img_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sign/',views.sign),
    path('api/login/',views.login),
    path('logout/',views.logout),
    path('api/ocr/',views.ocr),
    path('api/ocr_url/',views.ocr_url),
    path('api/imageClassify/',views.imageClassify),
    path('api/imageClassify_url/',views.imageClassify_url),
    path('api/',include(img_router.urls)),
    path('api/manage_user',views.manage_guest)
]
