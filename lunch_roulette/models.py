from django.db import models
from django.conf import settings

# Create your models here.

# class LunchDates(models.Model):
#     date = models.DateField()

#     class Meta:
#     	pass


class Participant(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	is_participating = models.BooleanField('Participate?', default=True)

	def __unicode__(self):
		return u'{} {}'.format(self.user.email, self.is_participating)


class LunchGroup(models.Model):
    date = models.DateField()
    participants = models.ManyToManyField(Participant)

    def __unicode__(self):
    	# participants_str = 'some participants'
    	participants_str = ',\n\t'.join([str(part) for part in self.participants.all()])
    	return u"{date}:\n\t{participants_str}".format(date=self.date, 
    												  participants_str=participants_str)

    class Meta:
    	pass
