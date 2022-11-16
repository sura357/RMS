from django.shortcuts import render  # 這個可以引入從templates中取得html
from AppProject.models import *
from django.shortcuts import redirect
from django.http import HttpResponse
from datetime import datetime
from django.db import connection


# Create your views here.
def listone(request):
    try:
        unit = Test.objects.get(cName="Majjor2")  # 嘗試讀取Student裡面的資料
    except():
        errormessage = "(讀取錯誤!)"
    return render(request, "listone.html", locals())


def listall(request):
    tests = Test.objects.all().order_by('id')
    return render(request, "listall.html", locals())


"""def register(request):
    users = User.objects.all().order_by('id')
    registerform = form.RegisterForm(request.POST)  # 如為空白是建立一個空白的物件

    if "account" in request.session:
        template = "models/basesignup.html"
        mess = "Data Received !"
    else:
        template = "models/base.html"
        mess = "Data not found !"

    if request.method == "POST":
        if registerform.is_valid():  # 是否通過驗證
            name = registerform.cleaned_data['cName']
            account = registerform.cleaned_data['cAccount']
            password = registerform.cleaned_data['cPassword']
            sex = registerform.cleaned_data['cSex']
            birthday = registerform.cleaned_data['cBirthday']
            email = registerform.cleaned_data['cEmail']
            phone = registerform.cleaned_data['cPhone']
            addr = registerform.cleaned_data['cAddr']

            for user in users:
                if account == user.cAccount:
                    mess = "Account has been register already !"
                    return render(request, "register.html", locals())

            unit = User.objects.create(cName=name, cAccount=account, cPassword=password, cSex=sex, cBirthday=birthday, cEmail=email, cPhone=phone, cAddr=addr)

            unit.save()
            mess = "Register successful !"
        else:
            mess = " Wrong Data !"
    else:
        mess = "表單資料尚未送出.."
    return render(request, "register.html", locals())"""


def index(request):
    now = datetime.now()

    if "raccount" in request.session:
        template = "models/basesignup.html"
        mess = "raccount session exsist!"
        myuser = Rehabilitator.objects.get(id=request.session["raccount"])
    else:
        template = "models/base.html"
        mess = "LogOut!"
        return redirect('../login')

    return render(request, "admins/index.html", locals())


def login(request):
    now = datetime.now()
    template = "models/base.html"

    rusers = Rehabilitator.objects.all().order_by('id')
    pusers = Patient.objects.all().order_by('id')
    # loginform = form.LoginForm(request.POST)  # 如為空白是建立一個空白的物件
    if "raccount" in request.session:
        return redirect('../index')

    if request.method != "POST":
        mess = "表單資料尚未送出.."
        return render(request, "admins/login.html", locals())
    else:
        account = request.POST['cAccount']
        password = request.POST['cPassword']
        for ruser in rusers:
            if account != ruser.id:
                mess = "User not exist !"
            elif password != ruser.password:
                mess = "Password not correct !"
            else:
                request.session["raccount"] = account
                if request.session is not None:
                    myuser = Rehabilitator.objects.get(id=request.session["raccount"])
                    mess = "Data Received !"
                else:
                    mess = "Data not found !"
                return redirect('../index')

    return render(request, "admins/login.html", locals())


def logout(request):
    if "raccount" in request.session:
        request.session.clear()  # 刪除所有session
        request.session.flush()
        # del request.session["account"]  # 刪除單一Session
    return redirect('../login')


def select_patient(request):
    now = datetime.now()

    if "raccount" in request.session:
        template = "models/basesignup.html"
        mess = "raccount session exsist!"
        patients = Patient.objects.all().order_by('id')
        myuser = Rehabilitator.objects.get(id=request.session["raccount"])

    else:
        template = "models/base.html"
        mess = "LogOut!"
        return redirect('../login')

    return render(request, "admins/patients.html", locals())


def patient_view(request):
    if "raccount" in request.session:
        template = "models/basesignup.html"
        mess = "raccount session exsist!"
        if 'id' in request.POST:
            pid = request.POST["id"]

    else:
        template = "models/base.html"
        mess = "LogOut!"
        return redirect('../login')

    return render(request, "admins/patients_view.html", locals())


