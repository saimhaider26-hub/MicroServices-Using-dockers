from django.contrib import admin
from django.urls import path, include
from admin.views import UserAPIView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('api/user', UserAPIView.as_view()),
]