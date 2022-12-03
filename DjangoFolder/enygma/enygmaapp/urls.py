from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout


urlpatterns = [
    path('', views.index, name='index'),
    path('default/', views.default, name='default'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('items/', views.items, name='items'),
    path('items/<int:mysteryid>/', views.mystery_title, name='mystery_title'),
    path('create_mystery/', views.create_mystery, name='create_mystery'),
    # path('select_culprit/', views.select_culprit, name="select_culprit"),
    path('select_clues/', views.select_clues, name="select_clues"),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('signout/', views.signout, name='signout'),
    path('my_profile/delete_user/<username>/', views.delete_user, name='delete_user'),
    # path('chatbot/', views.chatbot, name='chatbot'),
    # path('delete_user/<username>',delete_user, name='delete_user')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
