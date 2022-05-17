
from django.contrib import admin
from django.urls import path

import page.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lotto/', page.views.home),
    path('lotto/result/',page.views.result),
]
