# demoapp/views.py

from django.shortcuts import render

def set_cookie(request):
    response = render(request, 'demoapp/display_cookie_session.html')
    response.set_cookie('my_cookie', 'cookie_value')
    return response

def set_session(request):
    request.session['my_session'] = 'session_value'
    return render(request, 'demoapp/display_cookie_session.html')
