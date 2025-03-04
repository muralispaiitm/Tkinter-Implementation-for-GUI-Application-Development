import tkinter
from tkinter import ttk
from tkinter import messagebox
import uuid

from executions import UserInfo

def fetch_form_details():
    user_info = {}
    user_info['id'] = uuid.uuid4()
    user_info['first_name'] = entry_first_name.get()
    user_info['last_name'] = entry_last_name.get()
    user_info['title'] = combobox_title.get()
    user_info['age'] = spinbox_age.get()
    user_info['nationality'] = combobox_nationality.get()

    user_info['registered'] = var_reg_status.get()
    user_info['competed_courses'] = spinbox_num_courses.get()
    user_info['semesters'] = spinbox_num_semesters.get()

    user_info['accepted_tc'] = var_accepted.get()
    return user_info

def insert_user():
    user_info = fetch_form_details()
    UI = UserInfo(user_info)
    UI.insert()

def update_user():
    user_info = fetch_form_details()
    UI = UserInfo(user_info)
    UI.update()

def delete_user():
    user_info = fetch_form_details()
    user_name = user_info['first_name'] + " " + user_info['last_name']
    UI = UserInfo({})
    UI.delete(user_name)


def fetch_user():
    user_info = fetch_form_details()
    user_name = user_info['first_name'] + " " + user_info['last_name']
    UI = UserInfo({})
    index, record = UI.get_users(user_name)
    if record:
        tkinter.messagebox.showinfo(title="Success", message=record)
    else:
        tkinter.messagebox.showwarning(title="Error", message="User doesn't exists")

def fetch_all_users():
    UI = UserInfo({})
    _, record = UI.get_users()
    if record:
        tkinter.messagebox.showinfo(title="Success", message=record)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
entry_window = tkinter.Tk()
entry_window.title("Entry Form")

frame_main = tkinter.Frame(entry_window)
frame_main.pack()

# ------ USER INFORMATION ------
label_frame_user_info = tkinter.LabelFrame(frame_main, text="User Information")
label_frame_user_info.grid(row=0, column=0, padx=20, pady=10)

label_first_name = tkinter.Label(label_frame_user_info, text="First Name")
label_first_name.grid(row=0, column=0)
entry_first_name = tkinter.Entry(label_frame_user_info)
entry_first_name.grid(row=1, column=0)

label_last_name = tkinter.Label(label_frame_user_info, text="Last Name")
label_last_name.grid(row=0, column=1)
entry_last_name = tkinter.Entry(label_frame_user_info)
entry_last_name.grid(row=1, column=1)

label_title = tkinter.Label(label_frame_user_info, text="Title")
label_title.grid(row=0, column=2)
combobox_title = ttk.Combobox(label_frame_user_info, values=["", "Mr.", "Ms.", "Dr."])
combobox_title.grid(row=1, column=2)

label_age = tkinter.Label(label_frame_user_info, text="Age")
label_age.grid(row=2, column=0)
spinbox_age = tkinter.Spinbox(label_frame_user_info, from_=18, to=120)
spinbox_age.grid(row=3, column=0)

label_nationality = tkinter.Label(label_frame_user_info, text="Nationality")
label_nationality.grid(row=2, column=1)
combobox_nationality = ttk.Combobox(label_frame_user_info, values=["India", "Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
combobox_nationality.grid(row=3, column=1)

# Paddings for all the above widgets
for widget in label_frame_user_info.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# ------ COURSE INFORMATION ------
label_frame_courses_info = tkinter.LabelFrame(frame_main, text="Course Information")
label_frame_courses_info.grid(row=1, column=0, sticky="news", padx=20, pady=10)

label_registered = tkinter.Label(label_frame_courses_info, text="Registration Status")
label_registered.grid(row=0, column=0)

var_reg_status = tkinter.StringVar(value="Not Registered")
checkbutton_registered = tkinter.Checkbutton(label_frame_courses_info, text="Registered",
                                             variable=var_reg_status, onvalue='Registered',
                                             offvalue="Not Registered")
checkbutton_registered.grid(row=1, column=0)

label_num_courses = tkinter.Label(label_frame_courses_info, text="# Completed Courses")
label_num_courses.grid(row=0, column=1)
spinbox_num_courses = tkinter.Spinbox(label_frame_courses_info, from_=0, to="infinity")
spinbox_num_courses.grid(row=1, column=1)

label_num_semesters = tkinter.Label(label_frame_courses_info, text="# Semesters")
label_num_semesters.grid(row=0, column=2)
spinbox_num_semesters = tkinter.Spinbox(label_frame_courses_info, from_=0, to="infinity")
spinbox_num_semesters.grid(row=1, column=2)

# Paddings for all the above widgets
for widget in label_frame_courses_info.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# ------ TERMS & CONDITIONS ------
label_frame_terms_info = tkinter.LabelFrame(frame_main, text="Terms & Conditions")
label_frame_terms_info.grid(row=2, column=0, sticky="news", padx=20, pady=10)

var_accepted = tkinter.StringVar(value="Not Accepted")
checkbutton_terms = tkinter.Checkbutton(label_frame_terms_info,
                                        text="I accept the terms and conditions.",
                                        variable=var_accepted,
                                        onvalue="Accepted", offvalue="Not Accepted")
checkbutton_terms.grid(row=0, column=0)



# ------ SUBMIT BUTTON ------
button_insert = tkinter.Button(frame_main, text="INSERT", command=insert_user)
# button_insert.grid(row=3, column=0, sticky="news", padx=20, pady=10)
button_insert.grid(row=3, column=0, padx=20, pady=10)

button_update = tkinter.Button(frame_main, text="UPDATE", command=update_user)
button_update.grid(row=3, column=1, padx=20, pady=10)

button_update = tkinter.Button(frame_main, text="DELETE", command=delete_user)
button_update.grid(row=4, column=0, padx=20, pady=10)

button_get = tkinter.Button(frame_main, text="FETCH", command=fetch_user)
button_get.grid(row=4, column=1, padx=20, pady=10)

button_get = tkinter.Button(frame_main, text="FETCH_ALL", command=fetch_all_users)
button_get.grid(row=4, column=2, padx=20, pady=10)

entry_window.mainloop()