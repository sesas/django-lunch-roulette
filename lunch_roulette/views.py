from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import get_user_model

from . import models
from . import forms

# Create your views here.
def join(request):
	# import pdb; pdb.set_trace()
	participant = request.user.participant
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
	if request.method == 'GET':
		form = forms.LunchGroupForm()
		context = {'user': request.user, 
				   'my_formset': form}
		return render(request, 'lunch_roulette/base.html', context)