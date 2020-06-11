# lesson 1 simple implementation with mongodb
# import pymongo
# uri = "mongodb://127.0.0.1:27017"
# client = pymongo.MongoClient(uri)
# database = client['fullstack']
# collection = database['students']
# students = collection.find({})
# for student in students:
#     print(student)
# students = [student for student in collection.find({})]
# lesson 2
# students = [student['mark'] for student in collection.find({}) if student['mark' == 99.0]]
# print(students)
from database import Database
from menu import Menu

__author__ = 'jslvtr'

Database.initialize()

menu = Menu()

menu.run_menu()