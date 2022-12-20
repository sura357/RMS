from django.shortcuts import render  # 這個可以引入從templates中取得html
from AppProject.models import *
from django.shortcuts import redirect
from django.http import HttpResponse
from datetime import datetime
from django.db import connection


def logout(request):
    if "raccount" in request.session:
        request.session.clear()  # 刪除所有session
        request.session.flush()
        # del request.session["account"]  # 刪除單一Session
    return redirect('../login')
###################################
############### 前端 ###############
###################################

def getName(request):
    if "paccount" in request.session:
        cursor = connection.cursor()

        patientquery = f"""
                SELECT p.name
                FROM AppProject_patient p
                WHERE p.id = '{request.session["paccount"]}'
                """
        cursor.execute(patientquery)
        patient = cursor.fetchall()[0]  # cursor.fetchone()[0]
        return patient[0]
    return "None Name"

def patient_Logout(request):# 登出
    request.session.clear()
    return redirect('../patient_Login')

def patient_Login(request):# 登入
    rusers = Rehabilitator.objects.all().order_by('id')
    pusers = Patient.objects.all().order_by('id')

    #request.session['paccount'] = "A144650796"#A109913910 - A144650796

    # loginform = form.LoginForm(request.POST)  # 如為空白是建立一個空白的物件
    if "raccount" in request.session:
        return redirect('../rehabilitator_Information')

    if "paccount" in request.session:
        return redirect('../patient_home')

    if request.method != "POST":
        mess = "表單資料尚未送出.."
    else:
        account = request.POST['Account']
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

def patient_home(request):# 首頁

    if "paccount" in request.session:
        name = getName(request)
        cursor = connection.cursor()

        # 查詢可做動作
        getCanDoMotionQuery = f"""
        SELECT SetID, name
        FROM AppProject_medicalrecord
            LEFT JOIN AppProject_plan ON AppProject_medicalrecord.planID =  AppProject_plan.planID
            LEFT JOIN AppProject_planset ON AppProject_plan.SetID_id =  AppProject_planset.id
            LEFT JOIN AppProject_plansetmotion ON AppProject_planset.smID_id = AppProject_plansetmotion.id
            LEFT JOIN AppProject_motion ON AppProject_plansetmotion.mID_id = AppProject_motion.id
        WHERE AppProject_planset.SetID BETWEEN DATE('now','localtime','-7 days') AND DATE('now','localtime','+7 days')
		    AND pID_id = '{request.session["paccount"]}'
		ORDER BY datetime(AppProject_planset.SetID) ASC;
        """
        cursor.execute(getCanDoMotionQuery)
        motionList = cursor.fetchall()  # cursor.fetchone()[0]

        MotionList = []
        for motion in motionList:
            MotionList.append(list(motion))
        for i in range(len(MotionList)):
            MotionList[i][0] = str(int(MotionList[i][0].year)-1911) + "年" + str(MotionList[i][0].month) + "月" + str(MotionList[i][0].day) + "日"

        print(MotionList)
        print(5555)


        # 查詢通知
        getcontactrecord = f"""
        SELECT ct.content
        FROM AppProject_contactrecord ct
        WHERE pID_id = '{request.session["paccount"]}'
        ORDER BY ct.id DESC;
        """
        cursor.execute(getcontactrecord)
        contactrecordList = cursor.fetchall()


        # 查詢小知識
        getrehuburl = f"""
        SELECT id,content,url
        FROM AppProject_rehuburl;
        """
        cursor.execute(getrehuburl)
        rehuburlList = cursor.fetchall()

        # print(rehuburlList)

    else:
        return redirect('../patient_Login')


    template = "models/patientbase.html"
    return render(request, "patient_home.html", locals())

