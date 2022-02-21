from django.views.generic import CreateView, TemplateView, ListView

from .forms import CategoryForm
from .models import Category


class AdminHome(TemplateView):
    template_name = 'admins/adminhome.html'


class CategoryCreate(CreateView):
    model = Category
    template_name = 'admins/category.html'
    form_class = CategoryForm
    success_url = 'categorylist'

class CategoryList(ListView):
    model = Category
    template_name = 'admins/category_list.html'
    context_object_name = 'categories'