import tkinter as tk
import mysql.connector
from tkinter import *
import main as main


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

#----- v Student page and selection v --------
def student_page(root):
        id_var = tk.StringVar()

        id_label = tk.Label(root, text='Student ID', font=('calibre', 10, 'bold')).grid(row=0, column=0)
        id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

        sub_btn = tk.Button(root, text='QUERY', command=lambda: select_student(id_var)).grid(row=1, column=1)
        back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)

def select_student(id_var):
    if(len(id_var.get()) == 0):
       # TODO print message about valid args
      change_page("back")
      return

    id = id_var.get()

    cnx = connect()
    cursor = cnx.cursor()
    student_data = (id,)
    selection = ("QUERY FROM Student WHERE student_id = %s")
    cursor.execute(selection, student_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    # TODO print success message
    change_page("main")

#----- v Faculty page and selection v --------
def faculty_page(root):
    id_var = tk.StringVar()

    id_label = tk.Label(root, text='Faculty ID', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    sub_btn = tk.Button(root, text='QUERY', command=lambda: select_faculty(id_var)).grid(row=1, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def select_faculty(id_var):
    if (len(id_var.get()) == 0):
        # TODO print message about valid args
        change_page("back")
        return

    id = id_var.get()

    cnx = connect()
    cursor = cnx.cursor()
    faculty_data = (id,)
    selection = ("delete "
                "from Faculty "
                "where fac_id = %s) ")

    cursor.execute(selection, faculty_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    #TODO print success message
    change_page("main")

#----- v Dormitory page and selection v --------
def dormitory_page(root):
    name_var = tk.StringVar()

    name_label = tk.Label(root, text='Dormitory Name', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    sub_btn = tk.Button(root, text='QUERY',
                        command=lambda: select_dormitory(name_var)).grid(row=1, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def select_dormitory(name_var):
    if (len(name_var.get()) == 0):
        # TODO print message about valid args
        change_page("back")
        return

    name = name_var.get()

    cnx = connect()
    cursor = cnx.cursor()
    dormitory_data = (name,)
    selection = ("delete "
                "from Dormitory "
                "where name = %s) ")

    cursor.execute(selection, dormitory_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    # TODO print success message
    change_page("main")

#----- v Course page and selection v --------
def course_page(root):
    id_var = tk.StringVar()

    id_label = tk.Label(root, text='Course ID', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    sub_btn = tk.Button(root, text='QUERY',
                        command=lambda: select_course(id_var)).grid(row=1, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def select_course(id_var):
    if (len(id_var.get()) == 0):
        # TODO print message about valid args
        change_page("back")
        return

    id = id_var.get()

    cnx = connect()
    cursor = cnx.cursor()
    course_data = (id,)
    selection = ("delete "
                "from Course "
                "where id = %s) ")

    cursor.execute(selection, course_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    # TODO print success message
    change_page("main")

#----- v CourseSection page and selection v --------

def course_section_page(root):
    sec_id_var = tk.StringVar()
    course_id_var = tk.StringVar()

    sec_id_label = tk.Label(root, text='Section ID', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    sec_id_entry = tk.Entry(root, textvariable=sec_id_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    course_id_label = tk.Label(root, text='Course ID', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    course_id_entry = tk.Entry(root, textvariable=course_id_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    sub_btn = tk.Button(root, text='QUERY',
                        command=lambda: select_course_section(sec_id_var, course_id_var).grid(row=7, column=1))
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back").grid(row=2, column=6))


def select_course_section(sec_id_var, course_id_var, instr_id_var, building_var):
    if (len(sec_id_var.get()) == 0 or len(course_id_var.get()) == 0):
        # TODO print message about valid args
        change_page("back")
        return

    sec_id = sec_id_var.get()
    course_id = course_id_var.get()

    cnx = connect()
    cursor = cnx.cursor()
    course_section_data = (sec_id, course_id)
    selection = ("delete "
                "from Student "
                "where section_id = %s AND course_id = %s) ")

    cursor.execute(selection, course_section_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    # TODO print success message
    change_page("main")


#----- v Department page and selection v --------
def department_page(root):
    name_var = tk.StringVar()

    name_label = tk.Label(root, text='Department Name', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    sub_btn = tk.Button(root, text='QUERY',
                        command=lambda: select_department(name_var)).grid(row=1, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def select_department(name_var):
    if (len(name_var.get()) == 0):
        # TODO print message about valid args
        change_page("back")
        return

    name = name_var.get()

    cnx = connect()
    cursor = cnx.cursor()
    department_data = (name,)
    selection = ("delete "
                "from Department "
                "where id = %s) ")

    cursor.execute(selection, department_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    # TODO print success message
    change_page("main")


#----- v Classroom page and selection v --------
def classroom_page(root):
    room_var = tk.StringVar()
    building_var = tk.StringVar()
    cap_var = tk.StringVar()

    name_label = tk.Label(root, text='Room Number', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    name_entry = tk.Entry(root, textvariable=room_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    building_label = tk.Label(root, text='Building', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    building_entry = tk.Entry(root, textvariable=building_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    sub_btn = tk.Button(root, text='QUERY',
                        command=lambda: select_classroom(room_var, building_var)).grid(row=2, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def select_classroom(room_var, building_var):
    if (len(room_var.get()) == 0 or len(building_var.get()) == 0):
        # TODO print message about valid args
        change_page("back")
        return

    room = room_var.get()
    building = building_var.get()

    cnx = connect()
    cursor = cnx.cursor()
    classrooom_data = (room, building)
    selection = ("delete "
                "from Classroom "
                "where room_number = %s AND building_name = %s) ")
    cursor.execute(selection, classrooom_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    # TODO print success message
    change_page("main")


#----- v Club page and selection v --------
def club_page(root):
    name_var = tk.StringVar()

    name_label = tk.Label(root, text='Club Name', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    sub_btn = tk.Button(root, text='QUERY',
                        command=lambda: select_club(name_var)).grid(row=1, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def select_club(name_var):
    if (len(name_var.get()) == 0):
        # TODO print message about valid args
        change_page("back")
        return

    name = name_var.get()

    cnx = connect()
    cursor = cnx.cursor()
    club_data = (name,)
    selection = ("delete "
                "from Club "
                "where club_name = %s) ")

    cursor.execute(selection, club_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    # TODO print success message
    change_page("main")

#----- v Building page and selection v --------
def building_page(root):
    name_var = tk.StringVar()

    name_label = tk.Label(root, text='Building Name', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    sub_btn = tk.Button(root, text='QUERY',
                        command=lambda: select_building(name_var)).grid(row=1, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def select_building(name_var):
    if (len(name_var.get()) == 0):
        # TODO print message about valid args
        change_page("back")
        return

    name = name_var.get()

    cnx = connect()
    cursor = cnx.cursor()
    building_data = (name,)
    selection = ("delete "
                "from Building "
                "where building_name = %s) ")

    cursor.execute(selection, building_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    # TODO print success message
    change_page("main")



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