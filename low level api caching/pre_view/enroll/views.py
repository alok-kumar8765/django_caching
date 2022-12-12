from django.shortcuts import render
from django.core.cache import cache
# Create your views here.
# def home(request):
#     mv = cache.get('movie','has_expired')
#     if mv == 'has_expired':
#         cache.set('movie','Dhoom',30)
#         mv=cache.get('movie')
#     return render(request,'enroll/course.html',{"fm":mv})

# def home(request):
#     mv = cache.get_or_set('fee',4000,30,version=2)
#     return render(request,'enroll/course.html',{"fm":mv})

# def home(request):
#     data = {'name':'ramesh','age':20}
#     cache.set_many(data,30)
#     sv = cache.get_many(data)
#     return render(request,'enroll/course.html',{"stu":sv})

def home(request):
    cache.delete('name') # to delete mention key_name
    return render(request,'enroll/course.html')
