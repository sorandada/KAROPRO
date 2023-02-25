from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import KaroModel
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import Count, Avg, Sum, Max, Min

# Create your views here.

#class KaroList(ListView):
    #template_name = "list.html"
    #model = KaroModel

def KaroList(request):
    object_list=KaroModel.objects.all()

    kcolsum=object_list.aggregate(Sum("kcol"))
    golekcolmax=object_list.aggregate(Max("goleKcol"))
    golekcolmin=object_list.aggregate(Min("goleKcol"))



    #####################目標カロリーの表示##############################
    #最後）のレコードを取得
    last_order = KaroModel.objects.order_by("id").last()
    #print(last_order)
    golekcolcount=object_list.aggregate(Count("goleKcol"))
    golekcolcount=golekcolcount["goleKcol__count"]

    l=[]
    for i in object_list:
        l.append(i.id)
    #print(l)
    
    gole=0
    if KaroModel!=None and len(l)>1:
        #print("ok")
        gole=last_order.goleKcol
        print(gole)
        print(golekcolmax["goleKcol__max"])
        print(KaroModel.objects.get(pk=l[-2]).goleKcol)
        if (gole == 0) or (gole < golekcolmax["goleKcol__max"]):
            #print(KaroModel.objects.get(pk=l[-2]).goleKcol)
            if (KaroModel.objects.get(pk=l[-2]).goleKcol == 0):
                #l = sorted(l, reverse=True)
                #print(l) 
                
                for i in object_list:
                    if 0 != i.goleKcol:
                        gole = i.goleKcol
                        print(gole)
                #l = sorted(l, reverse=False)
                #print(l) 
                print(gole)  
            elif (gole != KaroModel.objects.get(pk=l[-2]).goleKcol):
                
                if gole==0:
                    for i in object_list:
                        if 0 != i.goleKcol:
                            gole = i.goleKcol
                
                gole = gole
                        

            else:
                gole=KaroModel.objects.get(pk=l[-2]).goleKcol
                #print(gole, "sss")
        else:
            gole=last_order.goleKcol
            #print(gole, "aaa")
        
    else:
        #print("no")
        #print(l)
        gole=0
        #print(gole)
        for i in object_list:
            gole = i.goleKcol 
            #print(gole)
    ###################### ここまで　############################

    if kcolsum["kcol__sum"] == None:
        kcolsum["kcol__sum"]=0
        lastkcal = gole-kcolsum["kcol__sum"]
    else:
        lastkcal = gole-kcolsum["kcol__sum"]

    import datetime
    dt_now = datetime.datetime.now()
    #print(dt_now)

    

    return render(request, "list.html", {"object_list": object_list, "kcolsum":kcolsum, "golekcolmax":golekcolmax,
    "golekcolmin":golekcolmin,"last_order":last_order, "gole":gole, "dt_now":dt_now,"lastkcal":lastkcal, "golekcolcount":golekcolcount})

    



class KaroDetail(DetailView):
    template_name="detail.html"
    model = KaroModel

class KaroCreate(CreateView):
    template_name="create.html"
    model = KaroModel
    
    fields = ("eat", "kcol", "daycolor", "date", "goleKcol", )
    success_url = reverse_lazy("list")

class KaroDelete(DeleteView):
    template_name="delete.html"
    model = KaroModel
    success_url = reverse_lazy("list")

class KaroUpdate(UpdateView):
    template_name="update.html"
    model = KaroModel
    fields = ("eat", "kcol", "daycolor")
    success_url = reverse_lazy("list")






def fulldelete(request):
    template_name = "fulldelete.html"
    if request.POST:
        KaroModel.objects.all().delete()
        return redirect("list")
    return render(request, template_name)
    


    

    

