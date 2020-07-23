from django.urls import path
from .views import *

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', home_view, name='home'),
    path('worksheet-list/<int:pk>', WorkSheetList.as_view(), name='list'),
    path('create-worksheet/', create_worksheet_method, name='create_worksheet'),
    path('create-worksheet/success', create_success, name='create_success'),
    path('detail/<slug:slug>/', DetailWorksheet.as_view(), name='detail'),
    path('detail/<slug:slug>/edit', EditWorksheet.as_view(), name='edit'),
    path('detail/<slug:slug>/delete', DeleteWorksheet.as_view(), name='delete'),
    path("get_districts/", view=get_districts),
]