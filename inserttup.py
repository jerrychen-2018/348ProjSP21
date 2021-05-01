import tkinter as tk
import mysql.connector


def page1(root):
    id_var = tk.StringVar()
    name_var = tk.StringVar()
    grade_var = tk.StringVar()
    gpa_var = tk.StringVar()
    dorm_var = tk.StringVar()
    classification_var = tk.StringVar()
    adviser_var = tk.StringVar()

    # entry boxes and their labels

    id_label = tk.Label(root, text='Student ID', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    name_label = tk.Label(root, text='Name', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    grade_label = tk.Label(root, text='Grade', font=('calibre', 10, 'bold')).grid(row=2, column=0)
    grade_entry = tk.Entry(root, textvariable=grade_var, font=('calibre', 10, 'normal')).grid(row=2, column=1)

    gpa_label = tk.Label(root, text='GPA', font=('calibre', 10, 'bold')).grid(row=3, column=0)
    gpa_entry = tk.Entry(root, textvariable=gpa_var, font=('calibre', 10, 'normal')).grid(row=3, column=1)

    dorm_label = tk.Label(root, text='Dormitory', font=('calibre', 10, 'bold')).grid(row=4, column=0)
    dorm_entry = tk.Entry(root, textvariable=dorm_var, font=('calibre', 10, 'normal')).grid(row=4, column=1)

    classification_label = tk.Label(root, text='Classification', font=('calibre', 10, 'bold')).grid(row=5, column=0)
    classification_entry = tk.Entry(root, textvariable=classification_var, font=('calibre', 10, 'normal')).grid(row=5, column=1)

    adviser_label = tk.Label(root, text='Advisor', font=('calibre', 10, 'bold')).grid(row=6, column=0)
    adviser_entry = tk.Entry(root, textvariable=adviser_var, font=('calibre', 10, 'normal')).grid(row=6, column=1)
    sub_btn = tk.Button(root, text='Create', command=lambda: get_std_atrb(id_var, name_var, grade_var, gpa_var, dorm_var, classification_var, adviser_var)).grid(row=7, column=1)

    tk.Label(root, text = 'This is the Students page for adding Students to the Students table').grid(row = 8)
    tk.Button(root, text='To Student Insert Page', command=lambda: changepage(1)).grid(row=9, column=0)
    tk.Button(root, text='To Faculty Insert Page', command=lambda: changepage(2)).grid(row=9, column=1)
    tk.Button(root, text='To Course Insert Page', command=lambda: changepage(3)).grid(row=9, column=2)


def page2(root):
    id_var = tk.StringVar()
    name_var = tk.StringVar()
    sal_var = tk.StringVar()
    phone_var = tk.StringVar()

    # entry boxes and their labels

    id_label = tk.Label(root, text='Faculty ID', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    name_label = tk.Label(root, text='Name', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    sal_label = tk.Label(root, text='Salary', font=('calibre', 10, 'bold')).grid(row=2, column=0)
    sal_entry = tk.Entry(root, textvariable=sal_var, font=('calibre', 10, 'normal')).grid(row=2, column=1)

    phone_label = tk.Label(root, text='Phone Number', font=('calibre', 10, 'bold')).grid(row=3, column=0)
    phone_entry = tk.Entry(root, textvariable=phone_var, font=('calibre', 10, 'normal')).grid(row=3, column=1)

    sub_btn = tk.Button(root, text='Create',
                        command=lambda: get_fac_atrb(id_var, name_var, sal_var, phone_var)).grid(row=4, column=1)
    tk.Label(root, text='This is the Faculty page for adding faculty to the Faculty table').grid(row=5)
    tk.Button(root, text='To Student Insert Page', command=lambda: changepage(1)).grid(row=6, column=0)
    tk.Button(root, text='To Faculty Insert Page', command=lambda: changepage(2)).grid(row=6, column=1)
    tk.Button(root, text='To Course Insert Page', command=lambda: changepage(3)).grid(row=6, column=2)


def page3(root):
    id_var = tk.StringVar()
    name_var = tk.StringVar()

    # entry boxes and their labels

    id_label = tk.Label(root, text='Course ID', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    name_label = tk.Label(root, text='Course Name', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    sub_btn = tk.Button(root, text='Create',
                        command=lambda: get_c_atrb(id_var, name_var)).grid(row=2, column=1)

    tk.Label(root, text='This is the Faculty page for adding faculty to the Faculty table').grid(row=3)
    tk.Button(root, text='To Student Insert Page', command=lambda: changepage(1)).grid(row=4, column=0)
    tk.Button(root, text='To Faculty Insert Page', command=lambda: changepage(2)).grid(row=4, column=1)
    tk.Button(root, text='To Course Insert Page', command=lambda: changepage(3)).grid(row=4, column=2)


def get_std_atrb(id_var, name_var, grade_var, gpa_var, dorm_var, classification_var, adviser_var):
    id = id_var.get()
    name = name_var.get()
    grade = grade_var.get()
    gpa = gpa_var.get()
    dorm = dorm_var.get()
    classification = classification_var.get()
    adviser = adviser_var.get()

    cnx = mysql.connector.connect(user='root', password='rohanjerrytroy',
                                  host='35.224.65.220',
                                  database='schoolsystem')

    # Do not forget to use try, except, finally when accessing the database

    cursor = cnx.cursor()
    student_data = (id, name, grade, gpa, dorm, classification, adviser)
    insertion = ("INSERT INTO Student "
                 "(student_id, stu_name, grade_level, gpa, dormitory_name, classification, advisor) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(insertion, student_data)

    cnx.commit()
    cursor.close()
    cnx.close()

    id_var.set("")
    name_var.set("")
    grade_var.set("")
    gpa_var.set("")
    dorm_var.set("")
    classification_var.set("")
    adviser_var.set("")


def get_fac_atrb(id_var, name_var, sal_var, phone_var):
    id = id_var.get()
    name = name_var.get()
    sal = sal_var.get()
    phone = phone_var.get()

    cnx = mysql.connector.connect(user='root', password='rohanjerrytroy',
                                  host='35.224.65.220',
                                  database='schoolsystem')

    # Do not forget to use try, except, finally when accessing the database

    cursor = cnx.cursor()
    fac_data = (id, name, sal, phone)
    insertion = ("INSERT INTO Faculty "
                 "(fac_id, fac_name, salary, phone_number) "
                 "VALUES (%s, %s, %s, %s)")
    cursor.execute(insertion, fac_data)

    cnx.commit()
    cursor.close()
    cnx.close()

    id_var.set("")
    name_var.set("")
    sal_var.set("")
    phone_var.set("")


def get_c_atrb(id_var, name_var):
    id = id_var.get()
    name = name_var.get()

    cnx = mysql.connector.connect(user='root', password='rohanjerrytroy',
                                  host='35.224.65.220',
                                  database='schoolsystem')

    # Do not forget to use try, except, finally when accessing the database

    cursor = cnx.cursor()
    c_data = (id, name)
    insertion = ("INSERT INTO Course "
                 "(course_id, course_name) "
                 "VALUES (%s, %s)")
    cursor.execute(insertion, c_data)

    cnx.commit()
    cursor.close()
    cnx.close()

    id_var.set("")
    name_var.set("")


def changepage(page_num):
    global root
    for widget in root.winfo_children():
        widget.destroy()
    if page_num == 1:
        page1(root)
    elif page_num == 2:
        page2(root)
    elif page_num == 3:
        page3(root)

root = tk.Tk()
width = 1000
height = 1000
root.geometry("%dx%d" % (width, height))
root.title("School System 348")
page1(root)
root.mainloop()