from django.db import models

class Event(models.Model):
	name = models.CharField(max_length=100)
	date = models.DateTimeField('date of event')
	time = models.DateTimeFile('time of event')

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