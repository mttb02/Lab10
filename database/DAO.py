from database.DB_connect import DBConnect
from model.confine import Confine

class DAO():

    @staticmethod
    def get_all_countries():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * from country"""

        cursor.execute(query, ())

        for row in cursor:
            result.append(row["StateNme"])

        cursor.close()
        conn.close()
        return result



    @staticmethod
    def get_confini(anno_max):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT c1.StateNme as c1, c2.StateNme as c2, conttype FROM contiguity, country as c1, country as c2
                WHERE state1no<state2no and state1no = c1.CCode and state2no = c2.CCode and year <= %s"""

        cursor.execute(query, (anno_max,))

        for row in cursor:
            result.append(Confine(row["c1"], row["c2"], row["conttype"]))

        cursor.close()
        conn.close()
        return result