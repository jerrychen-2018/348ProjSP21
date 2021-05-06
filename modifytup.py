import tkinter as tk
import mysql.connector
from tkinter import *
import main


def connect():
    cnx = mysql.connector.connect(user='root', password='rohanjerrytroy',
                                  host='35.224.65.220',
                                  database='schoolsystem')
    return cnx


def modify_home(root):
    global temp_root
    temp_root = root
    for widget in root.winfo_children():
        widget.destroy()

    table_options = [
        "Student",
        "Faculty",
        "Course",
        "Course Section",
        "Dormitory",
        "Department",
        "Classroom",
        "Club",
        "Building"
    ]

    clicked = tk.StringVar()
    clicked.set("Select Table")
    drop = OptionMenu(root, clicked, *table_options).grid(row=2, column=5)
    myButton = tk.Button(root, text="Confirm Selection", command=lambda: change_page(clicked.get())).grid(row=2, column=6)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("main")).grid(row=2, column=7)


def student_page(root):
    for widget in temp_root.winfo_children():
        widget.destroy()
    id_var = tk.StringVar()

    id_label = tk.Label(root, text='Please enter the current ID of the student to be updated:',
                        font=('calibre', 10, 'bold')).grid(row=1, column=0)
    id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    sub_btn = tk.Button(root, text='Submit', command=lambda: validate_stud(id_var)).grid(row=2, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def validate_stud(id_var):
    if (len(id_var.get()) == 0):
        tk.Label(temp_root, text='ERROR: try again', fg="red", font=('calibre', 10, 'bold')).grid(row=3, column=0)
        id_var.set("")
    else:
        cnx = connect()
        cursor = cnx.cursor(prepared=True)
        data = (id_var.get().split())
        verify = ("SELECT COUNT(*) "
                  "FROM Student "
                  "WHERE student_id = %s")
        cursor.execute(verify, data)
        res = cursor.fetchall()
        cnx.commit()
        cursor.close()
        cnx.close()
        if (res[0][0] != 1):
            tk.Label(temp_root, text='ERROR: try again', fg="red", font=('calibre', 10, 'bold')).grid(row=3, column=0)
            id_var.set("")
        else:
            update_student(id_var)

def update_student(id_var):
    for widget in temp_root.winfo_children():
        widget.destroy()
    id = id_var.get()

    new_name_var = tk.StringVar()
    new_grade_var = tk.StringVar()
    new_gpa_var = tk.StringVar()
    new_dorm_var = tk.StringVar()
    new_class_var = tk.StringVar()
    new_advisor_var = tk.StringVar()

    name_label = tk.Label(temp_root, text='New Name', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    name_entry = tk.Entry(temp_root, textvariable=new_name_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    grade_label = tk.Label(temp_root, text='New Grade', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    grade_entry = tk.Entry(temp_root, textvariable=new_grade_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    gpa_label = tk.Label(temp_root, text='New GPA', font=('calibre', 10, 'bold')).grid(row=2, column=0)
    gpa_entry = tk.Entry(temp_root, textvariable=new_gpa_var, font=('calibre', 10, 'normal')).grid(row=2, column=1)

    dorm_label = tk.Label(temp_root, text='New Dormitory', font=('calibre', 10, 'bold')).grid(row=3, column=0)
    dorm_entry = tk.Entry(temp_root, textvariable=new_dorm_var, font=('calibre', 10, 'normal')).grid(row=3, column=1)

    classification_label = tk.Label(temp_root, text='New Classification', font=('calibre', 10, 'bold')).grid(row=4, column=0)
    classification_entry = tk.Entry(temp_root, textvariable=new_class_var, font=('calibre', 10, 'normal')).grid(
        row=4, column=1)

    adviser_label = tk.Label(temp_root, text='New Advisor', font=('calibre', 10, 'bold')).grid(row=5, column=0)
    adviser_entry = tk.Entry(temp_root, textvariable=new_advisor_var, font=('calibre', 10, 'normal')).grid(row=5, column=1)
    desc_label = tk.Label(temp_root, text='(Need to include input for all attributes, even if they remain the same)',
                          font=('calibre', 10, 'normal')).grid(row=6, column=0)
    sub_btn = tk.Button(temp_root, text='Submit',
                        command=lambda: commit_student_update(id, new_name_var, new_grade_var, new_gpa_var, new_dorm_var, new_class_var, new_advisor_var)).grid(row=7, column=1)
    back_btn = tk.Button(temp_root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def commit_student_update(id, new_name_var, new_grade_var, new_gpa_var, new_dorm_var, new_class_var, new_advisor_var):
    new_name = new_name_var.get()
    new_grade = new_grade_var.get()
    new_gpa = new_gpa_var.get()
    new_dorm = new_dorm_var.get()
    new_class = new_class_var.get()
    new_advisor = new_advisor_var.get()

    if (new_name == "" and new_grade == "" and new_gpa == "" and new_dorm == "" and new_class == "" and new_advisor == ""):
        # TODO print message about valid args
        change_page("back")
    else:
        cnx = connect()
        cursor = cnx.cursor(prepared=True)
        data = (new_name, new_grade, new_gpa, new_dorm, new_class, new_advisor, id)
        update = ("UPDATE Student "
                  "SET stu_name = %s, grade_level = %s, gpa = %s, dormitory_name = %s, classification = %s, advisor = %s "
                  "WHERE student_id = %s")
        cursor.execute(update, data)
        cnx.commit()
        cursor.close()
        cnx.close()

    new_name_var.set("")
    new_grade_var.set("")
    new_gpa_var.set("")
    new_dorm_var.set("")
    new_class_var.set("")
    new_advisor_var.set("")


def faculty_page(root):
    id_var = tk.StringVar()

    id_label = tk.Label(root, text='Please enter the current ID of the faculty to be updated:',
                        font=('calibre', 10, 'bold')).grid(row=1, column=0)
    id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    sub_btn = tk.Button(root, text='Submit', command=lambda: validate_fac(id_var)).grid(row=2, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def validate_fac(id_var):
    if (len(id_var.get()) == 0):
        tk.Label(temp_root, text='ERROR: try again', fg="red", font=('calibre', 10, 'bold')).grid(row=3, column=0)
        id_var.set("")
    else:
        cnx = connect()
        cursor = cnx.cursor(prepared=True)
        data = (id_var.get().split())
        verify = ("SELECT COUNT(*) "
                  "FROM Faculty "
                  "WHERE fac_id = %s")
        cursor.execute(verify, data)
        res = cursor.fetchall()
        cnx.commit()
        cursor.close()
        cnx.close()
        if (res[0][0] != 1):
            tk.Label(temp_root, text='ERROR: try again', fg="red", font=('calibre', 10, 'bold')).grid(row=3, column=0)
            id_var.set("")
        else:
            update_faculty(id_var)

def update_faculty(id_var):
    for widget in temp_root.winfo_children():
        widget.destroy()
    id = id_var.get()
    new_name_var = tk.StringVar()
    new_dept_var = tk.StringVar()
    new_salary_var = tk.StringVar()
    new_phone_var = tk.StringVar()
    new_office_var = tk.StringVar()
    new_building_var = tk.StringVar()

    new_name_label = tk.Label(temp_root, text='New Name', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    new_name_entry = tk.Entry(temp_root, textvariable=new_name_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    new_dept_label = tk.Label(temp_root, text='New Department', font=('calibre', 10, 'bold')).grid(row=2, column=0)
    new_dept_entry = tk.Entry(temp_root, textvariable=new_dept_var, font=('calibre', 10, 'normal')).grid(row=2,
                                                                                                             column=1)
    new_salary_label = tk.Label(temp_root, text='New Salary', font=('calibre', 10, 'bold')).grid(row=3, column=0)
    new_salary_entry = tk.Entry(temp_root, textvariable=new_salary_var, font=('calibre', 10, 'normal')).grid(row=3, column=1)

    new_phone_label = tk.Label(temp_root, text='New Phone Number', font=('calibre', 10, 'bold')).grid(row=4, column=0)
    new_phone_entry = tk.Entry(temp_root, textvariable=new_phone_var, font=('calibre', 10, 'normal')).grid(row=4, column=1)

    new_office_label = tk.Label(temp_root, text='New Office', font=('calibre', 10, 'bold')).grid(row=5, column=0)
    new_office_entry = tk.Entry(temp_root, textvariable=new_office_var, font=('calibre', 10, 'normal')).grid(row=5, column=1)

    new_building_label = tk.Label(temp_root, text='New Building', font=('calibre', 10, 'bold')).grid(row=6, column=0)
    new_building_entry = tk.Entry(temp_root, textvariable=new_building_var, font=('calibre', 10, 'normal')).grid(row=6, column=1)
    desc_label = tk.Label(temp_root, text='(Need to include input for all attributes, even if they remain the same)',
                          font=('calibre', 10, 'normal')).grid(row=7, column=0)
    sub_btn = tk.Button(temp_root, text='Submit',
                        command=lambda: commit_faculty_update(id, new_name_var, new_dept_var, new_salary_var, new_phone_var, new_office_var, new_building_var)).grid(row=7, column=1)
    back_btn = tk.Button(temp_root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def commit_faculty_update(id, new_name_var, new_dept_var, new_salary_var, new_phone_var, new_office_var, new_building_var):
    new_name = new_name_var.get()
    new_dept = new_dept_var.get()
    new_salary = new_salary_var.get()
    new_phone = new_phone_var.get()
    new_office = new_office_var.get()
    new_building = new_building_var.get()
    if (new_name == "" and new_dept == "" and new_salary == "" and new_phone == "" and new_office == "" and new_building == ""):
        # TODO print message about valid args
        change_page("back")
    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    data = (new_name, new_dept, new_salary, new_phone, new_office, new_building, id)
    update = ("UPDATE Faculty "
              "SET faculty_name = %s, department = %s, salary = %s, phone_number = %s, office = %s, building = %s "
              "WHERE fac_id = %s")
    cursor.execute(update, data)
    cnx.commit()
    cursor.close()
    cnx.close()

    new_name_var.set("")
    new_dept_var.set("")
    new_salary_var.set("")
    new_phone_var.set("")
    new_office_var.set("")
    new_building_var.set("")


def course_page(root):
    id_var = tk.StringVar()

    id_label = tk.Label(root, text='Please enter the current ID of the course to be updated:', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    sub_btn = tk.Button(root, text='Submit', command=lambda: validate_course(id_var)).grid(row=2, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def validate_course(id_var):
    if (len(id_var.get()) == 0):
        tk.Label(temp_root, text='ERROR: try again', fg="red", font=('calibre', 10, 'bold')).grid(row=3, column=0)
        id_var.set("")
    else:
        cnx = connect()
        cursor = cnx.cursor(prepared=True)
        data = (id_var.get().split())
        verify = ("SELECT COUNT(*) "
                  "FROM Course "
                  "WHERE course_id = %s")
        cursor.execute(verify, data)
        res = cursor.fetchall()
        cnx.commit()
        cursor.close()
        cnx.close()
        if (res[0][0] != 1):
            tk.Label(temp_root, text='ERROR: try again', fg="red", font=('calibre', 10, 'bold')).grid(row=3, column=0)
            id_var.set("")
        else:
            update_course(id_var)

def update_course(id_var):
    for widget in temp_root.winfo_children():
        widget.destroy()
    id = id_var.get()
    new_name_var = tk.StringVar()
    new_dept_var = tk.StringVar()

    new_name_label = tk.Label(temp_root, text='New Course Name', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    new_name_entry = tk.Entry(temp_root, textvariable=new_name_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)
    new_dept_label = tk.Label(temp_root, text='New Department', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    new_dept_entry = tk.Entry(temp_root, textvariable=new_dept_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)
    desc_label = tk.Label(temp_root, text='(Fields left blank will not modify the attribute)', font=('calibre', 10, 'normal')).grid(row=2, column=0)
    sub_btn = tk.Button(temp_root, text='Submit', command=lambda: commit_course_update(id, new_name_var, new_dept_var)).grid(row=2, column=1)
    back_btn = tk.Button(temp_root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def commit_course_update(id, new_name_var, new_dept_var):
    new_name = new_name_var.get()
    new_dept = new_dept_var.get()

    if (new_name == "" and new_dept == ""):
        # TODO print message about valid args
        change_page("back")
    else:
        cnx = connect()
        cursor = cnx.cursor(prepared=True)
        if (new_name == ""):
            data = (new_dept, id)
            update = ("UPDATE Course "
                      "SET department = %s "
                      "WHERE course_id = %s")
        elif (new_dept == ""):
            data = (new_name, id)
            update = ("UPDATE Course "
                      "SET course_name = %s "
                      "WHERE course_id = %s")
        else:
            data = (new_name, new_dept, id)
            update = ("UPDATE Course "
                      "SET course_name = %s, department = %s "
                      "WHERE course_id = %s")
        cursor.execute(update, data)
        cnx.commit()
        cursor.close()
        cnx.close()

    new_name_var.set("")
    new_dept_var.set("")


def b_page(root):
    id_var = tk.StringVar()

    id_label = tk.Label(root, text='Please enter the current name of the building to be updated:',
                        font=('calibre', 10, 'bold')).grid(row=1, column=0)
    id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    sub_btn = tk.Button(root, text='Submit', command=lambda: validate_b(id_var)).grid(row=2, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def validate_b(id_var):
    if (len(id_var.get()) == 0):
        tk.Label(temp_root, text='ERROR: try again', fg="red", font=('calibre', 10, 'bold')).grid(row=3, column=0)
        id_var.set("")
    else:
        cnx = connect()
        cursor = cnx.cursor(prepared=True)
        data = (id_var.get().split())
        print(data)
        verify = ("SELECT COUNT(*) "
                  "FROM Building "
                  "WHERE building_name = %s")
        cursor.execute(verify, data)
        res = cursor.fetchall()
        cnx.commit()
        cursor.close()
        cnx.close()
        if (res[0][0] != 1):
            print(res)
            tk.Label(temp_root, text='ERROR: try again', fg="red", font=('calibre', 10, 'bold')).grid(row=3, column=0)
            id_var.set("")
        else:
            update_building(id_var)


def update_building(id_var):
    for widget in temp_root.winfo_children():
        widget.destroy()
    id = id_var.get()
    new_name_var = tk.StringVar()
    new_add_var = tk.StringVar()

    new_name_label = tk.Label(temp_root, text='New Course Name', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    new_name_entry = tk.Entry(temp_root, textvariable=new_name_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)
    new_add_label = tk.Label(temp_root, text='New Department', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    new_add_entry = tk.Entry(temp_root, textvariable=new_add_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)
    desc_label = tk.Label(temp_root, text='(Fields left blank will not modify the attribute)', font=('calibre', 10, 'normal')).grid(row=2, column=0)
    sub_btn = tk.Button(temp_root, text='Submit', command=lambda: commit_building_update(id, new_name_var, new_add_var)).grid(row=2, column=1)
    back_btn = tk.Button(temp_root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def commit_building_update(id, new_name_var, new_add_var):
    new_name = new_name_var.get()
    new_add = new_add_var.get()

    if (new_name == "" and new_add == ""):
        # TODO print message about valid args
        change_page("back")
    else:
        cnx = connect()
        cursor = cnx.cursor(prepared=True)
        if (new_name == ""):
            data = (new_add, id)
            update = ("UPDATE Building "
                      "SET address = %s "
                      "WHERE building_name = %s")
        elif (new_add == ""):
            data = (new_name, id)
            update = ("UPDATE Building "
                      "SET building_name = %s "
                      "WHERE building_name = %s")
        else:
            data = (new_name, new_add, id)
            update = ("UPDATE Building "
                      "SET building_name = %s, address = %s "
                      "WHERE building_name = %s")
        cursor.execute(update, data)
        cnx.commit()
        cursor.close()
        cnx.close()

    new_name_var.set("")
    new_add_var.set("")


def dorm_page(root):
    name_var = tk.StringVar()

    name_label = tk.Label(root, text='Please enter the current name of the dormitory to be updated:',
                        font=('calibre', 10, 'bold')).grid(row=1, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    sub_btn = tk.Button(root, text='Submit', command=lambda: validate_dorm(name_var)).grid(row=2, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def validate_dorm(name_var):
    if (len(name_var.get()) == 0):
        tk.Label(temp_root, text='ERROR: try again', fg="red", font=('calibre', 10, 'bold')).grid(row=3, column=0)
        name_var.set("")
    else:
        cnx = connect()
        cursor = cnx.cursor(prepared=True)
        data = (name_var.get().split())
        verify = ("SELECT COUNT(*) "
                  "FROM Dormitory "
                  "WHERE dorm_name = %s")
        cursor.execute(verify, data)
        res = cursor.fetchall()
        cnx.commit()
        cursor.close()
        cnx.close()
        if (res[0][0] != 1):
            tk.Label(temp_root, text='ERROR: try again', fg="red", font=('calibre', 10, 'bold')).grid(row=3, column=0)
            name_var.set("")
        else:
            update_dorm(name_var)

def update_dorm(name_var):
    for widget in temp_root.winfo_children():
        widget.destroy()
    name = name_var.get()
    new_name_var = tk.StringVar()
    new_dine_var = tk.StringVar()
    new_add_var = tk.StringVar()

    new_name_label = tk.Label(temp_root, text='New Dormitory Name', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    new_name_entry = tk.Entry(temp_root, textvariable=new_name_var, font=('calibre', 10, 'normal')).grid(row=0,
                                                                                                         column=1)
    new_add_label = tk.Label(temp_root, text='New Address', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    new_add_entry = tk.Entry(temp_root, textvariable=new_add_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    new_dine_label = tk.Label(temp_root, text='New Dining Hall', font=('calibre', 10, 'bold')).grid(row=2, column=0)
    new_dine_entry = tk.Entry(temp_root, textvariable=new_dine_var, font=('calibre', 10, 'normal')).grid(row=2, column=1)
    desc_label = tk.Label(temp_root, text='(Need to include input for all attributes, even if they remain the same)',
                          font=('calibre', 10, 'normal')).grid(row=3, column=0)
    sub_btn = tk.Button(temp_root, text='Submit',
                        command=lambda: commit_dorm_update(id, new_name_var, new_add_var, new_dine_var)).grid(row=3, column=1)
    back_btn = tk.Button(temp_root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def commit_dorm_update(id, new_name_var, new_add_var, new_dine_var):
    new_name = new_name_var.get()
    new_add = new_add_var.get()
    new_dine = new_dine_var.get()

    if (new_name == "" or new_add == "" or new_dine == ""):
        # TODO print message about valid args
        change_page("back")
    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    data = (new_name, new_add, new_dine, id)
    update = ("UPDATE Dormitory "
              "SET dorm_name = %s, address = %s, dining_hall = %s "
              "WHERE dorm_name = %s")
    cursor.execute(update, data)
    cnx.commit()
    cursor.close()
    cnx.close()

    new_name_var.set("")
    new_add_var.set("")
    new_dine_var.set("")


def dept_page(root):
    name_var = tk.StringVar()

    namelabel = tk.Label(root, text='Please enter the current name of the department to be updated:',
                        font=('calibre', 10, 'bold')).grid(row=1, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    sub_btn = tk.Button(root, text='Submit', command=lambda: validate_dept(name_var)).grid(row=2, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def validate_dept(name_var):
    if (len(name_var.get()) == 0):
        tk.Label(temp_root, text='ERROR: try again', fg="red", font=('calibre', 10, 'bold')).grid(row=3, column=0)
        name_var.set("")
    else:
        cnx = connect()
        cursor = cnx.cursor(prepared=True)
        data = (name_var.get().split())
        verify = ("SELECT COUNT(*) "
                  "FROM Department "
                  "WHERE dept_name = %s")
        cursor.execute(verify, data)
        res = cursor.fetchall()
        cnx.commit()
        cursor.close()
        cnx.close()
        if (res[0][0] != 1):
            tk.Label(temp_root, text='ERROR: try again', fg="red", font=('calibre', 10, 'bold')).grid(row=3, column=0)
            name_var.set("")
        else:
            update_dept(name_var)

def update_dept(name_var):
    for widget in temp_root.winfo_children():
        widget.destroy()
    name = name_var.get()
    new_name_var = tk.StringVar()
    new_chair_var = tk.StringVar()
    new_b_var = tk.StringVar()

    new_name_label = tk.Label(temp_root, text='New Department Name', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    new_name_entry = tk.Entry(temp_root, textvariable=new_name_var, font=('calibre', 10, 'normal')).grid(row=0,
                                                                                                         column=1)
    new_chair_label = tk.Label(temp_root, text='New Chair', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    new_chair_entry = tk.Entry(temp_root, textvariable=new_chair_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    new_b_label = tk.Label(temp_root, text='New Building', font=('calibre', 10, 'bold')).grid(row=2, column=0)
    new_b_entry = tk.Entry(temp_root, textvariable=new_b_var, font=('calibre', 10, 'normal')).grid(row=2, column=1)
    desc_label = tk.Label(temp_root, text='(Need to include input for all attributes, even if they remain the same)',
                          font=('calibre', 10, 'normal')).grid(row=3, column=0)
    sub_btn = tk.Button(temp_root, text='Submit',
                        command=lambda: commit_dept_update(id, new_name_var, new_chair_var, new_b_var)).grid(row=3, column=1)
    back_btn = tk.Button(temp_root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def commit_dept_update(id, new_name_var, new_chair_var, new_b_var):
    new_name = new_name_var.get()
    new_chair = new_chair_var.get()
    new_b = new_b_var.get()

    if (len(new_name) == 0 or len(new_chair) == 0 or len(new_b) == 0):
        # TODO print message about valid args
        change_page("back")
    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    data = (new_name, new_chair, new_b, id)
    update = ("UPDATE Department "
              "SET dept_name = %s, chair = %s, building = %s "
              "WHERE dept_name = %s")
    cursor.execute(update, data)
    cnx.commit()
    cursor.close()
    cnx.close()

    #new_name_var.set("")
    #new_chair_var.set("")
    #new_b_var.set("")


def club_page(root):
    name_var = tk.StringVar()

    name_label = tk.Label(root, text='Please enter the current name of the department to be updated:',
                         font=('calibre', 10, 'bold')).grid(row=1, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    sub_btn = tk.Button(root, text='Submit', command=lambda: validate_club(name_var)).grid(row=2, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def validate_club(name_var):
    if (len(name_var.get()) == 0):
        tk.Label(temp_root, text='ERROR: try again', fg="red", font=('calibre', 10, 'bold')).grid(row=3, column=0)
        name_var.set("")
    else:
        cnx = connect()
        cursor = cnx.cursor(prepared=True)
        data = (name_var.get().split())
        verify = ("SELECT COUNT(*) "
                  "FROM Club "
                  "WHERE club_name = %s")
        cursor.execute(verify, data)
        res = cursor.fetchall()
        cnx.commit()
        cursor.close()
        cnx.close()
        if (res[0][0] != 1):
            tk.Label(temp_root, text='ERROR: try again', fg="red", font=('calibre', 10, 'bold')).grid(row=3, column=0)
            name_var.set("")
        else:
            update_club(name_var)

def update_club(name_var):
    for widget in temp_root.winfo_children():
        widget.destroy()
    name = name_var.get()
    new_name_var = tk.StringVar()
    new_super_var = tk.StringVar()
    new_fund_var = tk.StringVar()
    new_b_var = tk.StringVar()

    new_name_label = tk.Label(temp_root, text='New Department Name', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    new_name_entry = tk.Entry(temp_root, textvariable=new_name_var, font=('calibre', 10, 'normal')).grid(row=0,
                                                                                                         column=1)
    new_super_label = tk.Label(temp_root, text='New Supervisor', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    new_super_entry = tk.Entry(temp_root, textvariable=new_super_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    new_fund_label = tk.Label(temp_root, text='New Building', font=('calibre', 10, 'bold')).grid(row=2, column=0)
    new_fund_entry = tk.Entry(temp_root, textvariable=new_fund_var, font=('calibre', 10, 'normal')).grid(row=2, column=1)

    new_b_label = tk.Label(temp_root, text='New Building', font=('calibre', 10, 'bold')).grid(row=3, column=0)
    new_b_entry = tk.Entry(temp_root, textvariable=new_b_var, font=('calibre', 10, 'normal')).grid(row=3,
                                                                                                         column=1)
    desc_label = tk.Label(temp_root, text='(Need to include input for all attributes, even if they remain the same)',
                          font=('calibre', 10, 'normal')).grid(row=4, column=0)
    sub_btn = tk.Button(temp_root, text='Submit',
                        command=lambda: commit_club_update(id, new_name_var, new_super_var, new_fund_var, new_b_var)).grid(row=4, column=1)
    back_btn = tk.Button(temp_root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)

def commit_club_update(id, new_name_var, new_super_var, new_fund_var, new_b_var):
    new_name = new_name_var.get()
    new_super = new_super_var.get()
    new_fund = new_fund_var.get()
    new_b = new_b_var.get()

    if (new_name == "" or new_super == "" or new_fund == "" or new_b == ""):
        # TODO print message about valid args
        change_page("back")
    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    data = (new_name, new_super, new_fund, new_b, id)
    update = ("UPDATE Club "
              "SET club_name = %s, supervisor_id = %s, funding = %s, building_name = %s "
              "WHERE club_name = %s")
    cursor.execute(update, data)
    cnx.commit()
    cursor.close()
    cnx.close()


def cr_page(root):
    room_var = tk.StringVar()
    b_var = tk.StringVar()

    room_label = tk.Label(root, text='Please enter the current classroom number to be updated:',
                         font=('calibre', 10, 'bold')).grid(row=1, column=0)
    room_entry = tk.Entry(root, textvariable=room_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)
    b_label = tk.Label(root, text='Please enter the building of the classroom:',
                         font=('calibre', 10, 'bold')).grid(row=2, column=0)
    b_entry = tk.Entry(root, textvariable=b_var, font=('calibre', 10, 'normal')).grid(row=2, column=1)

    sub_btn = tk.Button(root, text='Submit', command=lambda: validate_cr(room_var, b_var)).grid(row=3, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def validate_cr(room_var, b_var):
    if (len(room_var.get()) == 0 or len(b_var.get()) == 0):
        tk.Label(temp_root, text='ERROR: try again', fg="red", font=('calibre', 10, 'bold')).grid(row=3, column=0)
        room_var.set("")
        b_var.set("")
    else:
        cnx = connect()
        cursor = cnx.cursor(prepared=True)
        data = (room_var.get(), b_var.get())
        verify = ("SELECT COUNT(*) "
                  "FROM Classroom "
                  "WHERE room_number = %s AND building_name = %s")
        cursor.execute(verify, data)
        res = cursor.fetchall()
        cnx.commit()
        cursor.close()
        cnx.close()
        if (res[0][0] != 1):
            tk.Label(temp_root, text='ERROR: try again', fg="red", font=('calibre', 10, 'bold')).grid(row=3, column=0)
            room_var.set("")
            b_var.set("")
        else:
            update_cr(room_var, b_var)

def update_cr(room_var, b_var):
    for widget in temp_root.winfo_children():
        widget.destroy()
    room = room_var.get()
    b = b_var.get()
    new_room_var = tk.StringVar()
    new_b_var = tk.StringVar()
    new_c_var = tk.StringVar()

    new_room_label = tk.Label(temp_root, text='New Room Number', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    new_room_entry = tk.Entry(temp_root, textvariable=new_room_var, font=('calibre', 10, 'normal')).grid(row=0,
                                                                                                         column=1)
    new_b_label = tk.Label(temp_root, text='New Building', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    new_b_entry = tk.Entry(temp_root, textvariable=new_b_var, font=('calibre', 10, 'normal')).grid(row=1,
                                                                                                           column=1)
    new_c_label = tk.Label(temp_root, text='New Capacity', font=('calibre', 10, 'bold')).grid(row=2, column=0)
    new_c_entry = tk.Entry(temp_root, textvariable=new_c_var, font=('calibre', 10, 'normal')).grid(row=2,
                                                                                                         column=1)
    desc_label = tk.Label(temp_root, text='(Need to include input for all attributes, even if they remain the same)',
                          font=('calibre', 10, 'normal')).grid(row=3, column=0)
    sub_btn = tk.Button(temp_root, text='Submit',
                        command=lambda: commit_cr_update(room, b, new_room_var, new_b_var, new_c_var)).grid(row=3, column=1)
    back_btn = tk.Button(temp_root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def commit_cr_update(room, b, new_room_var, new_b_var, new_c_var):
    new_room = new_room_var.get()
    new_c = new_c_var.get()
    new_b = new_b_var.get()

    if (new_room == "" or new_c == "" or new_b == ""):
        # TODO print message about valid args
        change_page("back")
    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    data = (new_room, new_b, new_c, room, b)
    update = ("UPDATE Classroom "
              "SET room_number = %s, building_name = %s, capacity = %s "
              "WHERE room_number = %s AND building_name = %s")
    cursor.execute(update, data)
    cnx.commit()
    cursor.close()
    cnx.close()


def cs_page(root):
    secid_var = tk.StringVar()
    cid_var = tk.StringVar()

    secid_label = tk.Label(root, text='Please enter the course ID of the course to be updated:',
                        font=('calibre', 10, 'bold')).grid(row=1, column=0)
    secid_entry = tk.Entry(root, textvariable=secid_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    cid_label = tk.Label(root, text='Please enter the section ID of the course to be updated:',
                           font=('calibre', 10, 'bold')).grid(row=2, column=0)
    cid_entry = tk.Entry(root, textvariable=cid_var, font=('calibre', 10, 'normal')).grid(row=2, column=1)

    sub_btn = tk.Button(root, text='Submit', command=lambda: validate_cs(secid_var, cid_var)).grid(row=3, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def validate_cs(secid_var, cid_var):
    if (len(secid_var.get()) == 0 or len(cid_var.get()) == 0):
        tk.Label(temp_root, text='ERROR: try again', fg="red", font=('calibre', 10, 'bold')).grid(row=3, column=0)
        secid_var.set("")
        cid_var.set("")
    else:
        cnx = connect()
        cursor = cnx.cursor(prepared=True)
        data = (secid_var.get(), cid_var.get())
        verify = ("SELECT COUNT(*) "
                  "FROM CourseSection "
                  "WHERE section_id = %s AND course_id = %s")
        cursor.execute(verify, data)
        res = cursor.fetchall()
        cnx.commit()
        cursor.close()
        cnx.close()
        if (res[0][0] != 1):
            tk.Label(temp_root, text='ERROR: try again', fg="red", font=('calibre', 10, 'bold')).grid(row=3, column=0)
            secid_var.set("")
            cid_var.set("")
        else:
            update_cs(secid_var, cid_var)


def update_cs(secid_var, cid_var):
    for widget in temp_root.winfo_children():
        widget.destroy()
    secid = secid_var.get()
    cid = cid_var.get()
    new_i_var = tk.StringVar()
    new_b_var = tk.StringVar()

    new_i_label = tk.Label(temp_root, text='New Instructor ID', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    new_i_entry = tk.Entry(temp_root, textvariable=new_i_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)
    new_b_label = tk.Label(temp_root, text='New Building', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    new_b_entry = tk.Entry(temp_root, textvariable=new_b_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)
    desc_label = tk.Label(temp_root, text='(Need to include input for all attributes, even if they remain the same)',
                          font=('calibre', 10, 'normal')).grid(row=2, column=0)
    sub_btn = tk.Button(temp_root, text='Submit',
                        command=lambda: commit_cs_update(secid, cid, new_i_var, new_b_var)).grid(row=2, column=1)
    back_btn = tk.Button(temp_root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def commit_cs_update(secid, cid, new_i_var, new_b_var):
    new_i = new_i_var.get()
    new_b = new_b_var.get()

    if (new_i == "" or new_b == ""):
        # TODO print message about valid args
        change_page("back")
    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    data = (new_i, new_b, secid, cid)
    update = ("UPDATE CourseSection "
              "SET instructor_id = %s, building_name = %s "
              "WHERE section_id = %s AND course_id = %s")
    cursor.execute(update, data)
    cnx.commit()
    cursor.close()
    cnx.close()


def change_page(table):
    for widget in temp_root.winfo_children():
        widget.destroy()
    if table == "back":
        modify_home(temp_root)
    elif table == "main":
        main.home(temp_root)
    elif table == "Student":
        student_page(temp_root)
    elif table == "Faculty":
        faculty_page(temp_root)
    elif table == "Course":
        course_page(temp_root)
    elif table == "Course Section":
        cs_page(temp_root)
    elif table == "Dormitory":
        dorm_page(temp_root)
    elif table == "Department":
        dept_page(temp_root)
    elif table == "Classroom":
        cr_page(temp_root)
    elif table == "Club":
        club_page(temp_root)
    elif table == "Building":
        b_page(temp_root)
