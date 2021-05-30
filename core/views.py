# core/views.py
from django.shortcuts import render
from django.contrib.auth.models import User              
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import ListView


class MyPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:
                # return the last page
                return self.num_pages
            elif int(number) < 1:
                # return the first page
                return 1
            else:
                raise


class ListUsers(ListView):
    model = User
    template_name = 'home.html'
    paginate_by = 5
    paginator_class = MyPaginator # We use our paginator class
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        users = User.objects.all()
        paginator = self.paginator_class(users, self.paginate_by)
        
        users = paginator.page(page)
        
        context['users'] = users
        return context