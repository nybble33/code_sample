import django.http as d_http

from django import forms
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

def nybble_user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'],
                password=cd['password']
                )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return HttpResponse('Authenticated successfully')
                    auth_response = 'Authenticated successfully'
                else:
                    # return HttpResponse('Disabled account')
                    auth_response = 'Disabled account'
                # return render(request, 'cms/login_result.html')
            else:
                # return HttpResponse()
                auth_response = 'Invalid login'
            return render(
                request,
                'cms/auth_response.html',
                {'auth_response': auth_response}
                )

    else:
        form = LoginForm()
        ref_page = 'Ololo'
    return render(request, 'cms/login.html',
        {'form': form, 'ref_page': ref_page}
        )

def nybble_user_logout(request):
    logout(request)
    auth_response = 'Now you logged out.'
    auth_response += ' <a href="/login">Here</a> you can log in again'
    return render(
        request,
        'cms/auth_response.html',
        {'auth_response': auth_response}
        )


def ajax_login(request):
    context = {'response': 'Not processed'}
    if request.method == 'POST':
        q_data = request.POST.copy()
    else:
        q_data = request.GET.copy()
    try:
        user_name = q_data.get('user', 'Nan!!')
        user_pwd = q_data.get('pwd', '___')
        is_ajax = q_data.get('ajax', False)
        user = authenticate(
                username=user_name,
                password=user_pwd
            )
        if user is not None:
            context['response'] = "Success"
            login(request, user)
        else:
            context['response'] = "Error"
        return d_http.JsonResponse(context)
    except:
        pass
    return d_http.JsonResponse(context)

def ajax_logout(request):
    logout(request)
    tmpl = '''
            <h3>Now you are logged out.</h3>
            <p><a href="/login">Here</a> you can log in back</p>'
           '''
    context = {'template': tmpl}
    return d_http.JsonResponse(context)
