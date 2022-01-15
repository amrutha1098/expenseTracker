from flask import Flask, request
from database import *
from datetime import datetime


class ExpenseTrackerAPI(MyDatabase):

    def __init__(self):
        self.app = Flask(__name__)
        MyDatabase.__init__(self)

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
        @self.app.route('/addexpense', methods=['PUT'])
        def update_expense():
            try:
                data = request.get_json()
                data["dateTime"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(data)
                self.update_table_data_expense_tracker(data)
                return data
            except Exception as error:
                print("Failed to do a put request {}".format(error))
            else:
                print("successful put request ")



# Run Server
if __name__ == '__main__':
    Obj = ExpenseTrackerAPI()
    Obj.add_expense()
    Obj.update_expense()

    Obj.app.run(debug=True)