def plan_edit(request):
    if "raccount" in request.session:
        template = "models/basesignup.html"
        mess = "raccount session exsist!"
        if 'id' in request.POST:
            pid = request.POST["id"]
    else:
        template = "models/base.html"
        mess = "LogOut!"
        return redirect('../login')

    return render(request, "admins/plan_edit.html", locals())


def patient_register(request):
    if "raccount" in request.session:
        template = "models/basesignup.html"
        mess = "raccount session exsist!"
        if 'id' in request.POST:
            pid = request.POST["id"]
    else:
        template = "models/base.html"
        mess = "LogOut!"
        return redirect('../login')

    return render(request, "admins/patients_register.html", locals())


"""def userprofile(request):
    now = datetime.now()
    if "account" in request.session:
        # myuserfields = User._meta.fields
        myuser = User.objects.get(cAccount=request.session["account"])
        template = "models/basesignup.html"
        mess = "Data Received !"
    else:
        template = "models/base.html"
        mess = "Data not found !"
    return render(request, "userprofile.html", locals())


def deleteuser(request, id=None):
    users = User.objects.all().order_by('id')
    try:
        unit = User.objects.get(id=id)
        unit.delete()

        mess = "Delete complete!"
        # return redirect('/index/')  # 這個可以用 只是紅蟲
    except():
        mess = "Can't not read!"
    return redirect("../register.html")


def product(request):
    now = datetime.now()
    if "account" in request.session:
        template = "models/basesignup.html"
        mess = "Data Received !"
    else:
        template = "models/base.html"
        mess = "Data not found !"

    products = Product.objects.all().order_by('id')
    return render(request, "products.html", locals())


def product_detail(request, id=None):
    if "account" in request.session:
        template = "models/basesignup.html"
        mess = "Data Received !"
    else:
        template = "models/base.html"
        mess = "Data not found !"

    products = Product.objects.filter(id=id)
    return render(request, "product_detail.html", locals())


def buy(request, id=None):
    if "account" in request.session:
        template = "models/basesignup.html"
        mess = "Data Received !"
    else:
        template = "models/base.html"
        mess = "Data not found !"

    if request.method == "GET":
        account = request.session["account"]
        id = id
        name = Product.objects.values_list('pName', flat=True).filter(id=id)
        price = Product.objects.values_list('pPrice', flat=True).filter(id=id)

        buyproduct = Cart.objects.filter(pID=id).first()
        if buyproduct is None:
            amount = 1
            unit = Cart.objects.create(cAccount=account, pID=id, pName=name, pPrice=price, pAmount=amount)
            unit.save()
        else:
            buyproduct.pAmount += 1
            buyproduct.save()

        mess = "buy successful !"
    else:
        mess = "表單資料尚未送出.."

    # url = "../products"
    return render(request, "buy.html", locals())
    # return redirect(url)


def cart(request):
    if "account" in request.session:
        template = "models/basesignup.html"
        mess = "Data Received !"
    else:
        return redirect('../products')

    content = Cart.objects.filter(cAccount=request.session["account"])
    count = content.count()
    total = 0
    for i in content:
        total += i.pPrice

    return render(request, "cart.html", locals())


def orderconfirm(request):
    if "account" in request.session:
        template = "models/basesignup.html"
        if request.method == "POST":  # 如果是以POST方式才處理
            account = request.session["account"]
            fname = request.POST['Fname']  # 取得表單輸入資料，在網頁上也要寫入mess變數，而網頁傳過來的username Django也要命名'username'
            lname = request.POST['Lname']
            caddr = request.POST['cAddr']
            paymentmethod = request.POST['paymentMethod']
            creditnum = request.POST['creditnum']
            ccv = request.POST['CCV']
            total = 0

            deal = Cart.objects.all().filter(cAccount=account)
            theorder = Order.objects.all().order_by('id').first()
            oid = int(theorder.id)+1

            for i in deal:
                total += i.pPrice*i.pAmount
                pid = i.pID
                pname = i.pName
                pprice = i.pPrice
                pamount = i.pAmount
                unit = Odetail.objects.create(oID=oid, pID=pid, pName=pname, pPrice=pprice, pAmount=pamount)
                unit.save()

            unit = Order.objects.create(cAccount=account, pUpdate="2022-05-01", cFname=fname, cLname=lname, cAddr=caddr,
                                        cPayment=paymentmethod, cCreditnum=creditnum, cCCV=ccv, oTotal=total)
            unit.save()


            unit = Cart.objects.all().filter(cAccount=account)
            unit.delete()
            mess = "Data Received !"
        else:
            mess = "表單資料尚未送出.."

    else:
        return render(request, "orderconfirm.html", locals())

    return render(request, "orderconfirm.html", locals())


def orderprogress(request):
    if "account" in request.session:
        template = "models/basesignup.html"
        if request.method == "POST":  # 如果是以POST方式才處理
            mess = "Data Received !"
        else:
            mess = "表單資料尚未送出.."

    else:
        return render(request, "orderprogress.html", locals())

    return render(request, "orderprogress.html", loc
"""
def patient_Login(request):  # 缺登入疑慮，只有使用者可以登
    template = "models/patientbase.html"
    rusers = Rehabilitator.objects.all().order_by('id')
    pusers = Patient.objects.all().order_by('id')
    # loginform = form.LoginForm(request.POST)  # 如為空白是建立一個空白的物件
    if "raccount" in request.session:
        return redirect('../rehabilitator_Information')

    if "paccount" in request.session:
        return redirect('../patient_home')

    if request.method != "POST":
        mess = "表單資料尚未送出.."
    else:
        account = request.POST['cAccount']
        #  password = request.POST['cPassword']

        for ruser in rusers:
            if account != ruser.id:
                mess = "User not exist !"
            # elif password != ruser.password:
            #    mess = "Password not correct !"
            else:
                request.session["raccount"] = account
                if request.session is not None:
                    myuser = Rehabilitator.objects.get(id=request.session["raccount"])
                    mess = "Data Received !"
                else:
                    mess = "Data not found !"
                return redirect('../patient_Login')

        for puser in pusers:
            if account != puser.id:
                mess = "User not exist !"
            else:
                request.session["paccount"] = account
                if request.session is not None:
                    myuser = Patient.objects.get(id=request.session["paccount"])
                    mess = "Data Received !"
                else:
                    mess = "Data not found !"
                return redirect('../patient_home')

    return render(request, "patient_Login.html", locals())


