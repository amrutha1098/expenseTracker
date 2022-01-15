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
            data = request.get_json()
            data["dateTime"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(data)
            self.insert_table_data_expense_tracker(data)
            return data

    def update_expense(self):
        @self.app.route('/addexpense', methods=['PUT'])
        def update_expense():
            data = request.get_json()
            data["dateTime"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(data)
            self.update_table_data_expense_tracker(data)
            return data

# Run Server
if __name__ == '__main__':
    Obj = ExpenseTrackerAPI()
    Obj.add_expense()
    Obj.update_expense()

    Obj.app.run(debug=True)