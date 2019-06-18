from django.urls import path
from .views import AgentView, AgentForm


urlpatterns = [
    path('', AgentView.list_agents, name='list_agents'),
    path('<int:pk>/', AgentView.get_agent, name='agent_detailed_view'),
    path('addAgent/', AgentForm.add_agent, name='add_agent_form'),
]
