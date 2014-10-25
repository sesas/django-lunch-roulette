import logging
import random

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from django.forms.models import modelformset_factory

import toolz

from . import models
from . import forms

# Create your views here.
def join(request):
    # import pdb; pdb.set_trace()

    # The following try/except block should probably be 
    # in a signal receiver for newly created User objects
    try:
        participant = request.user.participant
    except models.Participant.DoesNotExist:
        participant = models.Participant(user=request.user)
        participant.save()
    
    if request.method == 'GET':
        form = forms.ParticipantForm(request.GET)
        context = {'form': form}
        return render(request, 'lunch_roulette/base.html', context)

    if request.method == 'POST':
        form = forms.ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            model_instance = form.save()
        # if request.REQUEST.get('is_participating') == 'on':
        #     participant.is_participating = True
        # else: 
        #     participant.is_participating = False
                
        return redirect(join)


def roll(request):
    form = forms.LunchGroupForm

    if request.method == 'GET':
        ParticipantFormset = modelformset_factory(models.Participant)
        formset = ParticipantFormset(queryset=models.Participant.objects.filter(is_participating=True))
        context = {'form': form(), 
                    'formset': formset
                    }
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




