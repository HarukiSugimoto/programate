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

def low_if(request):
    return render(request, 'myapp/low_if.html')

def low_for(request):
    return render(request, 'myapp/low_for.html')

def low_def(request):
    return render(request, 'myapp/low_def.html')

def middle_if(request):
    return render(request, 'myapp/middle_if.html')

def middle_for(request):
    return render(request, 'myapp/middle_for.html')

def middle_def(request):
    return render(request, 'myapp/middle_def.html')

def high_course(request):
    return render(request, 'myapp/high_course.html')
