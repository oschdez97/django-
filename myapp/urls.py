from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('login.html', views.login, name='login'),
    path('register.html', views.register, name='register'),
    path('forgot-password.html', views.forgot_password, name='forgot-password'),
    path('buttons.html', views.buttons, name='buttons'),
    path('cards.html', views.cards, name='cards'),
    path('charts.html', views.charts, name='charts'),
    path('tables.html', views.tables, name='tables'),
    path('utilities-color.html', views.utilities_color, name='utilities-color'),
    path('utilities-border.html', views.utilities_border, name='utilities-border'),
    path('utilities-animation.html', views.utilities_animation, name='utilities-animation'),
    path('utilities-other.html', views.utilities_other, name='utilities-other'),
    path('404.html', views.not_found, name='not-found'),
    path('blank.html', views.blank, name='blank'),
]