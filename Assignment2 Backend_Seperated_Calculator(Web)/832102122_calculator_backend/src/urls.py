from django.urls import path
from calculator_web import views

urlpatterns = [
    path('', views.handler),  # 处理打开网页请求
    path('history/', views.history, name='show_history'),  # 历史记录页面

    path('calculation/', views.calculation, name='calculation'),  # 前端向后端发送计算请求
    path('set_mode/', views.set_mode, name='set_mode'),  # 设置三角函数、inv函数模式
    path('change_tri_mode/', views.change_tri_mode, name='change_tri_mode'),  # 设置三角函数计算模式
    path('change_inv_mode/', views.change_inv_mode, name='change_inv_mode'),  # 设置是否使用反函数

    path('clear_history/', views.clear_history, name='clear_history'),  # 清除上次使用的历史记录
    path('history/get_history/', views.get_history, name='get_history'),  # 清除上次使用的历史记录
]
