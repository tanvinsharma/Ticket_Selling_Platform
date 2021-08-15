from django.db import models
from django.utils.translation import gettext as _


class Event(models.Model):
	name = models.CharField(max_length=100)
	date = models.DateTimeField('date of event')
	time = models.DateTimeField('time of event')
	def __str__(self):
		return self.name

class Ticket(models.Model):
	STATUS = (
	  (1,  _('Ticket is available')),
	  (0, _('Ticket is not available')),
	  (2, _('Ticket is reserved')),
   )

	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	is_available = models.PositiveSmallIntegerField(
	  choices=STATUS,
	  default=1,
   )
	def __int__(self):
		return self.is_available

class Reservation(models.Model):
	STATUS = (
	  (1,  _('Yes')),
	  (0, _('No')),
   )
	is_reserved = models.PositiveSmallIntegerField(choices=STATUS, default=0)
	ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
	def __int__(self):
		return self.is_reserved