from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def bosh_sahifa(request):
    if request.user.is_authenticated:



        return render(request,"bosh_sahifa.html")
    return redirect('/')
def kitoblar(request):
    if request.method=="POST":
        Kitob.objects.create(
            nom=request.POST.get('n'),
            sahifa=request.POST.get('s'),
            muallif=Muallif.objects.get(id=request.POST.get('m')),
            janr=request.POST.get('j')
        )
        return redirect('/kitob/')

    soz=request.GET.get('qidirish')
    if soz is None or soz=="":
        st=Kitob.objects.all()
    else:
        st=Kitob.objects.filter(nom__contains=soz)

    data={"kitob":st,
          "muallif":Muallif.objects.all()}
    return render(request,"kitoblar.html",data)
def kitob_ochir(request,son):
    data={"kitob":Kitob.objects.get(id=son).delete()}
    return redirect('/kitob/')
def mualliflar(request):
    if request.method=="POST":
        Muallif.objects.create(
            ism=request.POST.get('i'),
            jinsi=request.POST.get('j'),
            tirik=request.POST.get('t'),
            kitob_soni=request.POST.get('k_s'),
            tugulgan_sana=request.POST.get('t_s')

        )
        return redirect('/muallif/')
    soz=request.GET.get('qidirish')
    if soz is None or soz=="":
        st=Muallif.objects.all()
    else:
        st=Muallif.objects.filter(ism__contains=soz)
    data={"muallif":st}
    return render(request,"muallif.html",data)
def muallif_edit(request,son):
    if request.method=="POST":
        Muallif.objects.filter(id=son).update(
            ism=request.POST.get('i'),
            jinsi=request.POST.get('j'),
            tirik=request.POST.get('t'),
            kitob_soni=request.POST.get('k_s'),
            tugulgan_sana=request.POST.get('t_s')

        )
        return redirect('/muallif/')
    data={"muallif":Muallif.objects.get(id=son)}
    return render(request,"muallif_edit.html",data)
def muallif_ochir(request,son):
    data={"muallif":Muallif.objects.get(id=son).delete()}
    return redirect("/muallif/")
def talabalar(request):
    if request.method=="POST":
        Talaba.objects.create(
            ism=request.POST.get('i'),
            bitiruvchi=request.POST.get('b'),
            kitoblar_soni=request.POST.get('k_s'),
            kurs=request.POST.get('k')
        )
        return redirect('/talaba/')
    a=request.GET.get('qidirish')
    if a is None or a=="":
        st=Talaba.objects.all()
    else:
        st=Talaba.objects.filter(ism__contains=a)

    data={"talaba":st}
    return render(request,"talaba.html",data)
def adminlar(request):
    data={"admin":Admin.objects.all()}
    return render(request,"admin.html",data)
def recordlar(request):
    if request.method=="POST":
        Record.objects.create(
            talaba=Talaba.objects.get(id=request.POST.get('t')),
            kitob=Kitob.objects.get(id=request.POST.get('k')),
            admin=Admin.objects.get(id=request.POST.get('a')),
            olingan_sana=request.POST.get('o_s'),
            qaytarish_sanasi=request.POST.get('q_s'),
            qaytardi=request.POST.get('q')

        )
        return redirect('/record/')
    a=request.GET.get('qidirish')
    if a is None or a=="":
        st=Record.objects.all()
    else:
        st=Record.objects.filter(talaba__ism__contains=a)

    data={"record":st,
          "talaba":Talaba.objects.all(),
          "kitob":Kitob.objects.all(),
          "admin":Admin.objects.all()}
    return render(request,"record.html",data)
def bitta_talaba(request,son):
    data={
        "talaba":Talaba.objects.get(id=son)
    }
    return render(request,"bitta_talaba.html",data)
def bitta_kitob(request,son):
    data={
        "kitob":Kitob.objects.get(id=son)
    }
    return render(request,"bitta_kitob.html",data)
def bitta_record(request,son):
    data={
        "record":Record.objects.get(id=son)
    }
    return render(request,"bitta_record.html",data)
def bitta_muallif(request,son):
    data = {
        "muallif": Muallif.objects.get(id=son)
    }
    return render(request, "bitta_muallif.html", data)
def talaba_edit(request,son):
    if request.method=="POST":
        Talaba.objects.filter(id=son).update(
            ism=request.POST.get('i'),
            bitiruvchi=request.POST.get('b'),
            kitoblar_soni=request.POST.get('k_s'),
            kurs=request.POST.get('k')

        )
    data={
        "talaba":Talaba.objects.get(id=son)
    }
    return render(request,"talaba_edit.html",data)
def record_edit(request,son):
    if request.method=="POST":
        Record.objects.filter(id=son).update(
            talaba=Talaba.objects.get(id=request.POST.get("t")),
            kitob=Kitob.objects.get(id=request.POST.get("k")),
            admin=Admin.objects.get(id=request.POST.get('a')),
            olingan_sana=request.POST.get('o_s'),
            qaytarish_sanasi=request.POST.get('q_s'),
            qaytardi=request.POST.get('q'),
        )
        return redirect('/record/')
    data={
        "record":Record.objects.get(id=son),
        "talaba":Talaba.objects.all(),
        "kitob":Kitob.objects.all(),
        "admin":Admin.objects.all()
    }
    return render(request,"record_edit.html",data)
def kitob_edit(request,son):
    if request.method=="POST":
        Kitob.objects.filter(id=son).update(
            nom=request.POST.get('n'),
            sahifa=request.POST.get('s'),
            muallif=Muallif.objects.get(id=request.POST.get('m')),
            janr=request.POST.get('j'),
        )
        return redirect('/kitob/')
    data={
        "kitob":Kitob.objects.get(id=son),
        "muallif":Muallif.objects.all()
    }
    return render(request,"kitob_edit.html",data)
def loginview(request):
    if request.method=="POST":
        user=authenticate(username=request.POST.get('l'),
                          password=request.POST.get('p'))
        if user is None:
            return redirect('/')
        login(request,user)
        return redirect('/bosh_sahifa/')
    return render(request,"login.html")
def logoutview(request):
    logout(request)
    return redirect('/')
def register(request):
    if request.method=="POST" and request.POST.get("p")==request.POST.get('cp'):
        User.objects.create_user(username=request.POST.get('l'),
                                 password=request.POST.get('cp'))
        return redirect('/')
    return render(request,"register.html")