def logout(request):
    if "raccount" in request.session:
        request.session.clear()  # 刪除所有session
        request.session.flush()
        # del request.session["account"]  # 刪除單一Session
    return redirect('../patient_Login')


def patient_home(request):
    template = "models/patientbase.html"
    return render(request, "patient_home.html", locals())


def patient_Information(request):
    template = "models/patientbase.html"
    return render(request, "patient_Information.html", locals())


def patient_medicalrecord(request):
    template = "models/patientbase.html"
    return render(request, "patient_medicalrecord.html", locals())


def patient_rehubrecord(request):
    template = "models/patientbase.html"
    return render(request, "patient_rehubrecord.html", locals())


###################################
def rehabilitator_Information(request):
    template = "models/rehabilitatorbase.html"
    if "raccount" not in request.session:
        return redirect('../patient_Login')
    rid = Rehabilitator.objects.get(id=request.session["raccount"])
    return render(request, "rehabilitator_Information.html", locals())


def rehabilitator_addPlan(request):
    template = "models/rehabilitatorbase.html"
    if "raccount" not in request.session:
        return redirect('../patient_Login')
    rid = Rehabilitator.objects.get(id=request.session["raccount"])

    # patients = MedicalRecord.objects.filter(rID_id=request.session["raccount"])
    cursor = connection.cursor()
    cursor.execute("select distinct name, id from AppProject_patient "
                   "WHERE id=(SELECT pID_id FROM AppProject_medicalrecord WHERE rID_id='" + request.session["raccount"] + "')")

    patients = cursor.fetchall()  # cursor.fetchone()[0]
    # print(patients)

    """    cursor = connection.cursor()
    cursor.execute("select * from AppProject_motion")

    motions = cursor.fetchall()  # cursor.fetchone()[0]"""
    motions = Motion.objects.all()

    if motions is not None:
        print(motions)

    if request.method != "GET":
        mess = "表單資料尚未送出.."
    else:
        sel_patient = request.GET.get('sel_patient')
        sel_plan = request.GET.get('sel_plan')
        sel_date = request.GET.getlist('selectedDate[]')
        set_details = request.GET.getlist('set_detail[]')
        plan_name = request.GET.get('planName')
        planid = request.GET.get('planid')
        # aa = request.GET.get('aa')
        """data = json.loads(request.GET.get('aa'))

        print(data)"""

        if sel_patient is not None and sel_patient != "" and sel_patient != "None":
            # print(sel_patient)
            cursor.execute("select distinct * from AppProject_patient "
                           "WHERE id= '"+sel_patient+"'")
            sel_patient_name = cursor.fetchall()  # cursor.fetchone()[0]
            print(sel_patient_name)
            print(sel_date)
            print(set_details)
            print(plan_name)
            print(planid)
            #print(set_details[1])
            #print(set_details[1][1])
            # print(aa)
            cursor.execute("SELECT max(planID) "
                           "from AppProject_plan")
            top_planid = cursor.fetchall()  # cursor.fetchone()[0]
            print(top_planid[0][0])

            top_planidnum = int(top_planid[0][0])+1

            if planid != -1:
                top_planidnum=planid

            for j in range(0, len(sel_date)):
                temp = 0
                if set_details[j] is "null":
                    continue
                set_details_split = set_details[j].split(',')
                print(len(set_details_split))
                set_len = len(set_details_split)/6
                for i in range(0, int(set_len)):
                    cursor = connection.cursor()
                    temp += 1
                    print(set_details_split)
                    cursor.execute(
                        "INSERT INTO AppProject_plansetdetail(id,duration,times,breadtime,ontop_duration,type,motion_time)"
                        "VALUES (NULL, '" + set_details_split[i*6+3] + "','" + set_details_split[i*6+1] + "','" + set_details_split[i*6+2] + "','" + set_details_split[i*6+3] + "','" + set_details_split[i*6+4] + "','" + set_details_split[i*6+5] + "')")

                    cursor.execute("insert into AppProject_plansetmotion(id, mID_id, sdID_id) "
                                   "VALUES(NULL, '"+set_details_split[i*6]+"',(SELECT last_insert_rowid()))")

                    temp_date = sel_date[j][0:4] + "-" + sel_date[j][4:6] + "-" + sel_date[j][6:8]
                    cursor.execute("insert into AppProject_planset(id, SetID, smID_id) "  # orders
                                   "VALUES(NULL, '" + temp_date + "', (SELECT last_insert_rowid()))")  # "+str(temp)+"

                    cursor.execute("insert into AppProject_plan(id, planID, creating_date, setID_id, planName) "
                                   "VALUES("
                                   "NULL, "
                                   "" + str(top_planidnum) + ", "
                                   "date('now','localtime'), "
                                   "(SELECT last_insert_rowid()), '" + plan_name + "')")

            cursor.execute("INSERT INTO AppProject_medicalrecord"
                           "(id, creating_date, disease, symptom, status, pID_id, planID_id, rid_id, remark)"
                           "VALUES(NULL, date('now','localtime'), '', '', 0, '" + sel_patient + "', " + str(top_planidnum) + ", '" + rid.id + "', 'aa');")

            return redirect('../rehabilitator_CheckPlan/?sel_patient=' + sel_patient)
        else:
            return redirect('../rehabilitator_CheckPlan/?sel_patient='+sel_patient)

    return render(request, "rehabilitator_addPlan.html", locals())


