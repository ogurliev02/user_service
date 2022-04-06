from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View


class UserView(View):
    def get(self, request, *args, **kwargs):
        page_number = request.GET.get('page')
        info_per_page = int(request.GET.get('info_per_page') or 25)
        if not page_number or not info_per_page:
            return HttpResponseNotFound('<h1>Введите, пожалуйста, аттрибуты page_number и/или info_per_page</h1>')
        users = User.objects.all().select_related('profile').defer('password')
        paginator = Paginator(users, info_per_page)
        page_obj = paginator.get_page(page_number)
        return render(request, 'list.html', {'page_obj': page_obj})


class EmailView(View):
    def get(self, request, *args, **kwargs):
        email = request.GET.get('email') or 'пусто!'
        user = User.objects.filter(email=email).first()
        if not user:
            return HttpResponseNotFound(f'<h1>По вашему email - {email} ничего не найдено'
                                        f', введите пожалуйста корректный email</h1>')
        return render(request, 'info.html', {'user': user})
