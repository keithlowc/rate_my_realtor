from django.shortcuts import render
from django.views import View
from django.views.decorators.http import require_GET
from django.shortcuts import redirect
from django.contrib import messages

from .models import Agent, AgentsData
from .forms import AddAgentForm

class AgentView(View):

    @require_GET
    def list_agents(request):
        data = Agent.objects.all()

        context = {
            'data': data,
        }
        
        return render(request, 'realtor/agents/list_agents.html', context)
    
    def get_agent(request, pk):
        agent_personal_info = Agent.objects.get(id=pk)
        agent_data = AgentsData.objects.filter(agent=agent_personal_info)
        form = AddAgentForm()
        context = {
            'agent_personal_info': agent_personal_info,
            'agent_data': agent_data,
            'form': form,
        }
        return render(request, 'realtor/agents/detailed_agent.html', context)


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
