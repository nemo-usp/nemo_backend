from django.shortcuts import render


def launch_site(request):
    return render(request, 'nemo/index.html', {})
