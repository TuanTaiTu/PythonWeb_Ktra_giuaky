from django.shortcuts import render

def hobby(request):
    return render(request, 'pages/hobby.html')