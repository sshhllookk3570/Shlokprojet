from django.shortcuts import render,HttpResponse
from student.models import Student

def save(request,name,address,age,T_mark):
    stud=Student(name=name,address=address,age=age,T_mark=T_mark)
    stud.save()
    return HttpResponse("saved secessfully")


def get_allStudent(request):
    stud=Student.objects.all()
    n=[]
    for i in stud:
        n.append({'name':i.name,
                  'Address':i.address,
                 'Age':i.age,
                  'Total mark':i.T_mark}
                 )

    return HttpResponse(n)



def getStudent(request,name):
    stud=Student.objects.get(name=name)
    n=[]
    n.append({'name': stud.name,
              'Address': stud.address,
              'Age': stud.age,
              'Total mark': stud.T_mark}
             )

    return HttpResponse(n)


def deleteStudent(request,name):
    stud=Student.objects.get(name=name)
    stud.delete()
    return HttpResponse("succesfull")

def percentage(request):
    stud = Student.objects.all()
    dic=[]
    for i in stud:
        m=i.T_mark
        per=(m*100)/500
        if(per>=70):
            dic.append({i.name:per})
   # dic="/".join(dic)
    return HttpResponse(dic)



def hello(request):
    return HttpResponse("hi hello")
#,i.address,i.age,i.T_marks