from .models import Product
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

# Create your views here.


class ProductListView(ListView):
    """
    一覧
    """

    # 一覧を表示するモデルを指定する
    model = Product


class ProductCreateView(CreateView):
    """
    新規登録
    """

    model = Product

    # 登録項目
    fields = ['name', 'price']
