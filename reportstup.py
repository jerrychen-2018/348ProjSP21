# file created by Rohan Shankar
import mysql.connector
import tkinter as tk;

window = tk.Tk()
mystring = tk.StringVar(window)

width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.title("School System Stored Procedures")

frame = tk.LabelFrame(window)
frame.grid(row=0, column=1)


def disableAllButtons():
    button1['state'] = 'disabled'
    button2['state'] = 'disabled'
    button3['state'] = 'disabled'
    button4['state'] = 'disabled'
    button5['state'] = 'disabled'
    button6['state'] = 'disabled'
    button7['state'] = 'disabled'
    button8['state'] = 'disabled'


def clear():
    for widget in frame.winfo_children():
        widget.destroy()
    frame.grid_remove()
    button1['state'] = 'normal'
    button2['state'] = 'normal'
    button3['state'] = 'normal'
    button4['state'] = 'normal'
    button5['state'] = 'normal'
    button6['state'] = 'normal'
    button7['state'] = 'normal'
    button8['state'] = 'normal'


def clickButton():
    disableAllButtons()
    frame.grid()
    prompt = tk.Label(frame, text="        Which class?")
    prompt.grid(row=0, column=2)
    courseName = tk.Entry(frame, textvariable=mystring)
    courseName.grid(row=0, column=3)
    eButton = tk.Button(frame, text='Enter', width=15, command=getQuery1)
    eButton.grid(row=0, column=4)


def clickButton2():
    disableAllButtons()
    frame.grid()
    prompt = tk.Label(frame, text="        Which class?")
    prompt.grid(row=0, column=2)
    courseName = tk.Entry(frame, textvariable=mystring)
    courseName.grid(row=0, column=3)
    eButton = tk.Button(frame, text='Enter', width=15, command=getQuery2)
    eButton.grid(row=0, column=4)


def clickButton3():
    disableAllButtons()
    frame.grid()
    getQuery3()


def clickButton4():
    disableAllButtons()
    frame.grid()
    getQuery4()


def clickButton5():
    disableAllButtons()
    frame.grid()
    prompt = tk.Label(frame, text="        Which professor?")
    prompt.grid(row=0, column=2)
    courseName = tk.Entry(frame, textvariable=mystring)
    courseName.grid(row=0, column=3)
    eButton = tk.Button(frame, text='Enter', width=15, command=getQuery5)
    eButton.grid(row=0, column=4)


def clickButton6():
    disableAllButtons()
    frame.grid()
    prompt = tk.Label(frame, text="        Which professor?")
    prompt.grid(row=0, column=2)
    courseName = tk.Entry(frame, textvariable=mystring)
    courseName.grid(row=0, column=3)
    eButton = tk.Button(frame, text='Enter', width=15, command=getQuery6)
    eButton.grid(row=0, column=4)


def clickButton7():
    disableAllButtons()
    frame.grid()
    prompt = tk.Label(frame, text="        Enter a student id")
    prompt.grid(row=0, column=2)
    courseName = tk.Entry(frame, textvariable=mystring)
    courseName.grid(row=0, column=3)
    eButton = tk.Button(frame, text='Enter', width=15, command=getQuery7)
    eButton.grid(row=0, column=4)


def clickButton8():
    frame.grid()
    cnx = mysql.connector.connect(user='root', password='rohanjerrytroy',
                                  host='35.224.65.220',
                                  database='schoolsystem')
    cursor = cnx.cursor()
    query = "drop index idx1 on Course;"
    cursor.execute(query)
    query = "drop index idx2 on Faculty;"
    cursor.execute(query)
    query = "create index idx1 on Course(course_name);"
    cursor.execute(query)
    query = "create index idx2 on Faculty(faculty_name);"
    cursor.execute(query)
    outputSuccess = tk.Label(frame, text="Index Creation Successful!")
    outputSuccess.grid(row=0, column=2)


