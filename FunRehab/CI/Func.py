from CI.pySQL import SQLiteDatabase
from pathlib import Path
import threading
import json
import time
import os

class FUNC():
    def __init__(self):
        self.fileDir = "Resource"
        self.BUFFER_SIZE = 10240 * 10240

        # RSS = 0
        RSSconnect = {0:None,1:self.RSS_connect,2:None}
        RSSselect = {1:self.RSS_login,2:self.RSS_getMotion,3:self.RSS_getGame}
        RSSInsert = {1:self.RSS_addAct}
        RSSDelete = {1:self.RSS_delAct}
        RSSFile = {1:self.RSS_sendFile,2:self.RSS_readFile,3:self.RSS_roadFile}
        RSS = {0:RSSconnect,1:RSSselect,2:RSSInsert,3:RSSDelete,4:RSSFile}
        # URS = 2
        URSconnect = {0:None,1:self.URS_connect,2:None}
        URSselect = {1:self.URS_login,2:self.URS_todaysAct,3:self.URS_checkDone}
        URSInsert = {1:self.URS_addRecord}
        URSFile = {1:self.RSS_sendFile,2:self.RSS_readFile,3:self.RSS_roadFile}
        URS = {0:URSconnect,1:URSselect,2:URSInsert,3:None,4:URSFile}

        self.Switch = {0:RSS,1:None,2:URS}
        self.sqlite =  SQLiteDatabase()

    def RMS_Response(self,obj):
        # 組織返回封包
        obj[1].ID = "1"
        restring = obj[1].Assemble()

        obj[0].send(restring.encode())
        print("RE:" + restring)

#region RSS FUNC
    def RSS_connect(self,obj):
        print("RSS:Connect")


    def RSS_login(self,obj):
        # 復健師登入
        # input: id, password
        data = self.sqlite.jasonToData(obj[1].MSG)
        returnJson = ""
        query = f"""
        SELECT *
        FROM AppProject_rehabilitator
        WHERE id = '{data["id"]}' AND password = '{data["password"]}';
        """
        
        try:
            returnJson = self.sqlite.Select(query)
        except Exception as e:
            print("Error:" + str(e))
        finally:
            obj[1].MSG = returnJson
            self.RMS_Response(obj)
        

    def RSS_getMotion(self,obj):
        # 復健師查詢動作
        # input: 
        #data = self.sqlite.jasonToData(obj[1].MSG)
        
        returnJson = ""
        query = f"""
        SELECT * 
        FROM AppProject_motion;
        """
        
        try:
            returnJson = self.sqlite.Select(query)
        except Exception as e:
            print("Error:" + str(e))
        finally:
            obj[1].MSG = returnJson
            self.RMS_Response(obj)

        pass

    def RSS_getGame(self,obj):
        # 查詢遊戲清單
        # input: type, bodytpart
        data = self.sqlite.jasonToData(obj[1].MSG)
        returnJson = ""
        query = f"""
        SELECT *
        FROM AppProject_gamesample;
        """#WHERE type = '{data["type"]}'
        #AND bodytpart = '{data["bodypart"]}'
        
        try:
            returnJson = self.sqlite.Select(query)
        except Exception as e:
            print("Error:" + str(e))
        finally:
            obj[1].MSG = returnJson
            self.RMS_Response(obj)

    def RSS_addAct(self,obj):
        # 復健師新增動作
        # input: type, name, video_file, standard_file, game_id_id, bodypart
        data = self.sqlite.jasonToData(obj[1].MSG)
        returnJson = ""
        query = f"""
        INSERT INTO AppProject_motion (type, name, video_file, standard_file, game_id_id, bodypart, rid_id) 
        VALUES ('{data["type"]}', '{data["name"]}', '{data["video_file"]}', '{data["standard_file"]}', '{data["game_id_id"]}', '{data["bodypart"]}','{data["rid_id"]}');
        """
        
        try:
            returnJson = self.sqlite.Change(query)
        except Exception as e:
            print("Error:" + str(e))
        finally:
            obj[1].MSG = returnJson
            self.RMS_Response(obj)

    def RSS_delAct(self,obj):
        # 復健師刪除動作
        # input: id
        data = self.sqlite.jasonToData(obj[1].MSG)
        returnJson = ""
        query = f"""
        DELETE FROM AppProject_motion 
        WHERE id  = '{data["id"]}';
        """
        
        try:
            returnJson = self.sqlite.Change(query)
        except Exception as e:
            print("Error:" + str(e))
        finally:
            obj[1].MSG = returnJson
            self.RMS_Response(obj)

        pass

    def RSS_sendFile(self,obj):
        # RSS是送的一端，所以這裡要接收
        # input: standard_file, fileSize
        data = self.sqlite.jasonToData(obj[1].MSG)
        

        with open(r'%s\%s' % (self.fileDir, data["standard_file"]), 'wb') as f:
            recv_size = 0
            print('打開檔案成功')
            while True:
                line = obj[0].recv(self.BUFFER_SIZE)
                f.write(line)
                recv_size += len(line)

                if (str(recv_size) == data["fileSize"]):
                    break
            print("結束讀寫")
        
        header = {"execute" : True}
        obj[1].MSG = json.dumps(header,ensure_ascii=False)
        self.RMS_Response(obj)

        

    def RSS_readFile(self, obj):
        # input: standard_file
        data = self.sqlite.jasonToData(obj[1].MSG)
        print("URS_readFile")

        print("step 1")

        path = r'%s\%s' % (self.fileDir, data["standard_file"])
        if os.path.isfile(path):
            print("Find file")
            header = \
            {
                "execute" : True,
                "responseList" : 
                [{
                    "standard_file":data["standard_file"],
                    "fileSize":str(Path(path).stat().st_size)
                }]
            }
        else:
            print("No such file")
            header = \
            {
                "execute" : False,
                "responseList" : 
                [{
                    "standard_file":"",
                    "fileSize":""
                }]
            }
        obj[1].MSG = json.dumps(header,ensure_ascii=False)
        
        self.RMS_Response(obj)
        print("step 2")
        

    def RSS_roadFile(self, obj):
        data = self.sqlite.jasonToData(obj[1].MSG)
        print("step 3")
        
        self.RMS_Response(obj)
        
        predict_send_times = int(data["fileSize"]) / self.BUFFER_SIZE

        print("step 4")
        with open(r'%s\%s' % (self.fileDir, data["standard_file"]), 'rb') as f:
            obj[0].send(f.read(self.BUFFER_SIZE))
                
            while predict_send_times > 0:      
                obj[0].send(f.read(self.BUFFER_SIZE))
                predict_send_times -= 1

        print("step 5")

        




