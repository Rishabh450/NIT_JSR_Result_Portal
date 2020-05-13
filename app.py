import requests
from pages.profile import ProfilePage
from bs4 import BeautifulSoup
from parsers.ProfileParcer import ProfileParser
from parsers.ResultTableParser import ResultsTableParser
from parsers.SubjectParser import SubjectParser
from flask import Flask, request, jsonify
import json

import os

app = Flask("__name__")


@app.route('/', methods=['POST'])
def get_user():
    return jsonify({'Developed by': "Rishabh Bhardwaj", 'status': 500})


def getContent(roll_number):
    dicter = {
        'roll': roll_number
    }
    s = requests.Session()
    r = s.post('https://nilekrator.pythonanywhere.com/', dicter)
    if r.status_code == 200:
        text = r.text
        dictr = text
        profile = s.get(url='https://nilekrator.pythonanywhere.com/profile', params=dictr).content
        return profile

    else:
        return "invalid"


@app.route('/api/profile', methods=['POST'])
def getBasicProfile():
    roll_number = request.json['roll']
    page = ProfilePage(getContent(roll_number))
    parsed = [ProfileParser(details).getDetails for details in page.getProfile]
    profile_list = [BeautifulSoup(str(item)).text for item in parsed[0]]
    profile_json = {
        "name": profile_list[0],
        "roll": profile_list[1],
        "branch": profile_list[2],
        "rank": profile_list[3]
    }
    return jsonify(profile_json)


@app.route('/api/cgpa', methods=['POST'])
def getCGPA():
    roll_number = request.json['roll']
    page = ProfilePage(getContent(roll_number))
    totalsems = []
    for table in page.getAllResultTables:
        res = ResultsTableParser(table)
        status_list = res.getSemesterStatus

        if status_list:
            status_json = {
                "semester": status_list[2],
                "status": status_list[3],
                "sgpa": status_list[0],
                "cgpa": status_list[1]
            }
            totalsems.append(status_json)
    return jsonify(totalsems)


@app.route('/api/results', methods=['POST'])
def getSemesterResults():
    roll_number = request.json['roll']

    page = ProfilePage(getContent(roll_number))
    semester_list = []
    for table in page.getAllResultTables:
        res = ResultsTableParser(table)
        totalsubjects = res.getAllSubjects
        sem_marks = []
        for subject in totalsubjects:
            subject_details_obj = SubjectParser(subject)
            subject_details = [subject_detail.string for subject_detail in subject_details_obj.getSubjectDetails]
            subject_details_json = {
                "code": subject_details[0],
                "name": subject_details[1],
                "mid_sem": subject_details[2],
                "internals": subject_details[3],
                "assignement": subject_details[4],
                "quiz": subject_details[5],
                "end_sem": subject_details[6],
                "total": subject_details[7],
                "grade": subject_details[8]
            }
            sem_marks.append(subject_details_json)
        if sem_marks:
            semester_list.append(sem_marks)
    return jsonify(semester_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', '5000'), debug=True)
