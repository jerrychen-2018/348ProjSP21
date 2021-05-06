import tkinter as tk
import mysql.connector
from tkinter import *
import main as main
from tkinter import messagebox



def connect():
    cnx = mysql.connector.connect(user='root', password='rohanjerrytroy',
                                  host='35.224.65.220',
                                  database='schoolsystem')
    return cnx

def insert_home(root):
    global temp_root
    temp_root = root
    for widget in root.winfo_children():
        widget.destroy()

    table_options = [
        "Student",
        "Faculty",
        "Dormitory",
        "Course",
        "CourseSection",
        "Department",
        "Classroom",
        "Club",
        "Building"
    ]

    clicked = tk.StringVar()
    clicked.set(table_options[0])
    drop = OptionMenu(root, clicked, *table_options).grid(row=2, column=5)
    myButton = tk.Button(root, text="Confirm Selection", command=lambda: change_page(clicked.get())).grid(row=2, column=6)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("main")).grid(row=2, column=7)

#----- v Student page and insertion v --------
def student_page(root):
        id_var = tk.StringVar()
        name_var = tk.StringVar()
        grade_var = tk.StringVar()
        gpa_var = tk.StringVar()
        dorm_var = tk.StringVar()
        classification_var = tk.StringVar()
        adviser_var = tk.StringVar()

        name_label = tk.Label(root, text='Name', font=('calibre', 10, 'bold')).grid(row=1, column=0)
        name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

        grade_label = tk.Label(root, text='Grade', font=('calibre', 10, 'bold')).grid(row=2, column=0)
        grade_entry = tk.Entry(root, textvariable=grade_var, font=('calibre', 10, 'normal')).grid(row=2, column=1)

        gpa_label = tk.Label(root, text='GPA', font=('calibre', 10, 'bold')).grid(row=3, column=0)
        gpa_entry = tk.Entry(root, textvariable=gpa_var, font=('calibre', 10, 'normal')).grid(row=3, column=1)

        dorm_label = tk.Label(root, text='Dormitory', font=('calibre', 10, 'bold')).grid(row=4, column=0)
        dorm_entry = tk.Entry(root, textvariable=dorm_var, font=('calibre', 10, 'normal')).grid(row=4, column=1)

        classification_label = tk.Label(root, text='Classification', font=('calibre', 10, 'bold')).grid(row=5, column=0)
        classification_entry = tk.Entry(root, textvariable=classification_var, font=('calibre', 10, 'normal')).grid(
            row=5, column=1)

        adviser_label = tk.Label(root, text='Advisor', font=('calibre', 10, 'bold')).grid(row=6, column=0)
        adviser_entry = tk.Entry(root, textvariable=adviser_var, font=('calibre', 10, 'normal')).grid(row=6, column=1)

        sub_btn = tk.Button(root, text='ADD', command=lambda: insert_student(name_var, grade_var, gpa_var, dorm_var, classification_var, adviser_var)).grid(row=7, column=1)
        back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)

