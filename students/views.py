from django.db.models import Q
from django.shortcuts import render,redirect
from .models import Student
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerailizer

def home(request):
    msg = ""
    msg_type = ""
    
    last_student = Student.objects.order_by("-id").first()

    if request.method == "POST":
        name = request.POST.get("name")
        father_name = request.POST.get("father_name")
        gender = request.POST.get("gender")
        state = request.POST.get("state")
        city = request.POST.get("city")
        course = request.POST.get("course")
        college = request.POST.get("college")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        
        if not email:
            msg = "Email is required"
            msg_type = "Erorr"

        else:
           if Student.objects.filter(email=email).exists():
              msg = "Email already exists! plz try another one"
              msg_type = "Erorr"

           else:

                last_student = Student.objects.create(
                   name=name,
                   father_name=father_name,
                   gender=gender,
                   state=state,
                   city=city,
                   course=course,
                   college=college,
                   email=email,
                   phone=phone
                )

                msg = "Student saved sucessfully 🎉"
                msg_type = "Success"

       


    return render(request, "home.html", {"msg": msg, "msg_type" : msg_type, "student": last_student})

def delete_latest_student(request):
    if request.method == "POST":
        latest_student = Student.objects.order_by("-id").first()
        
        if latest_student:
            latest_student.delete()
    return redirect("home")
        
def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def student_list(request):
    search = request.GET.get("search", "").strip()

    students = Student.objects.all().order_by("-id")

    if search:
        students = students.filter(
            Q(name__icontains=search) |
            Q(father_name__icontains=search) |
            Q(gender__icontains=search) |
            Q(state__icontains=search) |
            Q(city__icontains=search) |
            Q(course__icontains=search) |
            Q(college__icontains=search) |
            Q(email__icontains=search) |
            Q(phone__icontains=search)  
        )
        
    total = students.count()

    return render(request, "student_list.html", {"students": students, "search": search, "total": total})

@api_view(['GET', 'POST','DELETE'])
def student_api(request):

    if request.method == "GET":
        students = Student.objects.all().order_by("-id")
        serializer = StudentSerailizer(students, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = StudentSerailizer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        students.delete()
        return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)     

@api_view(['GET', 'POST', 'DELETE'])
def students_detail_api(request, id):
    try:
        student = Student.objects.get(id=id)

    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = StudentSerailizer(student)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = StudentSerailizer(student, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        student.delete()
        return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)