from django.shortcuts import render, get_object_or_404
from .models import Project, Category, SubCategory
# Create your views here.


def home(request):
    project = Project.objects.all()[0:6]
    context = {'project':project}
    return render(request, 'portfolio/home.html', context)

def portfolio(request):
    project = Project.objects.all()
    category = Category.objects.all()
    context = {'category':category, 'project':project}
    return render(request, 'portfolio/portfolio.html', context)

def portfolio_detail(request, id):
    context = {'project':project}
    return render(request, 'portfolio/portfolio_detail.html', context)    


#def sub_category_detail(request, id):
 #   sub_category = SubCategory.objects.get(id=id)
  #  context = {'sub_category': sub_category}
   # return render(request, 'portfolio/sub_category_detail.html', context)

def about(request):
    return render(request, 'portfolio/about.html')   