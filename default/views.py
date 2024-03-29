from django.shortcuts import render_to_response
from django.views.generic import *
from .models import *

# Create your views here.
#def poll_list(raq):
   # polls = Poll.objects.all()
   # return render_to_response('poll_list.html',{'items':polls})

class PollList(ListView):
    model = Poll

class PollDetail(DetailView):
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['options'] = Option.objects.filter(poll_id=self.kwargs['pk'])
        return context
    
class  PollVote(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        item = Option.objects.get(id=self.kwargs['oid'])
        item.count += 1
        item.save()
        return '/poll/{}/'.format(item.poll_id)

class PollCreate(CreateView):
    model = Poll
    fields = ['subject']
    success_url = '/poll/'
    #template_name = 