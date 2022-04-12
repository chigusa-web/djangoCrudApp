from .models import Product
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


class ProductListView(ListView):
    """
    一覧
    """

    # 一覧を表示するモデルを指定する
    model = Product

    # 1ページの件数
    paginate_by = 5


class ProductCreateView(CreateView):
    """
    新規登録
    """

    model = Product

    # 登録項目
    fields = ['name', 'price']


class ProductUpdateView(UpdateView):
    """
    編集
    """

    model = Product

    # 更新項目
    fields = ['name', 'price']

    # テンプレートファイル名の接尾辞の指定
    template_name_suffix = '_update_form'


class ProductDeleteView(DeleteView):
    """
    削除
    """

    model = Product

    # 削除完了後のリダイレクト先
    success_url = reverse_lazy('crud:list')
