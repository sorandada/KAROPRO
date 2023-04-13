from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import KaroModel
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import Count, Avg, Sum, Max, Min

import datetime

# Create your views here.

def KaroList(request):
    object_list=KaroModel.objects.all()
    kcolsum=object_list.aggregate(Sum("kcol"))
    golekcolmax=object_list.aggregate(Max("goleKcol"))

    #####################目標カロリーの表示##############################
    last_order = KaroModel.objects.order_by("id").last()
    golekcolcount=object_list.aggregate(Count("goleKcol"))
    golekcolcount=golekcolcount["goleKcol__count"]

    l=[]
    for i in object_list:
        l.append(i.id)
    
    gole=0
    if KaroModel!=None and len(l)>1:
        gole=last_order.goleKcol
        print(gole)
        print(golekcolmax["goleKcol__max"])
        print(KaroModel.objects.get(pk=l[-2]).goleKcol)
        if (gole == 0) or (gole < golekcolmax["goleKcol__max"]):
            if (KaroModel.objects.get(pk=l[-2]).goleKcol == 0):        
                for i in object_list:
                    if 0 != i.goleKcol:
                        gole = i.goleKcol
                        print(gole)
                print(gole)  
            elif (gole != KaroModel.objects.get(pk=l[-2]).goleKcol):
                
                if gole==0:
                    for i in object_list:
                        if 0 != i.goleKcol:
                            gole = i.goleKcol
                gole = gole

            else:
                gole=KaroModel.objects.get(pk=l[-2]).goleKcol
        else:
            gole=last_order.goleKcol
        
    else:
        gole=0
        for i in object_list:
            gole = i.goleKcol 
    ###################### ここまで　############################

    #摂取カロリーの合計
    if kcolsum["kcol__sum"] == None:
        kcolsum["kcol__sum"]=0
        lastkcal = gole-kcolsum["kcol__sum"]
    else:
        lastkcal = gole-kcolsum["kcol__sum"]


    dt_now = datetime.datetime.now()

    return render(request, "list.html", {"object_list": object_list, "kcolsum":kcolsum, "golekcolmax":golekcolmax,
    "last_order":last_order, "gole":gole, "dt_now":dt_now,"lastkcal":lastkcal, "golekcolcount":golekcolcount})

    


#詳細
class KaroDetail(DetailView):
    template_name="detail.html"
    model = KaroModel

#作成
class KaroCreate(CreateView):
    template_name="create.html"
    model = KaroModel
    
    fields = ("eat", "kcol", "daycolor", "date", "goleKcol", )
    success_url = reverse_lazy("list")

#削除
class KaroDelete(DeleteView):
    template_name="delete.html"
    model = KaroModel
    success_url = reverse_lazy("list")

#更新
class KaroUpdate(UpdateView):
    template_name="update.html"
    model = KaroModel
    fields = ("eat", "kcol", "daycolor")
    success_url = reverse_lazy("list")

#全削除
def fulldelete(request):
    template_name = "fulldelete.html"
    if request.POST:
        KaroModel.objects.all().delete()
        return redirect("list")
    return render(request, template_name)
    


    

    

