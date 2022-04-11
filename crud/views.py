from .models import Product
from django.views.generic.list import ListView

# Create your views here.


class ProductListView(ListView):
    """
    一覧
    """

    # 一覧を表示するモデルを指定する
    model = Product
