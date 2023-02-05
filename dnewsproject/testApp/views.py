from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'testApp/index.html')

def movies_view(request):
    head_msg = 'Durga Movies Information'
    sub_msg1 = 'RRR ready to release'
    sub_msg2 = 'Background support must be required to get oppurtinity'
    sub_msg3 = 'Indian Cine industry is struggling due to COVID'
    sub_msg4 = 'Biggest Benefit of COVID is OTT'
    sub_msg5 =  'Django movie is next big'
    my_dict = {'head_msg': head_msg, 'sub_msg1': sub_msg1, 'sub_msg2':sub_msg2,
    'sub_msg3':sub_msg3, 'sub_msg4':sub_msg4, 'sub_msg5':sub_msg5}
    return render(request, 'testApp/movies.html', my_dict)

def sports_view(request):
    head_msg = 'Sports Information'
    sub_msg1 = 'Now we have 2 Indian Team for International Cricket'
    sub_msg2 = 'SriLanka blaming India to send 2nd grade team'
    sub_msg3 = 'Population is 130 crores and medals very less'
    sub_msg4 = 'Sport need a big boost'
    sub_msg5 = 'Expecting many more Gold for India'
    my_dict = {'head_msg': head_msg, 'sub_msg1': sub_msg1, 'sub_msg2':sub_msg2,
    'sub_msg3':sub_msg3, 'sub_msg4':sub_msg4, 'sub_msg5':sub_msg5}
    return render(request, 'testApp/sports.html', my_dict)


def politics_view(request):
    head_msg = 'Politics Information'
    sub_msg1 = 'Election time is around the corner'
    sub_msg2 = 'COVID cases are on the rise'
    sub_msg3 = 'Politics over COVID has started again'
    sub_msg4 = 'Booster dose needs to be extended to kids and youth under 20'
    sub_msg5 = 'Masking mandated may be back'
    my_dict = {'head_msg': head_msg, 'sub_msg1': sub_msg1, 'sub_msg2':sub_msg2,
    'sub_msg3':sub_msg3, 'sub_msg4':sub_msg4, 'sub_msg5':sub_msg5}
    return render(request, 'testApp/politics.html', my_dict)
