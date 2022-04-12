from django.urls import path
from . import views

app_name = "crud"
urlpatterns = [

    # 一覧
    path("", views.ProductListView.as_view(), name="list"),

    # 新規登録
    path('new/', views.ProductCreateView.as_view(), name='new'),

    # 編集
    path('edit/<int:pk>/', views.ProductUpdateView.as_view(), name='edit'),

    # 削除
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete'),
]