def patient_Information(request):# 個人資訊
    if "paccount" in request.session:
        name = getName(request)
        cursor = connection.cursor()

        patientquery = f"""
        SELECT p.name, p.phonenumber, p.email, p.birthday
        FROM AppProject_patient p
        WHERE p.id = '{request.session["paccount"]}'
        """
        cursor.execute(patientquery)
        patient = list(cursor.fetchall()[0])  # cursor.fetchone()[0]
        print(patient)
        patient[3] = str(int(patient[3].year) - 1911) + "年" + str(patient[3].month) + "月" + str(patient[3].day) + "日"


        kinectquery = f"""
        SELECT ks.id, rr.startingdate,rr.duration, ks.status
        FROM AppProject_rentalrecords rr
            LEFT JOIN AppProject_patient p ON rr.pID_id = p.id
            LEFT JOIN AppProject_kinectstatus ks ON rr.kID_id = ks.id
        WHERE rr.pID_id = '{request.session["paccount"]}' AND ks.status = 0
        """
        print(kinectquery)
        cursor.execute(kinectquery)
        k = cursor.fetchall()
        print(len(k))
        if len(cursor.fetchall()) > 0:
            kinect = cursor.fetchall()[0]
            time = datetime.strftime(kinect[1], '%Y 年 %m 月 %d 日')
        else:
            kinect = []



    template = "models/patientbase.html"
    return render(request, "patient_Information.html", locals())

def patient_medicalrecord(request):# 看診紀錄
    if "paccount" in request.session:
        name = getName(request)
        cursor = connection.cursor()

        medicalrecordquery = f"""
        SELECT AppProject_medicalrecord.creating_date, AppProject_medicalrecord.disease,AppProject_medicalrecord.symptom,AppProject_medicalrecord.status
        FROM AppProject_medicalrecord
        WHERE pID_id = '{request.session["paccount"]}';
                """
        cursor.execute(medicalrecordquery)
        medicalrecordList = cursor.fetchall()  # cursor.fetchone()[0]
        MedicalrecordList = []
        for rehubrecord in medicalrecordList:
            MedicalrecordList.append(list(rehubrecord))
        for i in range(len(MedicalrecordList)):
            MedicalrecordList[i][0] = str(int(MedicalrecordList[i][0].year) - 1911) + "年" + str(MedicalrecordList[i][0].month) + "月" + str(
                MedicalrecordList[i][0].day) + "日"

    template = "models/patientbase.html"
    return render(request, "patient_medicalrecord.html", locals())

def patient_rehubrecord(request):# 復健紀錄
    if "paccount" in request.session:
        name = getName(request)
        cursor = connection.cursor()
        SearchPlanDir = []

        medicalquery = f"""
        SELECT mc.planID,mc.disease,mc.symptom,r.name,mc.creating_date
        FROM AppProject_medicalrecord mc
            LEFT JOIN AppProject_rehabilitator r ON mc.rID_id = r.id
        WHERE mc.pID_id = '{request.session["paccount"]}'"""
        cursor.execute(medicalquery)
        MedicalList = ListDateTrainsform(cursor.fetchall(), 4)

        # 根據看診清單，撈出附屬的所有應做動作
        for Medical in MedicalList:
            MedicalDir = {}
            MedicalDir["Medical"] = Medical

            planSetquery = f"""
                SELECT ps.SetID,m.name,rc.accuracy
                FROM AppProject_plan p
                    LEFT JOIN AppProject_planset ps ON p.setID_id = ps.id
                    LEFT JOIN AppProject_plansetmotion psm ON ps.smID_id = psm.id
                    LEFT JOIN AppProject_motion m ON psm.mID_id = m.id
                    LEFT JOIN AppProject_rehubrecord rc ON ps.id = rc.sid_id
                WHERE p.planID = '{Medical[0]}';"""
            cursor.execute(planSetquery)
            MedicalDir["Set"] = ListDateTrainsform(cursor.fetchall(), 0)

            for i in range(len(MedicalDir["Set"])):
                if MedicalDir["Set"][i][2] is None:
                    MedicalDir["Set"][i].append("未完成")
                else:
                    MedicalDir["Set"][i].append("")

            SearchPlanDir.append(MedicalDir)


    template = "models/patientbase.html"
    return render(request, "patient_rehubrecord.html", locals())