def rehabilitator_checkPlan(request):
    template = "models/rehabilitatorbase.html"
    if "raccount" not in request.session:
        return redirect('../patient_Login')
    rid = Rehabilitator.objects.get(id=request.session["raccount"])


    # patients = MedicalRecord.objects.filter(rID_id=request.session["raccount"])
    cursor = connection.cursor()
    cursor.execute("select distinct name , id from AppProject_patient "
                   "WHERE id=(SELECT pID_id FROM AppProject_medicalrecord WHERE rID_id='"+request.session["raccount"]+"')")

    patients = cursor.fetchall()  # cursor.fetchone()[0]
    # print(patients)
    motions = Motion.objects.all()

    if request.method != "GET":
        mess = "表單資料尚未送出.."
    else:
        sel_patient = request.GET.get('sel_patient')
        sel_plan = request.GET.get('sel_plan')

        if sel_patient is not None and sel_patient != "":
            # print(sel_patient)
            cursor.execute("select distinct * from AppProject_patient "
                           "WHERE id= '"+sel_patient+"'")
            sel_patient_name = cursor.fetchall()  # cursor.fetchone()[0]
            # print(sel_patient_name)

            cursor.execute("select distinct planID_id "
                            "from AppProject_medicalrecord "
                            "WHERE pID_id ='"+sel_patient+"'")
            plans = cursor.fetchall()  # cursor.fetchone()[0]

            # plans = MedicalRecord.objects.filter(pID_id=sel_patient)
            # print(plans)

        # print(request.GET.get('sel_plan'))
        if sel_plan is not None and sel_plan != "":
            cursor.execute("SELECT planName,planID from AppProject_plan WHERE planID == '" + sel_plan + "'")
            plan_name = cursor.fetchall()  # cursor.fetchone()[0]
            print(plan_name)

            cursor.execute("select distinct SetID "
                           " from AppProject_planset "
                           " WHERE id in (SELECT setID_id from AppProject_plan WHERE planID == '"+sel_plan+"')")
            plans_sets = cursor.fetchall()  # cursor.fetchone()[0]
            print(plans_sets)

            cursor.execute("select * "
                           " from AppProject_planset, AppProject_plansetmotion, AppProject_motion "
                           " where AppProject_planset.smID_id = AppProject_plansetmotion.id "
                           " and AppProject_plansetmotion.mID_id = AppProject_motion.id "
                           " and AppProject_planset.id"
                           " in (SELECT setID_id from AppProject_plan WHERE planID == '"+sel_plan+"')")
            sets_content = cursor.fetchall()  # cursor.fetchone()[0]
            print(sets_content)
            cursor.execute("select * "
                           " from AppProject_planset, AppProject_plansetmotion, AppProject_motion, AppProject_plansetdetail "
                           " where AppProject_planset.smID_id = AppProject_plansetmotion.id "
                           " and AppProject_plansetmotion.mID_id = AppProject_motion.id "
                           " and AppProject_plansetmotion.sdID_id = AppProject_plansetdetail.id"
                           " and AppProject_planset.id"
                           " in (SELECT setID_id from AppProject_plan WHERE planID == '" + sel_plan + "')")
            sd_contents = cursor.fetchall()  # cursor.fetchone()[0]
            print(sd_contents)

        #  password = request.POST['cPassword']
    return render(request, "rehabilitator_checkPlan.html", locals())


