from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from django.conf import settings


urlpatterns = [
    path('', home, name='home'),
    path('educations/<int:pk>', disciplines, name='disciplines'),
    path('discipline/<int:pk>', discipline, name='discipline_detail'),
    path('discipline/create', discipline_create, name='discipline_create'),
    path('register/', register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),  # авторизация
    path('logout/', auth_view.LogoutView.as_view(template_name='login.html'), name='logout'),  # выйти
    path('createnewyear/', createnewyear, name='createnewyear'),
    path('index/update/<int:pk>', updateindex, name='index_update'),
    path('user/detail/<int:pk>', user_detail, name='user_detail'),
    path('user/list/', user_list, name='user_list'),
    path('word/create/<int:pk>', word_gener, name='wordgen')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
