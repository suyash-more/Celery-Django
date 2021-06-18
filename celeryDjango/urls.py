from django.contrib import admin
from django.urls import path
from app2.views import ReviewEmailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reviews/', ReviewEmailView.as_view(), name="reviews"),
]