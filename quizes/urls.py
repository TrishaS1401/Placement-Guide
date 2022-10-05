import logging
from django.urls import path
from .views import (
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view,
    home,
    login_request,
    register_request,
    logout_request,
    contact,
    certificate
)

app_name = 'quizes'

urlpatterns = [
    path('home', home, name ="home"),
    path('login',login_request, name ="login"),
    path('register', register_request, name ="register"),
    path('contact', contact, name ="contact"),
    path('certificate', certificate, name='certificate'),
    path('logout', logout_request, name= "logout"),
    path('', QuizListView.as_view(), name='main-view'),
    path('<pk>/', quiz_view, name='quiz-view'),
    path('<pk>/save/', save_quiz_view, name='save-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
]