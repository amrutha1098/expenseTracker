import mysql.connector
from constants import *


class MyDatabase:
    connection = None
    cursor = None

    def __init__(self):
        if MyDatabase.connection is None:
            try:
                MyDatabase.connection = mysql.connector.connect(
                    host=DB_HOST,
                    user=DB_USER,
                    passwd=DB_PASSWORD,
                    database=DB_DATABASE
                )
                MyDatabase.cursor = MyDatabase.connection.cursor()
            except Exception as error:
                print("Error: Connection not established {}".format(error))
            else:
                print("Connection established")

        self.connection = MyDatabase.connection
        self.cursor = MyDatabase.cursor

    def get_db_details(self, table_name='EXPENSE_TRACKER'):

        self.cursor.execute('SELECT * FROM ' + str(table_name))
        data = self.cursor.fetchall()
        return data

    def insert_table_data_expense_tracker(self, data):
        try:
            query = 'Insert into EXPENSE_TRACKER (UserId, addExpense, category, dateTime, description, payee) values (' + str(
                data["userId"]) + ',' + str(data["addExpense"]) + ',"' + str(data["category"]) + '","' + str(
                data["dateTime"]) + '","' + str(data[
                                                    "description"]) + '","' + data["payee"] + '");'
            print(query)
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as error:
            print("Error inserting into database {}".format(error))
        else:
            print("Inserted data succcessfully into DB ")

    def update_table_data_expense_tracker(self, data):
        try:
            query = 'UPDATE EXPENSE_TRACKER set addExpense = ' + str(data["addExpense"]) + ', category = "' + str(
                data["category"]) + '", dateTime = "' + str(
                data["dateTime"]) + '", description = "' + str(data["description"]) + '" , payee = "' + data[
                        "payee"] + '" WHERE userId = ' + str(data['userId']) + ';'
            print(query)
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as error:
            print("Error updating into database {}".format(error))
        else:
            print("Updated data succcessfully into DB ")
