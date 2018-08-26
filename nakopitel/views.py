from django.shortcuts import render,render_to_response
from .forms import Postprice
from .models import Price
from .project import ver7_11_1
from django.http import  HttpResponse
from django.shortcuts import redirect

def index(request):
    f = Postprice()
    if request.method == 'POST':
        form = Postprice(request.POST)
        if form.is_valid():
            plot0 = float(form.cleaned_data.get('pot_0'))
            plot1 = float(form.cleaned_data.get('pot_1'))
            plot2 = float(form.cleaned_data.get('pot_2'))
            plot3 = float(form.cleaned_data.get('pot_3'))
            plot4 = float(form.cleaned_data.get('pot_4'))
            plot5 = float(form.cleaned_data.get('pot_5'))
            plot6 = float(form.cleaned_data.get('pot_6'))
            plot7 = float(form.cleaned_data.get('pot_7'))
            plot8 = float(form.cleaned_data.get('pot_8'))
            plot9 = float(form.cleaned_data.get('pot_9'))
            plot10 = float(form.cleaned_data.get('pot_10'))
            plot11 = float(form.cleaned_data.get('pot_11'))
            plot12 = float(form.cleaned_data.get('pot_12'))
            plot13 = float(form.cleaned_data.get('pot_13'))
            plot14 = float(form.cleaned_data.get('pot_14'))
            plot15 = float(form.cleaned_data.get('pot_15'))
            plot16 = float(form.cleaned_data.get('pot_16'))
            plot17 = float(form.cleaned_data.get('pot_17'))
            plot18 = float(form.cleaned_data.get('pot_18'))
            plot19 = float(form.cleaned_data.get('pot_19'))
            plot20 = float(form.cleaned_data.get('pot_20'))
            plot21 = float(form.cleaned_data.get('pot_21'))
            plot22 = float(form.cleaned_data.get('pot_22'))
            plot23 = float(form.cleaned_data.get('pot_23'))
            potreblenie=[plot0,plot1,plot2,plot3,plot4,plot5,plot6,plot7,plot8,plot9,plot10,plot11,plot12,plot13,plot14,plot15,plot16,plot17,plot18,plot19,plot20,plot21,plot22,plot23]
            prisoed_moshnost= int(form.cleaned_data.get('prisoed_moshnost_1'))
            kpd = float(form.cleaned_data.get('KPD_1'))
            tcikli_zar_i_raz = int(form.cleaned_data.get('tcikli_zar_i_raz_1'))
            Stoimost_emkosti_nakop = int(form.cleaned_data.get('Stoimost_emkosti_nakop_1'))
            Stoimost_podkl = int(form.cleaned_data.get('Stoimost_podkl_1'))
            pik_chasi1 = int(form.cleaned_data.get('pik_chasi_1'))
            pik_chasi2 = int(form.cleaned_data.get('pik_chasi_2'))
            pik_chasi3 = int(form.cleaned_data.get('pik_chasi_3'))
            pik_chasi4 =  int(form.cleaned_data.get('pik_chasi_4'))
            pik_chasi5 =  int(form.cleaned_data.get('pik_chasi_5'))
            pik_chasi6 =  int(form.cleaned_data.get('pik_chasi_6'))
            pik_chasi=[pik_chasi1,pik_chasi2,pik_chasi3,pik_chasi4,pik_chasi5,pik_chasi6]
            CK = int(form.cleaned_data.get('CK_1'))
            if prisoed_moshnost < 670:
                cat=1
            elif prisoed_moshnost >= 670 and prisoed_moshnost < 10000:
                cat=2
            else:
                cat=3
            prices1=[Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas0,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas1,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas2,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas3,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas4,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas5,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas6,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas7,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas8,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas9,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas10,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas11,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas12,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas13,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas14,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas15,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas16,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas17,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas18,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas19,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas20,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas21,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas22,Price.objects.get(category_of_prisoed_mosh=cat, category=3).chas23]
            prices2=[Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas0,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas1,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas2,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas3,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas4,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas5,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas6,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas7,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas8,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas9,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas10,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas11,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas12,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas13,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas14,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas15,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas16,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas17,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas18,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas19,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas20,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas21,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas22,Price.objects.get(category_of_prisoed_mosh=cat, category=4).chas23]
            prices3=[Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas0,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas1,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas2,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas3,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas4,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas5,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas6,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas7,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas8,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas9,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas10,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas11,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas12,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas13,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas14,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas15,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas16,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas17,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas18,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas19,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas20,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas21,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas22,Price.objects.get(category_of_prisoed_mosh=cat, category=5).chas23]
            prices4=[Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas0,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas1,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas2,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas3,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas4,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas5,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas6,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas7,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas8,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas9,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas10,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas11,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas12,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas13,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas14,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas15,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas16,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas17,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas18,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas19,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas20,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas21,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas22,Price.objects.get(category_of_prisoed_mosh=cat, category=6).chas23]
            prices=[prices1,prices2,prices3,prices4]
            Stoimost_PG = Price.objects.get(category_of_prisoed_mosh=cat, category=3).Stoimost_PG
            Stoimost_PT = Price.objects.get(category_of_prisoed_mosh=cat, category=4).Stoimost_PT
            print(Stoimost_PT,Stoimost_PG)
            answer,npv0pck,pck,moshnostnpv0pck,emkostnpv0pck,npvpck,emkostmaxnpvpck,moshnostmaxnpvpck,npv0sck,sck,emkostnpv0sck,moshnostnpv0sck,npvsck,emkostmaxnpvsck,moshnostmaxnpvsck =ver7_11_1(potreblenie,prisoed_moshnost,kpd,tcikli_zar_i_raz,Stoimost_emkosti_nakop,Stoimost_PG,Stoimost_PT,Stoimost_podkl,pik_chasi,CK,prices)
            print(answer,npv0pck,pck,moshnostnpv0pck,emkostnpv0pck,npvpck,emkostmaxnpvpck,moshnostmaxnpvpck,npv0sck,sck,emkostnpv0sck,moshnostnpv0sck,npvsck,emkostmaxnpvsck,moshnostmaxnpvsck)
            return render(request,'nakopitel/main.html', {'answer': answer, "npv0pck":npv0pck,"pck":pck,'emkostnpv0pck':emkostnpv0pck,'emkostnpv0sck':emkostnpv0sck,'moshnostnpv0pck':moshnostnpv0pck,'npvpck':npvpck,'emkostmaxnpvpck':emkostmaxnpvpck,"moshnostmaxnpvpck":moshnostmaxnpvpck,'npvsck':npvsck,'sck':sck,'CK1':CK+2,'npv0sck':npv0sck,'moshnostnpv0sck':moshnostnpv0sck,'emkostmaxnpvsck':emkostmaxnpvsck,'moshnostmaxnpvsck':moshnostmaxnpvsck,"CK":CK})
    return render(request, 'nakopitel/main.html', {'answer':":",'npv':-1,'pck':-1,'emkostnpv0pck':-1,'moshnostnpv0pck':-1,'moshnostmaxnpvpck':-1,'emkostmaxnpvpck':-1})
# Create your views here.
def hello(request):
    return HttpResponse('Hello World!')

def home(request):
    return render_to_response('nakopitel/index.html', {'variable': 'world'})