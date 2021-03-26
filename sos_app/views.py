from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInfo
from .utils import generate_user_id
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import redirect
from .utils import send_message


# Create your views here.

def add_details(request):
    # Collects and adds users details to database
    if request.method == 'POST':
        user_id = generate_user_id()
        nickname = request.POST.get('nickname')
        firstcontact_name = request.POST.get('firstcontact_name')
        firstcontact_number = request.POST.get('firstcontact_number')
        secondcontact_name = request.POST.get('secondcontact_name')
        secondcontact_number = request.POST.get('secondcontact_number')
        user_info = UserInfo.objects.create(user_id=user_id, nickname=nickname, firstcontact_name=firstcontact_name,
                                            firstcontact_number=firstcontact_number,
                                            secondcontact_name=secondcontact_name,
                                            secondcontact_number=secondcontact_number)
        user_info.save()
        return redirect('home', user_id)
    return render(request, 'sos_app/givecontact.html')


def send_sos(request, user_id):
    # Redirects user to unique URL IMPLEMET COPY HERE
    return render(request, 'sos_app/gethelp.html', {user_id: user_id})


@csrf_exempt
def get_location(request):
    # Gets User location and sends te
    print(request.POST)
    print(request.headers.values())
    if request.method == 'POST':
        if request.is_ajax():
            HttpResponse('SENT')
            user_id = request.headers['Authorization']
            user = UserInfo.objects.get(user_id=user_id)
            data = request.POST.get('position')
            data = json.loads(data)
            latitude = data.get('lat')
            longitude = data.get('lng')
            map_link = f"www.google.com/maps/place/{latitude},{longitude}"
            if map_link:
                send1 = send_message(user.nickname, user.firstcontact_name, user.firstcontact_number, map_link)
                send2 = send_message(user.nickname, user.secondcontact_name, user.secondcontact_number, map_link)
                print(send2, send1, '--------------------------------')
            else:
                HttpResponse("there was an error sending your message")
            return HttpResponse(map_link)
        return render(request, 'sos_app/gethelp.html')
    return HttpResponse('Your location could not be retrieved')


def success(request):
    return render(request, 'sos_app/success.html')
