from django.http.response import HttpResponse
from shortener.models import Url
from django.shortcuts import render, redirect
import uuid
# Create your views here.

def index(request):
	return render(request, "index.html")

def create(request):
	if request.method == 'POST':
		url = request.POST['link']
		uid = str(uuid.uuid4())[:5]
		new_url = Url(link=url, uuid= uid)
		new_url.save()
		return HttpResponse(uid)

def go(request, pk):
	url_details = Url.objects.get(uuid=pk)
	print(url_details.link)
	return redirect(''+url_details.link)