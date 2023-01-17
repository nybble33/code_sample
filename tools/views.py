from django.shortcuts import render

# Create your views here.

def screen_width(request):
    context = {
        'user_agent': request.META['HTTP_USER_AGENT'],
        'some_local': 'Psh psh'
    }
    return render(request, 'tools/screen_w.html', context)


def tiny_mce(request):
    return render(request, 'tools/tinymce.html', {} )


def canvas01(request):
    return render(request, 'tools/canvas01.html', {})

def dragNdrop(request):
    return render(request, 'tools/dragndrop.html', {})
