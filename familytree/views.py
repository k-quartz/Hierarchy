from django.shortcuts import render, redirect
from django.http import HttpResponse
from familytree.models import Member, RelationType, MemberPrt, Products
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.views.generic import CreateView, UpdateView
from django.forms.models import model_to_dict
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os


def index(request):
    return render(request, 'familytree/main.html')


def member(request):
    return render(request, 'familytree/member.html')


class CreateMemberView(CreateView):
    model = Member
    fields = ['fname', 'mname', 'lname', 'mobile1', 'email', 'mem_img']

    def form_valid(self, form):
        return super().form_valid(form)


def DisplayMember(request):
    if request.user.is_authenticated:
        memblist = Products.objects.all()
        page = request.GET.get('page', 1)

        paginator = Paginator(memblist, 10)
        try:
            members = paginator.page(page)
        except PageNotAnInteger:
            members = Paginator.page(1)
        except EmptyPage:
            members = paginator.page(paginator.num_pages)

        return render(request, "familytree/display_member.html", {"data": members})
    else:
        return render(request, 'users/login.html')


def DisplayMemberP(request, curpg):
    request.session['curpg'] = curpg
    return redirect('display-member')


def success(request):
    fname = request.POST["fname"]
    mname = request.POST["mname"]
    lname = request.POST["lname"]
    emailadd = request.POST["emailadd"]
    mobile = request.POST["mobile1"]
    memfile = request.FILES["myfile"]
    dob1 = request.POST["dob"]
    dob = datetime.strptime(dob1, "%Y-%m-%d").date()
    newMember = Member()

    newMember.agre = True
    newMember.reject = True
    now = datetime.now()
    # print(now)
    newMember.memberdate = now.strftime('%Y-%m-%d')
    # newMember.time=now.strftime('%H:%M:%S')

    newMember.fname = fname
    newMember.mname = mname
    newMember.lname = lname
    newMember.email = emailadd
    newMember.mobile1 = mobile
    newMember.mem_img = newMember.newlocation(memfile.name)

    newMember.dob = dob
    newMember.save()

    os.makedirs(os.path.join("media", str(newMember.memberid)))
    finalname = str(newMember.memberid) + "/" + str(newMember.mem_img)

    fs = FileSystemStorage()
    fs.save(finalname, memfile)
    newMember.mem_img = finalname

    return render(request, 'familytree/success.html')


def updateMemberView(request, id):
    smemid = id
    selected_member = get_object_or_404(Member, memberid=smemid)

    member_list = MemberPrt.objects.all().filter(member_id=id)

    relation_list = RelationType.objects.all()
    return render(request, 'familytree/member_update_form.html', {"member": selected_member, "memberlist": member_list, "relationlist": relation_list})


# def displayModalView(request, fname, mname, lname):
def displayModalView(request):
    fname = request.GET['fname']
    mname = request.GET['mname']
    lname = request.GET['lname']
    memberid = request.GET['m_id']
    relationtypeid = request.GET['reltpid']

    filtered_list = Member.objects.all().filter(~Q(memberid=memberid))

    if(len(fname) > 0):
        filtered_list = filtered_list.filter(fname=fname)

    if(len(mname) > 0):
        filtered_list = filtered_list.filter(mname=mname)

    if(len(lname) > 0):
        filtered_list = filtered_list.filter(lname=lname)

    # filtered_list = Member.objects.all()
    return render(request, 'familytree/display_serch_member.html', {"fname": fname, "mname": mname, "lname": lname, "filtered_list": filtered_list, "m_id": memberid, "relationtypeid": relationtypeid})


def addFamily(request, mid, newid, reltypeid):
    memberprt = MemberPrt()
    memberprt.member_id = mid
    memberprt.relative_id = newid
    memberprt.relationtype_id = reltypeid
    memberprt.save()

    return redirect('update-member', id=mid)


def personalDetail(request, id):
    print("akash")
    member = Member.objects.filter(memberid=id)
    fname = member[0].fname
    lname = member[0].lname
    member_name = fname + " " + lname
    return render(request, "familytree/personal_detail.html", {"member_name": member_name})
