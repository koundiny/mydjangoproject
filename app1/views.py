from django.shortcuts import redirect, render
from django.contrib import messages
from app1.forms import StudentForm
from app1.models import Student

# Create your views here.

def home(request):
    return render(request, 'home.html')


def studentdetail(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()        
            return redirect('studentdetail')
    else:
        form = StudentForm()
    student = Student.objects.all()
    return render(request, 'studentdetail.html', {'student': student, 'form': form})


def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('studentdetail')
    
def update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('studentdetail')
    return render(request, 'update.html', {'form': form, 'student': student})
