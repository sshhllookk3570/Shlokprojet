from django.shortcuts import render,HttpResponse
from student.models import Student
from student.models import Address

def save(request,id,name,age,T_mark):
    stud=Student(id=id,name=name,age=age,T_mark=T_mark)
    stud.save()
    return HttpResponse("saved secessfully")

#saving address of student by using id as refrence
def saveAddress(request,id,address):
    stud=Student.objects.get(id=id)
    studadd=Address(stud=stud,address=address)
    studadd.save()
    return HttpResponse("saved secessfully")


def get_allStudent(request):
    stud=Student.objects.all()
    add = Address.objects.all()
    a=-1
    n=[]
    for i in stud:
        a=a+1
        n.append({ 'ID':i.id,
                 'name':i.name,
                 'Age':i.age,
                  'Total mark':i.T_mark,
                  'Address':add[a].address,
                 }
                 )

    return HttpResponse(n)



def getStudent(request,name):
    stud=Student.objects.get(name=name)
    add=Address.objects.all()[stud.id-1].address

    #add=stud.addr_set.get(id=stud.id)
    n=[]
    n.append({'ID':stud.id,
            'name': stud.name,
              'Age': stud.age,
              'Total mark': stud.T_mark,
              'Address':add}
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