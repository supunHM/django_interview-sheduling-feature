from django.shortcuts import render, get_object_or_404,redirect
from .models import Student, Interview
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def index(request):
    interviews = Interview.objects.all()
    students = Student.objects.all()
    color = None
    query = ""

    if request.method == "POST":
        if "add" in request.POST:
            date = request.POST.get("date")
            time = request.POST.get("time")
            student = request.POST.get("student")
            position = request.POST.get("position")

            student = get_object_or_404(Student, stu_nic=student)

            Interview.objects.create(
                date=date,
                time=time,
                stu_nic=student,
                position=position,
            )
            color = 'success'
            messages.success(request, "Interview Schedule added successfully...")
        

        elif "update" in request.POST:

            id = request.POST.get("id")
            date = request.POST.get("date")
            time = request.POST.get("time")
            student = request.POST.get("student")
            position = request.POST.get("position")

            student = get_object_or_404(Student, stu_nic=student)

            updateInterview = get_object_or_404(Interview, id=id)
            updateInterview.date = date
            updateInterview.time = time
            updateInterview.stu_nic = student
            updateInterview.position = position
            updateInterview.save()

            color = "info"
            messages.success(request, "Interview Schedule Updated successfully...")
        
        elif "delete" in request.POST:
            id = request.POST.get("id")
            Interview.objects.get(id=id).delete()
            color = "danger"

            messages.success(request,"Student Deleted Successfully")

        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            interviews = Interview.objects.filter(Q(stu_nic__stu_nic__icontains=query) | Q(position__icontains=query))

    context = {"interviews": interviews,"students":students, "color": color, "query": query}
    return render(request, "index.html", context=context)
