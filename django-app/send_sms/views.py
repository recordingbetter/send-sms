from django.shortcuts import render, redirect


def send_sms(request):
    if request.method == 'GET':
        return render(request, 'send_sms/send_sms.html')
    else:
        pass
