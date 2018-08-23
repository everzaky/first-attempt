from django.shortcuts import render
from .forms import Postprice
from .models import Price
import sqlite3 as lite
import sys
from django.shortcuts import redirect

def index(request):
    f = Postprice()
    if request.method == 'POST':
        form = Postprice(request.POST)
        if form.is_valid():
            plot0 = int(form.cleaned_data.get('pot_0'))
            plot1 = int(form.cleaned_data.get('pot_1'))
            plot2 = int(form.cleaned_data.get('pot_2'))
            plot3 = int(form.cleaned_data.get('pot_3'))
            plot4 = int(form.cleaned_data.get('pot_4'))
            plot5 = int(form.cleaned_data.get('pot_5'))
            plot6 = int(form.cleaned_data.get('pot_6'))
            plot7 = int(form.cleaned_data.get('pot_7'))
            plot8 = int(form.cleaned_data.get('pot_8'))
            plot9 = int(form.cleaned_data.get('pot_9'))
            plot10 = int(form.cleaned_data.get('pot_10'))
            plot11 = int(form.cleaned_data.get('pot_11'))
            plot12 = int(form.cleaned_data.get('pot_12'))
            plot13 = int(form.cleaned_data.get('pot_13'))
            plot14 = int(form.cleaned_data.get('pot_14'))
            plot15 = int(form.cleaned_data.get('pot_15'))
            plot16 = int(form.cleaned_data.get('pot_16'))
            plot17 = int(form.cleaned_data.get('pot_17'))
            plot18 = int(form.cleaned_data.get('pot_18'))
            plot19 = int(form.cleaned_data.get('pot_19'))
            plot20 = int(form.cleaned_data.get('pot_20'))
            plot21 = int(form.cleaned_data.get('pot_21'))
            plot22 = int(form.cleaned_data.get('pot_22'))
            plot23 = int(form.cleaned_data.get('pot_23'))
            potreblenie=[plot0,plot1,plot2,plot3,plot4,plot5,plot6,plot7,plot8,plot9,plot10,plot11,plot12,plot13,plot14,plot15,plot16,plot17,plot18,plot19,plot20,plot21,plot22,plot23]
            prisoed_moshnost= int(form.cleaned_data.get('prisoed_moshnost_1'))
            kpd = float(form.cleaned_data.get('KPD_1'))
            tcikli_zar_i_raz = int(form.cleaned_data.get('tcikli_zar_i_raz_1'))
            Stoimost_emkosti_nakop = int(form.cleaned_data.get('Stoimost_emkosti_nakop_1'))
            Stoimost_PG =  int(form.cleaned_data.get('Stoimost_PG_1'))
            Stoimost_PT = int(form.cleaned_data.get('Stoimost_PT_1'))
            Stoimost_podkl = int(form.cleaned_data.get('Stoimost_podkl_1'))
            pik_chasi1 = int(form.cleaned_data.get('pik_chasi_1'))
            pik_chasi2 = int(form.cleaned_data.get('pik_chasi_2'))
            pik_chasi3 = int(form.cleaned_data.get('pik_chasi_3'))
            pik_chasi4 =  int(form.cleaned_data.get('pik_chasi_4'))
            pik_chasi5 =  int(form.cleaned_data.get('pik_chasi_5'))
            pik_chasi6 =  int(form.cleaned_data.get('pik_chasi_6'))
            CK = int(form.cleaned_data.get('CK_1'))
            if prisoed_moshnost < 670:
                cat=1
            elif prisoed_moshnost >= 670 and prisoed_moshnost < 10000:
                cat=2
            else:
                cat=3
#            #Energy_prices=[Price.objects.get(category_of_prisoed_mosh=cat, category=3).price_po_chas,Price.objects.get(category_of_prisoed_mosh=cat, category=4).price_po_chas,Price.objects.get(category_of_prisoed_mosh=cat, category=5).price_po_chas,Price.objects.get(category_of_prisoed_mosh=cat, category=6).price_po_chas]
 #           con = lite.connect('db.sqlite3')
  #          with con:
   #             cur = con.execute("SELECT * FROM NAKOPITEL ") """
            return render(request,'nakopitel/main.html', {'result': 1})
    return render(request, 'nakopitel/main.html', {'result':0})

# Create your views here.