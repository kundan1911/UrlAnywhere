from django.shortcuts import render,redirect
from django.http import HttpResponse
import uuid
from django.contrib.auth.models import User
# Create your views here.
from .models import LongtoShort,UserProfile
#when the following is called it responses with an string using the httpResponsemodule

def hw(req):
    return HttpResponse("hello")

def generate_user_id():
    user_id = uuid.uuid4().hex
    return user_id

def login_page(req):
    contxt=False
    print(req.session)
    if req.method=="POST":
        data=req.POST
        print(data)
        usrname=data["username"]
        passwrd=data["password"]
        userExist=UserProfile.objects.filter(userName=usrname);
        if len(userExist) == 0: 
            # try :
            _id=generate_user_id()
            print('current user id',_id)
            # if req.session.get('userId',""):
            req.session['userId']= _id
            usr = UserProfile(user_id=_id,userName=usrname, password=passwrd)
            
            usr.save();
            return redirect(home_page)
            # except:
            #     print("error in creating a user");
        else:
            curr_user=UserProfile.objects.filter(userName=usrname)
            
            if passwrd == curr_user[0].password:
                current_user_id=curr_user[0].user_id
                print('current user id',current_user_id)
                req.session['userId']= current_user_id
                return redirect(home_page)
            else :
                contxt=True
                print("wrong password")
    context={'invalid':False}
    if contxt==True:
        context['invalid']=True
    return render(req,'login.html',context);

#request contains all the information about the activity happen on the URL
#post,get as per the action on the particular endpoint
#req.post provide the detail entered on the form with an particular csrftoken
def home_page(req):
    # print(req.META)
    context={'submitted':False,'repeatAlias':False}
    user_agent = req.META.get('HTTP_USER_AGENT', '')
    print("agent",user_agent);
    # curr_user=UserProfile.objects.filter(userName=usrname);
    print(req.session.get('userId'))
    if req.method=="POST":
        data=req.POST
        longurl=data['longurl']
        #the url on which the page is rendered is the build_absolute_uri()
        # customurl=req.build_absolute_uri()+ data['custom_name']
        customurl=data['custom_name']
        print(req.build_absolute_uri().rsplit('/', 1)[0] + '/'+customurl)
        try:
            
            context['long_url']=longurl
            context['short_url']=req.build_absolute_uri().rsplit('/', 1)[0] + '/'+customurl

            currentShrtTolong=LongtoShort.objects.filter(user_id=req.session.get('userId'),custom_name=customurl);
            if len(currentShrtTolong)==0:
                obj=LongtoShort(user_id=req.session.get('userId'),long_url=longurl,custom_name=customurl)
                obj.save()
                context['submitted']=True
                context['clickCount']=obj.clicks
                context['date']=obj.date
            else:
                context={"repeatAlias":True}

        except:
            print("error")
            context={"repeatAlias":True}
           
    else:
        print("haven't submit the form")
    #render(request,file_to_render,data_from_model)
    #the render method searches for the html page in the templates folder automatically
    all_urls=LongtoShort.objects.filter(user_id=req.session.get('userId'))
    if len(all_urls) > 0:
        context['submitted']=True
        context['entries']=all_urls
    return render(req,"index.html",context)

def redirect_view(req,dynamicEndPnt):
    print(dynamicEndPnt);
    currentShrtTolong=LongtoShort.objects.filter(user_id=req.session.get('userId'),custom_name=dynamicEndPnt);
   
    if len(currentShrtTolong)==0:
        return HttpResponse("shorturl does not exist")
    else:
        entry=currentShrtTolong[0];
        entry.clicks=entry.clicks+1;
        entry.save();
        print(entry.long_url);

        return redirect(entry.long_url)
    
def specificAnalytic(req,dynamicEndPnt):
    print("In specific slug call",dynamicEndPnt)
    currentShrtTolong=LongtoShort.objects.filter(user_id=req.session.get('userId'),custom_name=dynamicEndPnt);
    if len(currentShrtTolong)==0:
        return HttpResponse("shorturl does not exist")
    else:
        entry=currentShrtTolong[0];
        # entry.clicks=entry.clicks+1;
        # entry.save();
        print("In ",entry.custom_name)
        context={
            "data":entry.date,
            "long_url":entry.long_url,
            "short_url":entry.custom_name,
            "clickCount":entry.clicks
        }
        return render(req,'analytics.html',context)



def allAnalyticsPage(req):
    allEntry=LongtoShort.objects.filter(user_id=req.session.get('userId'))
    for i in allEntry:
        print(i.custom_name)
    return render(req,'all-analytics.html',{"entries":allEntry})

