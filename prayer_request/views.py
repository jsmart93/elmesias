from django.shortcuts import render
from django.core.mail import send_mail

def prayer_request(request):
	return render(request, 'prayer_request/prayer_request.html')

def send(request):
	name = request.POST['name']
	email = request.POST['email']
	phone = request.POST['phone']
	prayer = request.POST['prayer']

	send_mail(
    	'Prayer Request',
    	"Name: " + name + '\n\n' + "Email: " + email + "\n\n" + "Phone: " + phone  + "\n\n" + "Prayer Request: \n\n" + prayer,
    	# 'jmartinez1093@gmail.com',
    	# ['jmartinez1093@gmail.com'],
    	'elmesiasfloresville@gmail.com',
    	['elmesiasfloresville@gmail.com'],
    	fail_silently=False,
    )

	return render(request, 'prayer_request/send.html')