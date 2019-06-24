from background_task import background
from realtor.models import Agent, AgentsData

@background(schedule=1)
def calculate_agent_rating(agent_id):
    print('Starting calculate_agent_rating()')
    
    agent = Agent.objects.get(id=agent_id)
    agent_ratings = AgentsData.objects.filter(agent=agent).values('rating')
    total_rating = 0

    if len(agent_ratings) != 0:

        for data in agent_ratings:
            total_rating += float(data['rating'])

        total_rating = total_rating / len(agent_ratings)

        agent.rating = round(total_rating, 1)

        agent.save()







