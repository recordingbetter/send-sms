from django.http import HttpResponse
from django.shortcuts import render
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException
from .api import API_KEY, API_SECRET


def send_sms(request):
    if request.method == 'GET':
        return render(request, 'send_sms/send_sms.html')
    else:
        params = dict()
        params['type'] = request.POST.get('type')
        params['to'] = request.POST.get('receiver')
        params['from'] = request.POST.get('sender')
        params['text'] = request.POST.get('text')

        cool = Message(API_KEY, API_SECRET)
        try:
            response = cool.send(params)
            print("Success Count : %s" % response['success_count'])
            print("Error Count : %s" % response['error_count'])
            print("Group ID : %s" % response['group_id'])

            if "error_list" in response:
                print("Error List : %s" % response['error_list'])
        except CoolsmsException as e:
            print("Error Code : %s" % e.code)
            print("Error Message : %s" % e.msg)
        return HttpResponse('Message sent!')
