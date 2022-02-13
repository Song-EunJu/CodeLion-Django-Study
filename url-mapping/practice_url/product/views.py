from django.shortcuts import render

# Create your views here.
def productList(request):
    return render(request, 'productList.html')

def productFirst(request):
    return render(request, 'productFirst.html')