def getQuery1():
    cName = mystring.get()
    print("cName is " + cName)

    cnx = mysql.connector.connect(user='root', password='rohanjerrytroy',
                                  host='35.224.65.220',
                                  database='schoolsystem')
    cursor = cnx.cursor(prepared=True)

    query = "select s.stu_name, c.course_name from EnrolledIn e, Student s, Course c  where e.course_id = c.course_id and e.student_id = s.student_id and course_name = %s"

    cursor.execute(query, (cName,))
    i = 0
    j = 5
    s_nameLabel = tk.Label(frame, text="student_name   ", font='Helvetica 18 bold')
    s_nameLabel.grid(row=i, column=j)
    c_nameLabel = tk.Label(frame, text="course_name", font='Helvetica 18 bold')
    c_nameLabel.grid(row=0, column=j + 1)
    for (student_name, course_name) in cursor:
        s_name = tk.Label(frame, text=student_name)
        s_name.grid(row=i + 1, column=j)
        c_name = tk.Label(frame, text=course_name)
        c_name.grid(row=i + 1, column=j + 1)
        i = i + 1
        print(i)
        print(j)

    cnx.commit()
    cursor.close()
    cnx.close()


def getQuery2():
    cName = mystring.get()
    print("cName is " + cName)
    cnx = mysql.connector.connect(user='root', password='rohanjerrytroy',
                                  host='35.224.65.220',
                                  database='schoolsystem')
    cursor = cnx.cursor(prepared=True)
    query = "select distinct f.faculty_name, c.course_name from Faculty f, Course c, CourseSection cs where c.course_id = cs.course_id and f.fac_id = cs.instructor_id and c.course_name = %s"
    print(query)
    cursor.execute(query, (cName,))
    i = 0
    j = 5
    s_nameLabel = tk.Label(frame, text="faculty_name   ", font='Helvetica 18 bold')
    s_nameLabel.grid(row=i, column=j)
    c_nameLabel = tk.Label(frame, text="course_name", font='Helvetica 18 bold')
    c_nameLabel.grid(row=0, column=j + 1)
    for (student_name, course_name) in cursor:
        s_name = tk.Label(frame, text=student_name)
        s_name.grid(row=i + 1, column=j)
        c_name = tk.Label(frame, text=course_name)
        c_name.grid(row=i + 1, column=j + 1)
        i = i + 1
        print(i)
        print(j)

    cnx.commit()
    cursor.close()
    cnx.close()


def getQuery3():
    cnx = mysql.connector.connect(user='root', password='rohanjerrytroy',
                                  host='35.224.65.220',
                                  database='schoolsystem')
    cursor = cnx.cursor(prepared=True)
    query = "select s.stu_name, bt.club_name from Student s, BelongsTo bt where s.student_id = bt.student_id;"
    print(query)
    cursor.execute(query)
    i = 0
    j = 5
    s_nameLabel = tk.Label(frame, text="Output:", font='Helvetica 18 bold')
    s_nameLabel.grid(row=i, column=j)
    for (student_name, course_name) in cursor:
        s_name = tk.Label(frame, text=student_name)
        s_name.grid(row=i + 1, column=j)
        c_name = tk.Label(frame, text=course_name)
        c_name.grid(row=i + 1, column=j + 1)
        i = i + 1
        print(i)
        print(j)

    cnx.commit()
    cursor.close()
    cnx.close()
    print(query)
    cursor.execute(query)
    i = 0
    j = 5
    s_nameLabel = tk.Label(frame, text="Output:", font='Helvetica 18 bold')
    s_nameLabel.grid(row=i, column=j)
    for (student_name, course_name) in cursor:
        s_name = tk.Label(frame, text=student_name)
        s_name.grid(row=i + 1, column=j)
        c_name = tk.Label(frame, text=course_name)
        c_name.grid(row=i + 1, column=j + 1)
        i = i + 1
        print(i)
        print(j)

    cnx.commit()
    cursor.close()
    cnx.close()


def getQuery4():
    # print("cName is " +  mystring.get())
    cnx = mysql.connector.connect(user='root', password='rohanjerrytroy',
                                  host='35.224.65.220',
                                  database='schoolsystem')
    cursor = cnx.cursor(prepared=True)
    query = "select dorm_name, dining_hall from Dormitory where dining_hall <> 'NULL';"
    print(query)
    cursor.execute(query)
    i = 0
    j = 5
    s_nameLabel = tk.Label(frame, text="Output:", font='Helvetica 18 bold')
    s_nameLabel.grid(row=i, column=j)
    for (student_name, course_name) in cursor:
        s_name = tk.Label(frame, text=student_name)
        s_name.grid(row=i + 1, column=j)
        c_name = tk.Label(frame, text=course_name)
        c_name.grid(row=i + 1, column=j + 1)
        i = i + 1
        print(i)
        print(j)

    cnx.commit()
    cursor.close()
    cnx.close()


