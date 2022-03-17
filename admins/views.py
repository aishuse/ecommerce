from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, ListView

from authapp.decorators import signin_required
from .forms import CategoryForm
from .models import Category


@method_decorator(signin_required, name='dispatch')
class AdminHome(TemplateView):
    template_name = 'admins/adminhome.html'


@method_decorator(signin_required, name='dispatch')
class CategoryCreate(CreateView):
    model = Category
    template_name = 'admins/category.html'
    form_class = CategoryForm
    success_url = 'categorylist'


@method_decorator(signin_required, name='dispatch')
class CategoryList(ListView):
    model = Category
    template_name = 'admins/category_list.html'
    context_object_name = 'categories'