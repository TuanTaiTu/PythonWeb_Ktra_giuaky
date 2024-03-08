from django.shortcuts import render

def characteristic(request):
    return render(request, 'pages/characteristic.html')