def rehabilitator_contactrecord(request):
    template = "models/rehabilitatorbase.html"
    if "raccount" not in request.session:
        return redirect('../patient_Login')
    rid = Rehabilitator.objects.get(id=request.session["raccount"])

    # patients = MedicalRecord.objects.filter(rID_id=request.session["raccount"])
    cursor = connection.cursor()
    cursor.execute("select name , id from AppProject_patient "
                   "WHERE id=(SELECT pID_id FROM AppProject_medicalrecord WHERE rID_id='"+request.session["raccount"]+"')")

    patients = cursor.fetchall()  # cursor.fetchone()[0]
    # print(patients)

    if request.method != "POST":
        mess = "表單資料尚未送出.."
    else:
        sel_patient = request.POST['sel_patient']
        # print(sel_patient)
        cursor.execute("select distinct * from AppProject_patient "
                       "WHERE id= '" + sel_patient + "'")
        sel_patient_name = cursor.fetchall()  # cursor.fetchone()[0]
        # print(sel_patient_name)

        if sel_patient is not None and sel_patient != "":
            if 'message' in request.POST:
                messages = request.POST['message']
                # print(messages)
                cursor.execute("INSERT INTO AppProject_contactrecord (id, send_time, content, pID_id, rid_id) "
                               "VALUES (NULL, date('now','localtime'), '" + messages + "', '" + sel_patient + "', '" +
                               request.session["raccount"] + "')")

        #  password = request.POST['cPassword']

    return render(request, "rehabilitator_contactrecord.html", locals())


