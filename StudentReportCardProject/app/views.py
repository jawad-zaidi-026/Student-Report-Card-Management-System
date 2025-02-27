from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q, Sum



# Create your views here.

def home(request):
    return render(request, 'home.html')

def students(request):
    return render(request, 'students.html')

def get_students(request):
    queryset = Student.objects.all()
    
    # ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks' , 'student_age')
    # for rank in ranks:
    #     print(rank.marks)
    
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = search)|
            Q(department__department__icontains = search)|
            Q(student_id__student_id__icontains = search)|
            Q(student_age__icontains = search)|
            Q(student_email__icontains = search)

        )
    paginator = Paginator(queryset, 10)  # Show 20 students per page

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'students.html', {'queryset': page_obj})


from .seed import generate_report_card
def see_marks(request , student_id):
    # generate_report_card()
    queryset = SubjectMarks.objects.filter(student__student_id__student_id  = student_id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    
    # current_rank = -1
    # ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks' , 'student_age')
    
    # i = 1
    # for rank in ranks:
    #     if student_id == rank.student_id.student_id:
    #         current_rank = i
    #         break
    #     i = i+1
    
    return render(request, 'see_marks.html', {'queryset': queryset , 'total_marks' : total_marks })
