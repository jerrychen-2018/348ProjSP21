import mysql.connector
import tkinter as tk;

window = tk.Tk()

width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.title("School System 348")

id_var = tk.StringVar()
name_var = tk.StringVar()
grade_var = tk.StringVar()
gpa_var = tk.StringVar()
dorm_var = tk.StringVar()
classification_var = tk.StringVar()
adviser_var = tk.StringVar()


def get_attributes():
    id = id_var.get()
    name = name_var.get()
    grade = grade_var.get()
    gpa = gpa_var.get()
    dorm = dorm_var.get()
    classification = classification_var.get()
    adviser = adviser_var.get()

    print("The id is : " + id)
    print("The name is : " + name)
    print("The grade is : " + grade)
    print("The gpa is : " + gpa)
    print("The classification is : " + classification)
    print("The adviser is : " + adviser)
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


# id
id_label = tk.Label(window, text='ID', font=('calibre', 10, 'bold'))
id_entry = tk.Entry(window, textvariable=id_var, font=('calibre', 10, 'normal'))
# name
name_label = tk.Label(window, text='Name', font=('calibre', 10, 'bold'))
name_entry = tk.Entry(window, textvariable=name_var, font=('calibre', 10, 'normal'))
# grade
grade_label = tk.Label(window, text='grade', font=('calibre', 10, 'bold'))
grade_entry = tk.Entry(window, textvariable=grade_var, font=('calibre', 10, 'normal'))
# gpa
gpa_label = tk.Label(window, text='gpa', font=('calibre', 10, 'bold'))
gpa_entry = tk.Entry(window, textvariable=gpa_var, font=('calibre', 10, 'normal'))
# dorm
dorm_label = tk.Label(window, text='dorm', font=('calibre', 10, 'bold'))
dorm_entry = tk.Entry(window, textvariable=dorm_var, font=('calibre', 10, 'normal'))
# classification
classification_label = tk.Label(window, text='classification', font=('calibre', 10, 'bold'))
classification_entry = tk.Entry(window, textvariable=classification_var, font=('calibre', 10, 'normal'))
# adviser
adviser_label = tk.Label(window, text='adviser', font=('calibre', 10, 'bold'))
adviser_entry = tk.Entry(window, textvariable=adviser_var, font=('calibre', 10, 'normal'))

sub_btn = tk.Button(window, text='Create', command=get_attributes)

id_label.grid(row=0, column=0)
id_entry.grid(row=0, column=1)
name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
grade_label.grid(row=2, column=0)
grade_entry.grid(row=2, column=1)
gpa_label.grid(row=3, column=0)
gpa_entry.grid(row=3, column=1)
dorm_label.grid(row=4, column=0)
dorm_entry.grid(row=4, column=1)
classification_label.grid(row=5, column=0)
classification_entry.grid(row=5, column=1)
adviser_label.grid(row=6, column=0)
adviser_entry.grid(row=6, column=1)

sub_btn.grid(row=7, column=1)

window.mainloop()
