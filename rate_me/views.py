from django.shortcuts import render
from django.views import View


class LadingPage(View):
    def lading_page(request):
        return render(request, 'landing_page.html')




