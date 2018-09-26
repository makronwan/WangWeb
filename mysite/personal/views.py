from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    for my_val in range(1,9):
        my_val_x = my_val +100
    return render(request, 'personal/basic.html', {'content':['If you would like to contact me, please email me','hskinsley@gmail.com',my_val_x]})
