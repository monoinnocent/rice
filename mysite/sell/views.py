from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Sum
from .models import LineSell

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def selldatatables(request):
    return render(request, 'sell/sell-datatables.net.html')

def sellcreate(request):
    return render(request, 'sell/sell-create.html')

def sellview(request):
    return render(request, 'sell/sell-view.html')

def sellviewcreate(request):
    return render(request, 'sell/sell-view-create.html')

def sellviewdata(request):
    return render(request, 'sell/sell-view-data.html')

def sellviewedit(request):
    return render(request, 'sell/sell-view-edit.html')

def selltimeseries(request):
    months = ['January', 'February', 'March', 'April', 'May', \
        'June', 'July', 'August', 'September', 'October', 'November', 'December']
    line_sell_list = {}
    line_sell_count = []

    for year in range(2014, 2018):
        for month in range(1, 13):
            line_sell_monthly_count = LineSell.objects.filter(sell_date__year=year, sell_date__month=month).aggregate(Sum('sell_amount'))['sell_amount__sum']
            line_sell_count.append(line_sell_monthly_count)
    
    line_sell_list[2018] = predictSale(line_sell_count)
    print(line_sell_list)

    return render(request, 'sell/sell-timeseries.net.html', {'months': months, 'line_sell_list': line_sell_list})
    # print(sell)
    # return render(request, 'sell/sell-timeseries.net.html')

# Predict Sale by year
def predictSale(line_sell_list):
    alpha = 0.15
    beta = 0.08
    gamma = 0.39
    value = line_sell_list
    print(value)

    ls = int(0)
    yl = int(0)

    mad_avg  = int(0)
    mape_avg = int(0)

    sl = []
    at = []
    bt = []
    st = []
    ft = []
    pd = []
    st_pd = []

    mad  = []
    mape = []

    count_at = int(1)
    count_bt = int(0)
    count_st = int(13)
    count_stl = int(0)

    #LS
    for l in range(12):
        ls += value[l]
    ls = ls/12
    print("Ls: ", ls)

    #Yl+t-Yt
    for y in range(0, 12, 1):
        yl += value[12+y]-value[0+y]
    print("Yl+t-Yt: ", yl)

    #Bs
    yl = yl/12**2
    print("Bs: ", yl)

    #Sl
    for s in range(0, 12, 1):
        sl.insert(s, value[s]/ls)
    print("St-L+m: ", sl)

    print(" ")

    #At
    at.insert(0, alpha*(value[12]/sl[0])+(1-alpha)*(ls+yl))

    #bt
    bt.insert(0, beta*(at[0]-ls)+(1-beta)*yl)

    #st
    st.insert(0, gamma*(value[12]/at[0])+(1-gamma)*(sl[0]))

    #At
    for atl in range(13, 24, 1):
        at.insert(count_at, alpha*(value[atl]/sl[count_at])+(1-alpha)*(at[count_at-1]+bt[count_at-1]))
        

        #bt
        bt.insert(count_bt+1, beta*(at[count_bt+1]-at[count_bt])+(1-beta)*bt[count_bt])
        count_bt += 1

        #st
        st.insert(count_at, gamma*(value[count_st]/at[count_at])+(1-gamma)*(sl[count_at]))
        count_st += 1
        count_at += 1


    #At2
    for atl in range(24, len(value), 1):
        at.insert(count_at, alpha*(value[atl]/st[count_stl])+(1-alpha)*(at[count_at-1]+bt[count_at-1])) 

        #bt2
        bt.insert(count_bt+1, beta*(at[count_bt+1]-at[count_bt])+(1-beta)*bt[count_bt])
        count_bt += 1

        #st2
        st.insert(count_at, gamma*(value[count_st]/at[count_at])+(1-gamma)*(st[count_stl]))
        count_st += 1
        count_at += 1
        count_stl += 1

    #Ft
    #print("ls", ls)
    #print("yl", yl)
    #print("st", st)


    ft.insert(0, (ls+yl)*st[0])
    for j in range(0, len(value)-13, 1):
        ft.insert(j+1, (at[j]+bt[j])*st[j+1])




    #print
    for i in range(0, len(value)-12, 1):   
        print("Period:", 13+i, "| Y: ", value[i+12], "| At:", at[i], "| bt:", bt[i], "| St:", st[i], "| ft:", ft[i], "| mad:", abs(value[i+12]-ft[i]), "| mape:",(abs(value[i+12]-ft[i])*100)/value[i+12] )
        mad.insert(i, abs(value[i+12]-ft[i]))
        mape.insert(i, (mad[i]*100)/value[i+12])
        
    print(" ")

    #mad average
    for m in mad:
        mad_avg += m
    print("mad avg: ", (mad_avg/len(mad)))

    #mape average
    for ma in mape:
        mape_avg += ma
    mape_avg = mape_avg/len(mape)  
    print("mape avg: ", mape_avg)
    print("len mape avg: ", len(mape))

    #beta alpha gamma
    print("Alpha: ", alpha, "| Beta", beta, "| Gamma: ", gamma )

    print(" ")

    #predict
    for m in range(len(st)-1, len(st)-13, -1):
        st_pd.insert(0, (st[m]))
        pd.insert(0, (at[len(at)-1]+bt[len(bt)-1])*st[m])

    predict_line_sell = []
    for j in range(0, 12, 1):
        predict_line_sell.append(pd[j])
    
    return predict_line_sell
