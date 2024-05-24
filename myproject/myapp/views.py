import re
from django.shortcuts import render,HttpResponseRedirect
from .models import Teacher
# Create your views here.
def add_and_show(request):
    if request.method=="POST":
        teacher_id=request.POST['teacher_id']
        teacher_name=request.POST['teacher_name']
        subject=request.POST['subject']
        school=request.POST['school']
        teacher=Teacher(teacher_id=teacher_id,teacher_name=teacher_name,subject=subject,school=school)
        teacher.save()
    teacher_data=Teacher.objects.all()
    return render(request,'home.html',{'data':teacher_data})   
     
def delete_teacher(request,id):
    teach_del=Teacher.objects.get(teacher_id=id) 
    teach_del.delete()  
    return HttpResponseRedirect('/create/')  

def update_teacher(request,id):
        if request.method=='POST':
            teacher_id=request.POST['teacher_id']
            teacher_name=request.POST['teacher_name']
            subject=request.POST['subject']
            school=request.POST['school']
            obj=Teacher.objects.get(teacher_id=id)
            obj.teacher_id=teacher_id
            obj.teacher_name=teacher_name
            obj.subject=subject
            obj.school=school
            obj.save()
            return HttpResponseRedirect('/create/')  
        teacher_data1=Teacher.objects.get(teacher_id=id)
        return render(request,'update.html',{'data1':teacher_data1})   

