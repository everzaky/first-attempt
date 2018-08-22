from django.shortcuts import render
def main(request):
    return render(request, 'nakopitel/main.html', {})
# Create your views here.
