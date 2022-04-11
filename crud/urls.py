from django.urls import path
from . import views

app_name = "crud"
urlpatterns = [

    # 一覧
    path("", views.ProductListView.as_view(), name="list"),
]
