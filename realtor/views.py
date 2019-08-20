from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.decorators.http import require_GET
from django.shortcuts import redirect
from django.contrib import messages
from django.core import serializers
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Agent, AgentsData
from .forms import AddAgentForm, AddAgentDataForm
from users.models import CustomUser


'''
Class for Agent view, and list view. It allows the user to filter 
and to search for agents.
'''
class AgentView(View):

    @require_GET
    def list_agents(request):
        data = Agent.objects.order_by('name')
        search_term = ''
        search = False

        if ('search' in request.GET) and (request.GET['search'] != ''):
            search = True
            search_term = request.GET['search']
            full_name = search_term.split()

            name = Q(name__icontains=full_name[0])
            last_name = Q(last_name__icontains=full_name[0])

            if len(full_name) > 1:
                last_name = Q(last_name__icontains=full_name[1])
                data = data.filter(name & last_name)
            
            data = data.filter(name | last_name)

        paginator = Paginator(data, 10)
        page = request.GET.get('page')
        data = paginator.get_page(page)
        get_dict_copy = request.GET.copy()
        params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()

        context = {
            'data': data,
            'search_term': search_term,
            'params': params,
            'search': search,
        }
        
        return render(request, 'realtor/agents/list_agents.html', context)
    
    def get_agent(request, pk):
        agent = Agent.objects.get(id=pk)
        agent_data = AgentsData.objects.filter(agent=agent)
        user = request.user
        
        if request.method == 'POST':
            form = AddAgentDataForm(request.POST)

            if form.is_valid():
                comment = form.save(commit=False)
                comment.agent = agent
                comment.created_by = user
                comment.save()

                agent_ratings = agent_data.values('rating')

                total_rating = 0

                for data in agent_ratings:
                    total_rating += float(data['rating'])

                total_rating = total_rating / len(agent_ratings)

                agent.rating = round(total_rating, 1)
                agent.save()

                messages.success(request, 'Succesfully added comment')
                return redirect('agent_detailed_view', pk)
            else:
                messages.warning(request, 'Something went wrong! Please check your comment')
        else:
            form = AddAgentDataForm()

        paginator = Paginator(agent_data, 5)
        page = request.GET.get('page')
        agent_data = paginator.get_page(page)
        get_dict_copy = request.GET.copy()
        params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()

        context = {
            'agent': agent,
            'agent_data': agent_data,
            'form': form,
            'params': params,
        }
        return render(request, 'realtor/agents/detailed_agent.html', context)
    
    def sort_agents(request, keyword):
        if keyword == 'rating':
            data = Agent.objects.order_by('-' + keyword)
        else:
            data = Agent.objects.order_by(keyword)
        
        if ('search' in request.GET) and (request.GET['search'] != ''):
            search_term = request.GET['search']
            full_name = search_term.split()
            name = Q(name__icontains=full_name[0])

            if len(full_name) > 1:
                last_name = Q(last_name__icontains=full_name[1])
                data = data.filter(name & last_name)

            data = data.filter(name)
            print('Data ', data)
        
        paginator = Paginator(data, 5)
        page = request.GET.get('page')
        data = paginator.get_page(page)
        get_dict_copy = request.GET.copy()
        params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()

        context = {
            'data': data,
            'params': params,
        }
        return render(request, 'realtor/agents/list_agents.html', context)

'''
Class for the agent form.
'''
class AgentForm():

    def add_agent(request):
        if request.method == 'POST':
            form = AddAgentForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Succesfully Added Agent')
                return redirect('list_agents')
        else:
            form = AddAgentForm()
        
        context = {
            'form': form
        }
        
        return render(request, 'realtor/agents/forms/add_agent_form.html', context)







    
