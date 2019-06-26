from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect


class LandingPage(View):
    def show_landing_page(request):

        if ('search' in request.GET) and (request.GET != ''):
            search_term = request.GET['search']
            query = 'realtors/?search=' + search_term
            return redirect(query)
        
        return render(request, 'landing_page.html')




