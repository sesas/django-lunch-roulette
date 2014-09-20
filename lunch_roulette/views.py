import logging
import random

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import get_user_model

import toolz

from . import models
from . import forms

# Create your views here.
def join(request):
    # import pdb; pdb.set_trace()
    try:
        participant = request.user.participant
    except models.Participant.DoesNotExist:
        participant = model.Participant(user=request.user)
    form = forms.ParticipantForm(instance=participant)
    context = {'user': request.user, 
               'my_formset': form}
    
    if request.method == 'GET':
        return render(request, 'lunch_roulette/base.html', context)

    if request.method == 'POST':
        if request.REQUEST.get('is_participating') == 'on':
            participant.is_participating = True
        else: 
            participant.is_participating = False
                
        return redirect(join)

        # return render(request, 'lunch_roulette/base.html', context)

def roll(request):
    form = forms.LunchGroupForm
    context = {'user': request.user, }

    if request.method == 'GET':
        context += {'my_formset': form()}
        return render(request, 'lunch_roulette/base.html', context)

    if request.method == 'POST':
        form = form(request.POST)
        if not form.is_valid():
            context['messages'] = ['Date is not valid']
            render(request, 'lunch_roulette/base.html', context)                
        date = form.cleaned_data.get('date')

        participants = list(models.Participant.objects.filter(is_participating=True))
        random.shuffle(participants)

        while 1:
            subgroup = list(toolz.take(4, participants))
            participants = participants[4:]
            logging.warn(subgroup)
            if not subgroup:
                break

            group = models.LunchGroup(date=date)
            group.save()

            group.participants.add(*subgroup)
            group.save()


        # import pdb; pdb.set_trace()

        return redirect(roll)




