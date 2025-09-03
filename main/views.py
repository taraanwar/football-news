from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406365276',
        'name': 'Tara Nirmala Anwar',
        'class': 'KKI'
    }

    return render(request, "main.html", context)