def insert_student(name_var, grade_var, gpa_var, dorm_var, classification_var, adviser_var):
    if(len(name_var.get()) == 0 or len(grade_var.get()) == 0 or len(gpa_var.get()) == 0 or len(dorm_var.get()) == 0 or len(classification_var.get()) == 0 or len(adviser_var.get()) == 0):
        messagebox.showinfo("showinfo", "Valid Arguments Required")
        change_page("back")
        return


    name = name_var.get()
    grade = grade_var.get()
    gpa = gpa_var.get()
    dorm = dorm_var.get()
    classification = classification_var.get()
    adviser = adviser_var.get()

    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    student_data = (name, grade, gpa, dorm, classification, adviser)
    insertion = ("INSERT INTO Student "
                 "(stu_name, grade_level, gpa, dormitory_name, classification, advisor) "
                 "VALUES (%s, %s, %s, %s, %s, %s)")
    cursor.execute(insertion, student_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    messagebox.showinfo("showinfo", "Insertion Successful!")
    change_page("main")

#----- v Faculty page and insertion v --------
def faculty_page(root):
    id_var = tk.StringVar()
    name_var = tk.StringVar()
    dept_var = tk.StringVar()
    salary_var = tk.StringVar()
    phone_var = tk.StringVar()
    office_var = tk.StringVar()
    building_var = tk.StringVar()

    id_label = tk.Label(root, text='Faculty ID', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    name_label = tk.Label(root, text='Name', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    dept_label = tk.Label(root, text='Department', font=('calibre', 10, 'bold')).grid(row=2, column=0)
    dept_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=2, column=1)

    salary_label = tk.Label(root, text='Salary', font=('calibre', 10, 'bold')).grid(row=3, column=0)
    salary_entry = tk.Entry(root, textvariable=salary_var, font=('calibre', 10, 'normal')).grid(row=3, column=1)

    phone_label = tk.Label(root, text='phone', font=('calibre', 10, 'bold')).grid(row=4, column=0)
    phone_entry = tk.Entry(root, textvariable=phone_var, font=('calibre', 10, 'normal')).grid(row=4, column=1)

    office_label = tk.Label(root, text='Office', font=('calibre', 10, 'bold')).grid(row=5, column=0)
    office_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=5, column=1)

    building_label = tk.Label(root, text='Building', font=('calibre', 10, 'bold')).grid(row=6, column=0)
    building_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=6, column=1)

    sub_btn = tk.Button(root, text='ADD', command=lambda: insert_faculty(id_var, name_var, dept_var, salary_var, phone_var, office_var, building_var)).grid(row=7, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def insert_faculty(id_var, name_var, dept_var, salary_var, phone_var, office_var, building_var):
    if (len(id_var.get()) == 0 or len(name_var.get()) == 0 or len(salary_var.get()) == 0 or len(
            phone_var.get()) == 0 or len(office_var.get()) == 0 or len(building_var.get()) == 0):
        messagebox.showinfo("showinfo", "Valid Arguments Required")
        change_page("back")
        return

    id = id_var.get()
    name = name_var.get()
    dept = dept_var.get()
    salary = salary_var.get()
    phone = phone_var.get()
    office = office_var.get()
    building = building_var.get()

    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    faculty_data = (id, name, dept, salary, phone, office, building)
    insertion = ("INSERT INTO Facultly "
                 "(fac_id, faculty_name, department, salary, phone_number, office, building) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s)")

    cursor.execute(insertion, faculty_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    #TODO print success message
    change_page("main")

#----- v Dormitory page and insertion v --------
def dormitory_page(root):
    name_var = tk.StringVar()
    dining_var = tk.StringVar()
    address_var = tk.StringVar()

    name_label = tk.Label(root, text='Dormitory Name', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    dining_label = tk.Label(root, text='Dining Hall', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    dinng_entry = tk.Entry(root, textvariable=dining_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    address_label = tk.Label(root, text='Address', font=('calibre', 10, 'bold')).grid(row=2, column=0)
    address_entry = tk.Entry(root, textvariable=address_var, font=('calibre', 10, 'normal')).grid(row=2, column=1)

    sub_btn = tk.Button(root, text='ADD',
                        command=lambda: insert_dormitory(name_var, dining_var, address_var)).grid(row=3, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def insert_dormitory(name_var, dining_var, address_var):
    if (len(name_var.get()) == 0 or len(dining_var.get()) == 0 or len(address_var.get()) == 0):
        messagebox.showinfo("showinfo", "Valid Arguments Required")
        change_page("back")
        return

    name = name_var.get()
    dining = dining_var.get()
    address = address_var.get()

    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    dormitory_data = (name, dining, address)
    insertion = ("INSERT INTO Dormitory "
                 "(dorm_name, address, dining_hall) "
                 "VALUES (%s, %s, %s)")

    cursor.execute(insertion, dormitory_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    messagebox.showinfo("showinfo", "Insertion Successful!")
    change_page("main")

#----- v Course page and insertion v --------
def course_page(root):
    id_var = tk.StringVar()
    name_var = tk.StringVar()
    dept_var = tk.StringVar()

    id_label = tk.Label(root, text='Course ID', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    name_label = tk.Label(root, text='Course Name', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    dept_label = tk.Label(root, text='Course Department', font=('calibre', 10, 'bold')).grid(row=2, column=0)
    dept_entry = tk.Entry(root, textvariable=dept_var, font=('calibre', 10, 'normal')).grid(row=2, column=1)

    sub_btn = tk.Button(root, text='ADD',
                        command=lambda: insert_course(id_var, name_var, dept_var)).grid(row=3, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def insert_course(id_var, name_var, dept_var):
    if (len(id_var.get()) == 0 or len(name_var.get()) == 0 or len(dept_var.get()) == 0):
        messagebox.showinfo("showinfo", "Valid Arguments Required")
        change_page("back")
        return

    id = id_var.get()
    name = name_var.get()
    dept = dept_var.get()

    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    course_data = (id, name, dept)
    insertion = ("INSERT INTO Course "
                 "(course_id, course_name, department) "
                 "VALUES (%s, %s, %s)")

    cursor.execute(insertion, course_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    messagebox.showinfo("showinfo", "Insertion Successful!")
    change_page("main")

#----- v CourseSection page and insertion v --------

def course_section_page(root):
    sec_id_var = tk.StringVar()
    course_id_var = tk.StringVar()
    instr_id_var = tk.StringVar()
    building_var = tk.StringVar()

    sec_id_label = tk.Label(root, text='Section ID', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    sec_id_entry = tk.Entry(root, textvariable=sec_id_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    course_id_label = tk.Label(root, text='Course ID', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    course_id_entry = tk.Entry(root, textvariable=course_id_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    instr_id_label = tk.Label(root, text='Instructor ID', font=('calibre', 10, 'bold')).grid(row=2, column=0)
    instr_id_entry = tk.Entry(root, textvariable=instr_id_var, font=('calibre', 10, 'normal')).grid(row=2, column=1)

    building_label = tk.Label(root, text='Building', font=('calibre', 10, 'bold')).grid(row=3, column=0)
    building_entry = tk.Entry(root, textvariable=building_var, font=('calibre', 10, 'normal')).grid(row=3, column=1)

    sub_btn = tk.Button(root, text='ADD',
                        command=lambda: insert_course_section(sec_id_var, course_id_var, instr_id_var, building_var)).grid(row=4, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def insert_course_section(sec_id_var, course_id_var, instr_id_var, building_var):
    if (len(sec_id_var.get()) == 0 or len(course_id_var.get()) == 0 or len(instr_id_var.get()) == 0 or len(
            building_var.get()) == 0):
        messagebox.showinfo("showinfo", "Valid Arguments Required")
        change_page("back")
        return

    sec_id = sec_id_var.get()
    course_id = course_id_var.get()
    instr_id = instr_id_var.get()
    building = building_var.get()

    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    course_section_data = (sec_id, course_id, instr_id, building)
    insertion = ("INSERT INTO CourseSection "
                 "(section_id, course_id, instructor_id, building) "
                 "VALUES (%s, %s, %s, %s)")

    cursor.execute(insertion, course_section_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    messagebox.showinfo("showinfo", "Insertion Successful!")
    change_page("main")


#----- v Department page and insertion v --------
def department_page(root):
    name_var = tk.StringVar()
    chair_var = tk.StringVar()
    building_var = tk.StringVar()

    name_label = tk.Label(root, text='Department Name', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    chair_label = tk.Label(root, text='Chair Name', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    chair_entry = tk.Entry(root, textvariable=chair_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    building_label = tk.Label(root, text='Building', font=('calibre', 10, 'bold')).grid(row=2, column=0)
    building_entry = tk.Entry(root, textvariable=building_var, font=('calibre', 10, 'normal')).grid(row=2, column=1)

    sub_btn = tk.Button(root, text='ADD',
                        command=lambda: insert_department(name_var, chair_var, building_var)).grid(row=3, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def insert_department(name_var, chair_var, building_var):
    if (len(name_var.get()) == 0 or len(chair_var.get()) == 0 or len(building_var.get()) == 0):
        messagebox.showinfo("showinfo", "Valid Arguments Required")
        change_page("back")
        return

    name = name_var.get()
    chair = chair_var.get()
    building = building_var.get()

    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    department_data = (name, chair, building)
    insertion = ("INSERT INTO Department "
                 "(dept_name, chair, building) "
                 "VALUES (%s, %s, %s)")

    cursor.execute(insertion, department_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    messagebox.showinfo("showinfo", "Insertion Successful!")
    change_page("main")


#----- v Classroom page and insertion v --------
def classroom_page(root):
    room_var = tk.StringVar()
    building_var = tk.StringVar()
    cap_var = tk.StringVar()

    name_label = tk.Label(root, text='Room Number', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    name_entry = tk.Entry(root, textvariable=room_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    building_label = tk.Label(root, text='Building', font=('calibre', 10, 'bold')).grid(row=2, column=0)
    building_entry = tk.Entry(root, textvariable=building_var, font=('calibre', 10, 'normal')).grid(row=2, column=1)

    cap_label = tk.Label(root, text='Capacity', font=('calibre', 10, 'bold')).grid(row=3, column=0)
    cap_entry = tk.Entry(root, textvariable=cap_var, font=('calibre', 10, 'normal')).grid(row=3, column=1)

    sub_btn = tk.Button(root, text='ADD',
                        command=lambda: insert_classroom(room_var, building_var, cap_var)).grid(row=4, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def insert_classroom(room_var, building_var, cap_var):
    if (len(room_var.get()) == 0 or len(building_var.get()) == 0 or len(cap_var.get()) == 0):
        messagebox.showinfo("showinfo", "Valid Arguments Required")
        change_page("back")
        return

    room = room_var.get()
    building = building_var.get()
    cap = cap_var.get()

    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    classrooom_data = (room, building, cap)
    insertion = ("INSERT INTO Classroom "
                 "(room_number, building_name, capacity) "
                 "VALUES (%s, %s, %s)")

    cursor.execute(insertion, classrooom_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    messagebox.showinfo("showinfo", "Insertion Successful!")
    change_page("main")


#----- v Club page and insertion v --------
def club_page(root):
    name_var = tk.StringVar()
    sup_id_var = tk.StringVar()
    funding_var = tk.StringVar()
    building_var = tk.StringVar()


    name_label = tk.Label(root, text='Club Name', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    sup_id_label = tk.Label(root, text='Supervisor ID', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    sup_id_entry = tk.Entry(root, textvariable=sup_id_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    funding_label = tk.Label(root, text='Funding', font=('calibre', 10, 'bold')).grid(row=2, column=0)
    funding_entry = tk.Entry(root, textvariable=funding_var, font=('calibre', 10, 'normal')).grid(row=2, column=1)

    building_label = tk.Label(root, text='Building', font=('calibre', 10, 'bold')).grid(row=3, column=0)
    building_entry = tk.Entry(root, textvariable=building_var, font=('calibre', 10, 'normal')).grid(row=3, column=1)

    sub_btn = tk.Button(root, text='ADD',
                        command=lambda: insert_club(name_var, sup_id_var, funding_var, building_var)).grid(row=4, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def insert_club(name_var, sup_id_var, funding_var, building_var):
    if (len(name_var.get()) == 0 or len(sup_id_var.get()) == 0 or len(funding_var.get()) == 0 or len(
            building_var.get()) == 0):
        messagebox.showinfo("showinfo", "Valid Arguments Required")
        change_page("back")
        return

    name = name_var.get()
    sup_id = sup_id_var.get()
    funding = funding_var.get()
    building = building_var.get()

    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    club_data = (name, sup_id, funding, building)
    insertion = ("INSERT INTO Club"
                 "(club_name, supervisor_id, funding, building_name) "
                 "VALUES (%s, %s, %s, %s)")

    cursor.execute(insertion, club_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    messagebox.showinfo("showinfo", "Insertion Successful!")
    change_page("main")

#----- v Building page and insertion v --------
def building_page(root):
    name_var = tk.StringVar()
    address_var = tk.StringVar()
    handi_var = tk.StringVar()

    name_label = tk.Label(root, text='Building Name', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    address_label = tk.Label(root, text='Address', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    address_entry = tk.Entry(root, textvariable=address_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    handi_label = tk.Label(root, text='Has Handicap Access (yes/no)', font=('calibre', 10, 'bold')).grid(row=2, column=0)
    handi_entry = tk.Entry(root, textvariable=handi_var, font=('calibre', 10, 'normal')).grid(row=2, column=1)

    sub_btn = tk.Button(root, text='ADD',
                        command=lambda: insert_building(name_var, address_var, handi_var)).grid(row=3, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def insert_building(name_var, address_var, handi_var):
    if (len(name_var.get()) == 0 or len(address_var.get()) == 0 or len(handi_var.get()) == 0):
        messagebox.showinfo("showinfo", "Valid Arguments Required")
        change_page("back")
        return

    name = name_var.get()
    address = address_var.get()
    handi = handi_var.get()

    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    building_data = (name, address, handi)
    insertion = ("INSERT INTO Building"
                 "(building_name, address, HasHandicapAccess) "
                 "VALUES (%s, %s, %s)")

    cursor.execute(insertion, building_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    messagebox.showinfo("showinfo", "Insertion Successful!")
    change_page("main")



def change_page(table):
    for widget in temp_root.winfo_children():
        widget.destroy()
    if table == "back":
        insert_home(temp_root)
    elif table == "main":
        main.home(temp_root)
    elif table == "Student":
        student_page(temp_root)
    elif table == "Faculty":
        faculty_page(temp_root)
    elif table == "Dormitory":
        dormitory_page(temp_root)
    elif table == "Course":
        course_page(temp_root)
    elif table == "CourseSection":
        course_section_page(temp_root)
    elif table == "Department":
        department_page(temp_root)
    elif table == "Classroom":
       classroom_page(temp_root)
    elif table == "Club":
        club_page(temp_root)
    elif table == "Building":
        building_page(temp_root)