def getQuery5():
    cName = mystring.get()
    print("cName is " + cName)
    cnx = mysql.connector.connect(user='root', password='rohanjerrytroy',
                                  host='35.224.65.220',
                                  database='schoolsystem')
    cursor = cnx.cursor(prepared=True)
    query = "select distinct cs.section_id, c.course_name from Faculty f, Course c, CourseSection cs where c.course_id = cs.course_id and f.fac_id = cs.instructor_id and f.faculty_name = %s"
    print(query)
    cursor.execute(query, (cName,))
    i = 0
    j = 5
    s_nameLabel = tk.Label(frame, text="section_id   ", font='Helvetica 18 bold')
    s_nameLabel.grid(row=i, column=j)
    c_nameLabel = tk.Label(frame, text="course_name", font='Helvetica 18 bold')
    c_nameLabel.grid(row=0, column=j + 1)
    for (student_name, course_name) in cursor:
        s_name = tk.Label(frame, text=student_name)
        s_name.grid(row=i + 1, column=j)
        c_name = tk.Label(frame, text=course_name)
        c_name.grid(row=i + 1, column=j + 1)
        i = i + 1
        print(i)
        print(j)

    cnx.commit()
    cursor.close()
    cnx.close()


def getQuery6():
    cName = mystring.get()
    cnx = mysql.connector.connect(user='root', password='rohanjerrytroy',
                                  host='35.224.65.220',
                                  database='schoolsystem')
    cursor = cnx.cursor()
    query = "call RateAProfessor(%s, @rating);"
    query2 = "select @rating as Rating;"
    print(query)
    cursor.execute(query, (cName,))
    cursor.execute(query2)
    i = 0
    j = 5
    s_nameLabel = tk.Label(frame, text="Output:", font='Helvetica 18 bold')
    s_nameLabel.grid(row=i, column=j)
    for (student_name) in cursor:
        s_name = tk.Label(frame, text=student_name)
        s_name.grid(row=i + 1, column=j)

    cnx.commit()
    cursor.close()
    cnx.close()


def getQuery7():
    cName = mystring.get()
    cnx = mysql.connector.connect(user='root', password='rohanjerrytroy',
                                  host='35.224.65.220',
                                  database='schoolsystem')
    cursor = cnx.cursor()
    query = "call RateMyCourses(%s, @r);"
    query2 = "select @r as 'Your Course Ratings';"
    print(query)
    cursor.execute(query, (cName,))
    cursor.execute(query2)
    i = 0
    j = 5
    s_nameLabel = tk.Label(frame, text="Output:", font='Helvetica 18 bold')
    s_nameLabel.grid(row=i, column=j)
    for (student_name) in cursor:
        s_name = tk.Label(frame, text=student_name)
        s_name.grid(row=i + 1, column=j)

    cnx.commit()
    cursor.close()
    cnx.close()


button1 = tk.Button(window, text="1) Get all names of students in a specific class", command=clickButton)
button2 = tk.Button(window, text="2) Get all professors teaching a specific course", command=clickButton2)
button3 = tk.Button(window, text="3) Get names of all students that are club leaders", command=clickButton3)
button4 = tk.Button(window, text="4) List which dorms have dining halls", command=clickButton4)
button5 = tk.Button(window, text="5) See how many individual courses a professor is teaching", command=clickButton5)
button6 = tk.Button(window, text="6) Rate a Professor's Difficulty", command=clickButton6)
button7 = tk.Button(window, text="7) Rate my Courses", command=clickButton7)
button8 = tk.Button(window, text="8) Create indexes", command=clickButton8)
clearButton = tk.Button(window, text="Clear", command=clear)

button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)
button4.grid(row=3, column=0)
button5.grid(row=4, column=0)
button6.grid(row=5, column=0)
button7.grid(row=6, column=0)
button8.grid(row=7, column=0)
clearButton.grid(row=9, column=0)

window.mainloop()