#endregion

#region URS FUNC
    def URS_connect(self,obj):
        print("URS:Connect")

    def URS_login(self,obj):
        # 病患登入
        # input: id
        data = self.sqlite.jasonToData(obj[1].MSG)

        query = f"""
        SELECT *
        FROM AppProject_patient
        WHERE id = '{data["id"]}';
        """
        
        try:
            returnJson = self.sqlite.Select(query)
        except Exception as e:
            print("Error:" + str(e))
        finally:
            obj[1].MSG = returnJson
            self.RMS_Response(obj)

    def URS_todaysAct(self,obj):
        # 取得今天份的(可做)動作清單
        # input: id
        returnJson = ""
        data = self.sqlite.jasonToData(obj[1].MSG)

        queryRecord = f"""
        SELECT 	AppProject_medicalrecord.disease,
                AppProject_medicalrecord.symptom,
                AppProject_medicalrecord.status,
                AppProject_medicalrecord.planID_id,
                AppProject_medicalrecord.rID_id
        FROM AppProject_medicalrecord
            LEFT JOIN AppProject_plan ON AppProject_medicalrecord.planID_id =  AppProject_plan.planID
            LEFT JOIN AppProject_planset ON AppProject_plan.SetID_id =  AppProject_planset.id
        WHERE AppProject_planset.SetID BETWEEN DATE('now','localtime','-7 days') AND DATE('now','localtime')
            AND AppProject_medicalrecord.pID_id = '{data["id"]}';
        """
        #
        queryMotion = f"""
        SELECT
            AppProject_planset.SetID as date_,
            AppProject_planset.id as sid,
            AppProject_plansetmotion.id as smid,
            AppProject_plansetmotion.mID_id as mid,
            AppProject_plansetmotion.sdID_id,
            AppProject_motion.game_id_id,
            
            AppProject_motion.name,
            AppProject_motion.type,
            AppProject_motion.bodypart,
            AppProject_plansetdetail.duration,
            AppProject_plansetdetail.times,
            AppProject_plansetdetail.breadtime,
            AppProject_plansetdetail.ontop_duration,
            AppProject_plansetdetail.motion_time,
            
            AppProject_motion.video_file,
            AppProject_motion.standard_file,
            AppProject_gamesample.game_file
        FROM AppProject_medicalrecord
            LEFT JOIN AppProject_plan ON AppProject_medicalrecord.planID_id =  AppProject_plan.planID
            LEFT JOIN AppProject_planset ON AppProject_plan.SetID_id =  AppProject_planset.id
            LEFT JOIN AppProject_plansetmotion ON AppProject_planset.smID_id = AppProject_plansetmotion.id
            LEFT JOIN AppProject_plansetdetail ON AppProject_plansetmotion.sdID_id =  AppProject_plansetdetail.id
            LEFT JOIN AppProject_motion ON AppProject_plansetmotion.mID_id = AppProject_motion.id
            LEFT JOIN AppProject_rehubrecord ON AppProject_planset.id = AppProject_rehubrecord.sid_id
            LEFT JOIN AppProject_gamesample ON AppProject_gamesample.id = AppProject_motion.game_id_id
        WHERE date_ BETWEEN DATE('now','localtime','-7 days') AND DATE('now','localtime')
            AND AppProject_medicalrecord.pID_id = '{data["id"]}'
            AND AppProject_medicalrecord.status = 0 
            AND AppProject_rehubrecord.sid_id IS NULL
        ORDER BY datetime(date_) ASC, smid ASC;
        """

        # try:
        returnJson = self.sqlite.bigSelect(queryRecord,queryMotion)
        # except Exception as e:
        #     print("Error:" + str(e))
        # finally:
        obj[1].MSG = returnJson
        self.RMS_Response(obj)

    def URS_checkDone(self,obj):
        # 取得動作詳細資訊
        # input: mID_id, sdID_id
        data = self.sqlite.jasonToData(obj[1].MSG)
        returnJson = ""
        query = f"""
        SELECT  *
        FROM AppProject_medicalrecord
            LEFT JOIN AppProject_plan ON AppProject_medicalrecord.planID_id =  AppProject_plan.planID
            LEFT JOIN AppProject_planset ON AppProject_plan.SetID_id =  AppProject_planset.id
            LEFT JOIN AppProject_rehubrecord ON AppProject_planset.id =  AppProject_rehubrecord.sID_id
        WHERE AppProject_medicalrecord.pID_id = '{data["id"]}' 
            AND AppProject_medicalrecord.status = 0
            AND AppProject_rehubrecord.sID_id = {data["sID_id"]};
        """
        
        # try:
        returnJson = self.sqlite.check(query)
        # except Exception as e:
        #     print("Error:" + str(e))
        # finally:
        obj[1].MSG = returnJson
        self.RMS_Response(obj)

    def URS_addRecord(self,obj):
        # 新增復健紀錄
        # input: sdID_id, accuaracy, times, duration, progress
        data = self.sqlite.jasonToData(obj[1].MSG)
        returnJson = ""
        query = f"""
        INSERT INTO AppProject_rehubrecord (sID_id, accuracy, times, duration, progress) 
        VALUES ({data["sID_id"]}, {data["accuracy"]}, {data["times"]}, {data["duration"]}, {data["progress"]});
        """
        
        try:
            returnJson = self.sqlite.Change(query)
        except Exception as e:
            print("Error:" + str(e))
        finally:
            obj[1].MSG = returnJson
            self.RMS_Response(obj)


    def URS_readFile(self,obj):
        # URS是收的一端，所以這裡要傳送
        # input: standard_file
        data = self.sqlite.jasonToData(obj[1].MSG)
        print("URS_readFile")
        header = \
        {
            "execute" : True,
            "responseList" : 
            {
                "file":data["standard_file"],
                "fileSize":str(Path(self.fileDir + data["standard_file"]).stat().st_size)
            }
        }
        print(str(Path(self.fileDir + data["standard_file"]).stat().st_size))


        obj[1].MSG = json.dumps(header,ensure_ascii=False)
        self.RMS_Response(obj)

        with open(r'%s\%s' % (self.fileDir, data["standard_file"]), 'rb') as f:
                for line in f:
                    obj[0].send(line)

#endregion
