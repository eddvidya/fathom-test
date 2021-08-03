from django.shortcuts import render
from rest_framework import viewsets
from .models import Log
from .serializers import LogSerializer

class LogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Log.objects.all().order_by('-created')
    serializer_class = LogSerializer

def root(request):
	from random import choice
	phrases = (
		"Hey welcome!",
		"Refresh for new logs",
		"How's it going?",
		"Today was kinda good I guess.",
		"Hope you've been well.",
		"I FUCKING LOVE VIDEOGAMES.",
		"https://www.youtube.com/watch?v=hRebDYKASfQ Been listening to this kind of stuff for a while",
		"Take care man."
	)
	logged = Log(desc = choice(phrases))
	logged.save()
	return render(request, 'index.html')
