from django.urls import path
from . import views
from django.contrib import admin



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name="home"),
    path('checkout/',views.checkout_view,name="checkout"),
    path('response/',views.response_view,name="response"),
]