def rehabilitator_rentalrecords(request):
    template = "models/rehabilitatorbase.html"
    if "raccount" not in request.session:
        return redirect('../patient_Login')
    rid = Rehabilitator.objects.get(id=request.session["raccount"])

    # patients = MedicalRecord.objects.filter(rID_id=request.session["raccount"])
    cursor = connection.cursor()
    cursor.execute("select name , id from AppProject_patient "
                   "WHERE id=(SELECT pID_id FROM AppProject_medicalrecord WHERE rID_id='"+request.session["raccount"]+"')")

    patients = cursor.fetchall()  # cursor.fetchone()[0]
    #print(patients)

    kinects = KinectStatus.objects.filter(status=1)
    kinect_amount = kinects.count()
    print(kinects)

    if request.method != "GET":
        mess = "表單資料尚未送出.."
    else:
        sel_kinect = request.GET.get('sel_kinect')
        sel_patient = request.GET.get('sel_patient')
        sel_date = request.GET.get('sel_date')
        period = request.GET.get('period')
        """print("sel_kinect:"+sel_kinect)
        print("sel_patient:"+sel_patient)
        print("sel_date:"+sel_date)
        print("period:"+period)"""
        # print(sel_patient)

        if sel_kinect is not None and sel_kinect != "":
            cursor.execute("INSERT INTO AppProject_rentalrecords(id,startingdate,duration,status,kID_id,pID_id)"
                            "VALUES (NULL ,'"+sel_date+"', "+period+", 0, "+sel_kinect+", '"+sel_patient+"')")

            cursor.execute("UPDATE AppProject_kinectstatus SET status = '1'"
                           "WHERE id = "+sel_kinect+"")


        #  password = request.POST['cPassword']
    return render(request, "rehabilitator_rentalrecords.html", locals())


def rehabilitator_rentalback(request):
    template = "models/rehabilitatorbase.html"
    if "raccount" not in request.session:
        return redirect('../patient_Login')
    rid = Rehabilitator.objects.get(id=request.session["raccount"])

    # patients = MedicalRecord.objects.filter(rID_id=request.session["raccount"])
    cursor = connection.cursor()
    cursor.execute("select name , id from AppProject_patient "
                   "WHERE id=(SELECT pID_id FROM AppProject_medicalrecord WHERE rID_id='" + request.session[
                       "raccount"] + "')")

    patients = cursor.fetchall()  # cursor.fetchone()[0]
    # print(patients)

    kinects = KinectStatus.objects.filter(status=1)
    kinect_amount = kinects.count()
    print(kinects)

    if request.method != "GET":
        mess = "表單資料尚未送出.."
    else:
        sel_kinect = request.GET.get('sel_kinect')
        print("sel_kinect:"+sel_kinect)
        """print("sel_patient:"+sel_patient)
        print("sel_date:"+sel_date)
        print("period:"+period)"""
        # print(sel_patient)

        if sel_kinect is not None and sel_kinect != "":
            cursor.execute("UPDATE AppProject_kinectstatus SET status = '0'"
                           "WHERE id = " + sel_kinect + "")

        #  password = request.POST['cPassword']
    return render(request, "rehabilitator_rentalback.html", locals())

