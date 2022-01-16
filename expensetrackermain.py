from flask import Flask, request, jsonify
from database import *
from datetime import datetime
from json_helper import *


class ExpenseTrackerAPI(MyDatabase,JsonHelper):

    def __init__(self):
        self.app = Flask(__name__)
        MyDatabase.__init__(self)
        JsonHelper.__init__(self)

    def add_expense(self):
        @self.app.route('/addexpense', methods=['POST'])
        def add_expense():
            try :
                data = request.get_json()
                data["dateTime"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(data)
                self.insert_table_data_expense_tracker(data)
                return data
            except Exception as error:
                print("Failed to do a post request {}".format(error))
            else:
                print("successful post request ")

    def update_expense(self):
        @self.app.route('/addexpense/{id}/{time}', methods=['PUT'])
        def update_expense(id, time):
            try:
                data = request.get_json()
                data["dateTime"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                data["usrId"] =  id
                print(data)
                self.update_table_data_expense_tracker(data, time)
                return self.app.jsonify(data)
            except Exception as error:
                print("Failed to do a put request {}".format(error))
            else:
                print("successful put request ")

    def get_expense_details(self):
        @self.app.route('/addexpense', methods=['GET'])
        def get_expense_details():
            try:
                data = self.get_table_data_expense_tracker()
                return data
            except Exception as error:
                print("Failed to do a put request {}".format(error))
            else:
                print("successful get request ")

    def get_expense_details_by_usrid(self):
        @self.app.route('/addexpense/<id>', methods=['GET'])
        def get_expense_details_by_usrid(id):
            try:
                data = self.get_userid_data_expense_tracker(id)
                return data
            except Exception as error:
                print("Failed to do a put request {}".format(error))
            else:
                print("successful get request ")

    def add_new_category(self):
        @self.app.route('/category', methods=['POST'])
        def add_new_category():
            try:
                data = request.get_json()
                print(data)
                self.insert_table_data_category(data)
                return data
            except Exception as error:
                print("Failed to do a post request {}".format(error))
            else:
                print("successful post request ")

# Run Server
if __name__ == '__main__':
    Obj = ExpenseTrackerAPI()
    Obj.add_expense()
    Obj.update_expense()
    Obj.get_expense_details()
    Obj.get_expense_details_by_usrid()

    Obj.app.run(debug=True)
