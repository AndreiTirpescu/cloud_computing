import json

from db_module.aliment_db_connection import AlimentDbConnection
from aliment_api.model.aliment import Aliment
from aliment_api.response.api_response import AlimentApiResponse


class AlimentApiController:
    def __init__(self):
        pass

    def get_aliment(self, args):
        db_connection = AlimentDbConnection.get().connection()
        db_cursor     = db_connection.cursor()

        db_cursor.execute("SELECT * FROM aliment")
        rows = db_cursor.fetchall()

        for row in rows:
            if (row[3] == args[0]):
                return AlimentApiResponse(
                    200, 
                    Aliment(row[0], row[1], row[2], row[3]).get_dict()
                )
        
        return AlimentApiResponse(
            404, 
            {"status": "Error, aliment not found"}
        )

    def get_aliments(self, args):
        db_connection = AlimentDbConnection.get().connection()
        db_cursor     = db_connection.cursor()

        db_cursor.execute("SELECT * FROM aliment")
        rows = db_cursor.fetchall()
        
        resultList = []
        for row in rows:
            resultList.append(Aliment(row[0], row[1], row[2], row[3]).get_dict())
        
        if len(resultList) > 0:
            return AlimentApiResponse(
                200, 
                {
                    "aliments" : resultList
                }
            )

        return AlimentApiResponse(
            404, 
            {"status": "Error, there are no aliments left"}
        )

    def post_aliment(self, body):
        db_connection = AlimentDbConnection.get().connection()
        db_cursor     = db_connection.cursor()

        db_cursor.execute("SELECT * FROM aliment WHERE code = '" +  body[0]["code"] + "'")
        row = db_cursor.fetchall()
        
        print(row)

        if len(row) != 0:
            return AlimentApiResponse(
                409 , 
                {"status": "Resource already exists"}
            )

        new_aliment = Aliment(0, body[0]["name"], body[0]["price"], body[0]["code"])

        db_cursor.execute("INSERT INTO aliment (name, price, code) VALUES ( '" + new_aliment.getName() + "', '" +  str(new_aliment.getPrice()) + "', '" + new_aliment.getCode() + "')" )
        db_connection.commit()
        
        db_cursor.execute("SELECT * FROM aliment WHERE code = '" + body[0]["code"] + "'")
        row = db_cursor.fetchone()

        if row == None:
            return AlimentApiResponse(
                500 , 
                {"status": "Error, Internal server error"}
            )
        
        return AlimentApiResponse(
            200, 
            {"status": "Success", "resource":  Aliment(row[0], row[1], row[2], row[3]).get_dict()}
        )

    def post_aliments(self, body):
        db_connection = AlimentDbConnection.get().connection()
        db_cursor     = db_connection.cursor()

        for new_prod in body[0]:
            db_cursor.execute("SELECT * FROM aliment WHERE code = '" +  new_prod["code"] + "'")
            row = db_cursor.fetchall()

            if len(row) != 0:
                continue
            
            new_aliment = Aliment(0, new_prod["name"], new_prod["price"], new_prod["code"])

            db_cursor.execute("INSERT INTO aliment (name, price, code) VALUES ( '" + new_aliment.getName() + "', '" +  str(new_aliment.getPrice()) + "', '" + new_aliment.getCode() + "')" )
            db_connection.commit()

            db_cursor.execute("SELECT * FROM aliment WHERE code = '" + new_prod["code"] + "'")
            row = db_cursor.fetchone()

            if row == None:
                return AlimentApiResponse(
                    500 , 
                    {"status": "Error, Could not insert into db"}
                )
        
        return AlimentApiResponse(
            200, 
            {"status": "Success"}
        )

    def put_aliment(self, body):
        db_connection = AlimentDbConnection.get().connection()
        db_cursor     = db_connection.cursor()

        db_cursor.execute("DELETE FROM aliment WHERE code = '" +  body[0]["code"] + "'")
        db_connection.commit()

        new_aliment = Aliment(0, body[0]["name"], body[0]["price"], body[0]["code"])

        db_cursor.execute("INSERT INTO aliment (name, price, code) VALUES ( '" + new_aliment.getName() + "', '" +  str(new_aliment.getPrice()) + "', '" + new_aliment.getCode() + "')" )
        db_connection.commit()
        
        db_cursor.execute("SELECT * FROM aliment WHERE code = '" + body[0]["code"] + "'")
        row = db_cursor.fetchone()

        if row == None:
            return AlimentApiResponse(
                500 , 
                {"status": "Error, Internal server error"}
            )
        
        return AlimentApiResponse(
            200, 
            {"status": "Success", "resource":  Aliment(row[0], row[1], row[2], row[3]).get_dict()}
        )

    def put_aliments(self, body):
        db_connection = AlimentDbConnection.get().connection()
        db_cursor     = db_connection.cursor()

        db_cursor.execute("DELETE FROM aliment")
        db_connection.commit()

        for new_prod in body[0]:
            new_aliment = Aliment(0, new_prod["name"], new_prod["price"], new_prod["code"])

            db_cursor.execute("INSERT INTO aliment (name, price, code) VALUES ( '" + new_aliment.getName() + "', '" +  str(new_aliment.getPrice()) + "', '" + new_aliment.getCode() + "')" )
            db_connection.commit()

            db_cursor.execute("SELECT * FROM aliment WHERE code = '" + new_prod["code"] + "'")
            row = db_cursor.fetchone()

            if row == None:
                return AlimentApiResponse(
                    500 , 
                    {"status": "Error, Could not insert into db"}
                )
        
        return AlimentApiResponse(
            200, 
            {"status": "Success"}
        )

    def delete_aliment(self, args):
        db_connection = AlimentDbConnection.get().connection()
        db_cursor     = db_connection.cursor()

        db_cursor.execute("DELETE FROM aliment WHERE code = '" +  args[0] + "'")
        db_connection.commit()

        return AlimentApiResponse(
            200, 
            {"status": "Success"}
        )

    def delete_aliments(self, args):
        db_connection = AlimentDbConnection.get().connection()
        db_cursor     = db_connection.cursor()

        db_cursor.execute("DELETE FROM aliment")
        db_connection.commit()

        return AlimentApiResponse(
            200, 
            {"status": "Success"}
        )