def test(request):
    return render(request, "models/patientbase.html", locals())

def ListDateTrainsform(inputlist,column):
    returnlist = []
    for row in inputlist:
        returnlist.append(list(row))
    for i in range(len(returnlist)):
        returnlist[i][column] = str(int(returnlist[i][column].year) - 1911) + "年" + str(
            returnlist[i][column].month) + "月" + str(
            returnlist[i][column].day) + "日"
    return returnlist

###################################
############### 後端 ###############
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
        disease = request.GET.get('disease')
        symptom = request.GET.get('symptom')
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
            print(disease)
            print(symptom)
            print(planid)

            if planid is None:
                return render(request, "rehabilitator_addPlan.html", locals())

            #print(set_details[1])
            #print(set_details[1][1])
            # print(aa)
            cursor.execute("SELECT max(planID) "
                           "from AppProject_plan")
            top_planid = cursor.fetchall()  # cursor.fetchone()[0]
            print(top_planid[0][0])
            print(top_planid)

            if top_planid[0][0] is None:
                top_planidnum = 1
            else:
                top_planidnum = int(top_planid[0][0])+1
            print(top_planidnum)
            print(planid)
            print(planid != -1)
            if planid != '-1':
                top_planidnum = planid

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
                                   "VALUES(NULL, " + str(top_planidnum) + ", "
                                   "date('now','localtime'), "
                                   "(SELECT last_insert_rowid()), '" + plan_name + "')")

            print("planid"+planid)
            if planid == "-1":
                print("why i'm here" + planid)
                cursor.execute("INSERT INTO AppProject_medicalrecord"
                               "(id, creating_date, disease, symptom, status, pID_id, planID, rid_id, remark)"
                               "VALUES(NULL, date('now','localtime'), '"+disease+"', '"+symptom+"', 0, '" + sel_patient + "', " + str(top_planidnum) + ", '" + rid.id + "', 'aa');")

            #return redirect('../rehabilitator_CheckPlan/?sel_patient=' + sel_patient)
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

            cursor.execute("select distinct planID "
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


def rehabilitator_deletePlan(request):
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
        sd_id = request.GET.get('sd_id')
        # aa = request.GET.get('aa')
        """data = json.loads(request.GET.get('aa'))

        print(data)"""

        if sel_patient is not None and sel_patient != "" and sel_patient != "None":
            # print(sel_patient)
            cursor.execute("select distinct * from AppProject_patient "
                           "WHERE id= '"+sel_patient+"'")
            sel_patient_name = cursor.fetchall()  # cursor.fetchone()[0]

            print(sel_patient_name)
            print(sd_id)
            cursor.execute("DELETE FROM AppProject_plan "
                           "WHERE setID_id = (SELECT id FROM AppProject_planset WHERE smID_id = "
                           "(SELECT id FROM AppProject_plansetmotion WHERE sdID_id = " + str(sd_id) + "))")

            cursor.execute("DELETE FROM AppProject_planset "
                           "WHERE smID_id = (SELECT id FROM AppProject_plansetmotion WHERE sdID_id = " + str(sd_id) + ") ")

            cursor.execute("DELETE FROM AppProject_plansetmotion WHERE sdID_id = " + str(sd_id) + "")

            cursor.execute("DELETE FROM AppProject_plansetdetail WHERE id = "+str(sd_id)+"")

            cursor.execute("SELECT count(planID) from AppProject_plan where planID="+sel_plan+"")
            plan_count = cursor.fetchall()  # cursor.fetchone()[0]

            if plan_count == 0:
                cursor.execute("DELETE from AppProject_medicalrecord WHERE planID_id = "+sel_plan+"")


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

    kinects = KinectStatus.objects.filter(status=0)
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
        # print("sel_kinect:"+sel_kinect)
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
            LEFT JOIN AppProject_medicalrecord mr ON  p.planID = mr.planID
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
