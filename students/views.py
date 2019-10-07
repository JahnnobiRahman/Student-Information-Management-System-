from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student
from django.db.models import Q


def home(request):
     students =Student.objects
     query = request.GET.get("q")
     if query:
        result = students.filter(Q(roll__icontains=query))
        return render(request,'students/home.html' ,{'students':result})

     return render(request,'students/home.html')

@login_required(login_url="/accounts/register")
def create(request):
    if request.method=='POST':
        if request.POST['student_num'] and request.POST['roll'] and request.POST['dept'] and request.POST['address'] and request.FILES['image']:
                student=Student()
                student.student_num= request.POST['student_num']
                student.roll=request.POST['roll']
                student.dept= request.POST['dept']
                student.address= request.POST['address']
                student.image= request.FILES['image']
                student.mark= 1
                student.adder=request.user
                student.save()
                return redirect('/students/' + str(student.id))
        
        
        else:
            return render(request, 'students/create.html',{'error':'All fields are required'})


    else:
        return render(request, 'students/create.html')


def detail(request,student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/detail.html',{'student':student})