def rehabilitator_rehubrecord(request):
    template = "models/rehabilitatorbase.html"
    if "raccount" not in request.session:
        return redirect('../patient_Login')
    rid = Rehabilitator.objects.get(id=request.session["raccount"])
    cursor = connection.cursor()
    cursor.execute("select name , id from AppProject_patient "
                   "WHERE id=(SELECT pID_id FROM AppProject_medicalrecord WHERE rID_id='"+request.session["raccount"]+"')")

    patients = cursor.fetchall()  # cursor.fetchone()[0]

    if request.method != "POST":
        mess = "表單資料尚未送出.."
    else:
        sel_patient = request.POST['sel_patient']

        cursor = connection.cursor()
        cursor.execute("select distinct * from AppProject_patient "
                       "WHERE id= '" + sel_patient + "'")
        sel_patient_name = cursor.fetchall()  # cursor.fetchone()[0]
        rehubrecordquery = f"""
        SELECT ps.SetID, rr.times,rr.duration, rr.accuracy ,rr.progress, p.planName
        FROM AppProject_rehubrecord rr
            LEFT JOIN AppProject_planset ps ON rr.sid_id = ps.id
            LEFT JOIN AppProject_plansetmotion psm ON ps.smID_id = psm.id
            LEFT JOIN AppProject_plansetdetail psd ON psm.sdID_id = psd.id
            LEFT JOIN AppProject_motion m ON m.id = psm.mID_id
            LEFT JOIN AppProject_plan p ON ps.id = p.setID_id
            LEFT JOIN AppProject_medicalrecord mr ON  p.planID = mr.planID_id
        WHERE mr.pID_id = '{sel_patient}' & rr.accuracy is not NULL
        """
        cursor.execute(rehubrecordquery)

        records = cursor.fetchall()  # cursor.fetchone()[0]
        print(records)
    return render(request, "rehabilitator_rehubrecord.html", locals())


def rehabilitator_medicalrecord(request):
    template = "models/rehabilitatorbase.html"
    if "raccount" not in request.session:
        return redirect('../patient_Login')
    rid = Rehabilitator.objects.get(id=request.session["raccount"])
    cursor = connection.cursor()
    cursor.execute("select name , id from AppProject_patient "
                   "WHERE id=(SELECT pID_id FROM AppProject_medicalrecord WHERE rID_id='"+request.session["raccount"]+"')")

    patients = cursor.fetchall()  # cursor.fetchone()[0]

    if request.method != "POST":
        mess = "表單資料尚未送出.."
    else:
        sel_patient = request.POST['sel_patient']
        records = MedicalRecord.objects.filter(pID_id=sel_patient)
        cursor.execute("select distinct * from AppProject_patient "
                       "WHERE id= '" + sel_patient + "'")
        sel_patient_name = cursor.fetchall()  # cursor.fetchone()[0]
    """
    cursor = connection.cursor()
    cursor.execute("select name , id from AppProject_patient "
                   "WHERE id=(SELECT pID_id FROM AppProject_medicalrecord WHERE rID_id='"+request.session["raccount"]+"')")

    patients = cursor.fetchall()  # cursor.fetchone()[0]
    """

    return render(request, "rehabilitator_medicalrecord.html", locals())


def patient_rehubrecord(request):
    template = "models/rehabilitatorbase.html"
    if "raccount" not in request.session:
        return redirect('../patient_Login')
    rid = Rehabilitator.objects.get(id=request.session["raccount"])
    cursor = connection.cursor()
    cursor.execute("select name , id from AppProject_patient "
                   "WHERE id=(SELECT pID_id FROM AppProject_medicalrecord WHERE rID_id='" + request.session[
                       "raccount"] + "')")

    patients = cursor.fetchall()  # cursor.fetchone()[0]

    if request.method != "POST":
        mess = "表單資料尚未送出.."
    else:
        sel_patient = request.POST['sel_patient']
        records = RehubRecord.objects.filter(pID_id=sel_patient)

        cursor.execute("select distinct * from AppProject_patient "
                       "WHERE id= '" + sel_patient + "'")
        sel_patient_name = cursor.fetchall()  # cursor.fetchone()[0]
    """
    cursor = connection.cursor()
    cursor.execute("select name , id from AppProject_patient "
                   "WHERE id=(SELECT pID_id FROM AppProject_medicalrecord WHERE rID_id='"+request.session["raccount"]+"')")

    patients = cursor.fetchall()  # cursor.fetchone()[0]
    """

    return render(request, "patient_rehubrecord.html", locals())