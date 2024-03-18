from django.shortcuts import render
from django.views import View
from .tasks import my_task, another_task


class IndexView(View):
    def get(self, request):
        my_task.delay()
        another_task.delay()
        return render(request, 'main_app/index.html')
