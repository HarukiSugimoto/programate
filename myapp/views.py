from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'myapp/home.html', {}) 

def course_one_example(request): #分岐の例題
    return render(request, 'myapp/course_one_example.html', {})

def course_one_main(request): #分岐の本題
    return render(request, 'myapp/course_one_main.html', {})

def course_two_example(request):
    return render(request, 'myapp/course_two_example.html', {})

def course_two_main(request):
    return render(request, 'myapp/course_two_main.html', {})

def course_three_example(request):
    return render(request, 'myapp/course_three_example.html')

def course_three_main(request):
    return render(request, 'myapp/course_three_main.html')