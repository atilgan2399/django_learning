from django.shortcuts import render
from django.http import HttpResponse , Http404 , HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse




course_dictionary = {
    "python" : "Python course page",
    "kotlin" : "Kotlin course page",
    "swift"  : "Swift course international system",
    "java"   : "Asla Pes Etme ... Başarı için mücadeledeye devam ."
        
}

def index(request):
    return HttpResponse("this is first django project,first index")

def course(request , item):
    try:
        course = course_dictionary[item]
        return HttpResponse(course)
    
    except:
         # raise Http404(" NOT FOUND !!! ")
        return HttpResponseNotFound("SİTE BULUNAMADI !!!")
    
def course_number(request,num1):
    course_list =list(course_dictionary.keys())
    try:
        course = course_list[num1]
        page_go_to = reverse("course",args=[course])
        return HttpResponseRedirect(page_go_to)
    except:
        return HttpResponseNotFound("SİTE BULUNAMADI !!!")
    
""""
def course(request,item):
    #return HttpResponse(course_dictionary.get(item,"Not Found!!"))
"""