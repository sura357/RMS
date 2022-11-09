import sqlite3
import json

#目標，將CI傳來的指令，執行SQL指令，並回傳json格式的字串
class SQLiteDatabase():
    def __init__(self,dataBase = "../db.sqlite3"):
        self.dataBase = dataBase
        
        

    def dataToJson(self, cursor, result):
        jasonString = ""
        resultList = {} 
        resultList["responseList"] = []
        resultList["execute"] = True
        try:
            columns = [column[0] for column in cursor.description]
            for row in result.fetchall():
                resultList["responseList"].append(dict(zip(columns, row)))
            

            # if len(resultList["responseList"])>0:
            #     resultList["execute"] = True
            # else:
            #     resultList["execute"] = False

        except Exception as e:
            resultList["execute"] = False
            print("Error: " + str(e))
        finally:

            jasonString = json.dumps(resultList,ensure_ascii=False)
            
            return jasonString



    def jasonToData(self,jsonStr):
        print(jsonStr)
        str_ = json.loads(jsonStr)
        return str_

    def Select(self, query):
        self.conn = sqlite3.connect(self.dataBase)
        cursor = self.conn.cursor()
        print(query)
        result = cursor.execute(query)

        jasonString = self.dataToJson(cursor,result)
        self.conn.close()
        if jasonString is not None:
            return jasonString

    def check(self, query):
        self.conn = sqlite3.connect(self.dataBase)
        cursor = self.conn.cursor()
        print(query)
        result = cursor.execute(query)


        resultList = {} 
        resultList["responseList"] = []
        resultList["execute"] = False 

        for re in result.fetchall():
            print(re)
            resultList["responseList"].append(True)
            resultList["execute"] =  True

        jasonString = json.dumps(resultList,ensure_ascii=False)
        self.conn.close()
        if jasonString is not None:
            return jasonString
        pass

    def bigSelect(self, Bquery, Lquery):
        resultList = {} 
        resultList["responseList"] = []
        resultList["execute"] = None 
        print(Bquery)
        print("--------------------------------")
        print(Lquery)
        self.conn = sqlite3.connect(self.dataBase)
        cursor = self.conn.cursor()
        
        Bresult = cursor.execute(Bquery)
        b = Bresult.fetchone()
        print(b)
        if b is not None:
            resultList["disease"] = b[0]
            resultList["symptom"] = b[1]
            resultList["status"] = b[2]
            resultList["planID_id"] = b[3]
            resultList["rID_id"] = b[4]
        else:
            resultList["disease"] = ""
            resultList["symptom"] = ""
            resultList["status"] = ""
            resultList["planID_id"] = ""
            resultList["rID_id"] = ""

        Lresult = cursor.execute(Lquery)
        columns = [column[0] for column in cursor.description]
        for row in Lresult.fetchall():
            resultList["responseList"].append(dict(zip(columns, row)))

        

        if len(resultList["responseList"])>0 and b is not None:
            resultList["execute"] = True
        else:
            resultList["execute"] = False
        
        jasonString = json.dumps(resultList,ensure_ascii=False)
        self.conn.close()
        print("jasonString:" + jasonString)
        if jasonString is not None:
            return jasonString

    def Change(self,query):
        resultList = {} 
        resultList["execute"] = None 
        
        self.conn = sqlite3.connect(self.dataBase)
        cursor = self.conn.cursor()
        print(query)

        # try:
        cursor.execute(query)
        self.conn.commit()
        resultList["execute"] = True 
        # except Exception as e:
        #     self.conn.rollback()
        #     resultList["execute"] = False 
        # finally:
        self.conn.close()
        jasonString = json.dumps(resultList,ensure_ascii=False)
        return jasonString



        

        


    def Delete(self,query):

        pass







if __name__ == '__main__':
    sql = SQLiteDatabase()
    sql.Select("SELECT * FROM `病患`")

