import mysql.connector


class MyDatabase:
    connection = None
    cursor = None

    def __init__(self):
        if MyDatabase.connection is None:
            try:
                MyDatabase.connection = mysql.connector.connect(
                    host="localhost",
                    user="",
                    passwd="",
                    database="testexpense"
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

    def update_table_data_expense_tracker(self, data):
        # cursor.execute(
        #     'Insert into EXPENSE_TRACKER (UserId, addExpense, category, dateTime, description, payee) values (' +
        #     str(data["userId"]) + ',' + str(data["addExpense"]) + ',' + str(data["category"]) + ',' + str(data["dateTime"]) + ',' + str(data[
        #         "description"]) + ',' + data["payee"] + ';')
        query = 'Insert into EXPENSE_TRACKER (UserId, addExpense, category, dateTime, description, payee) values (' + str(
            data["userId"]) + ',' + str(data["addExpense"]) + ',"' + str(data["category"]) + '","' + str(
            data["dateTime"]) + '","' + str(data[
                                                "description"]) + '","' + data["payee"] + '");'
        print(query)
        self.cursor.execute(query)

        self.connection.commit()
