import tkinter

user_data = []

class UserInfo:
    def __init__(self, user_info: dict):
        self.user_info = user_info
        self.titles = ["", "Mr.", "Ms.", "Dr."]
        self.nationality = ["India", "Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"]

    def insert(self):
        if self.validate_input_data():
            user_full_name = self.user_info['first_name'] + " " + self.user_info['last_name']
            index, record = self.get_users(user_full_name)
            if record:
                self.raise_warning(f"User exists already")
            else:
                user_data.append(self.user_info)
                self.raiise_success("Inserted user successfully")

    def update(self):
        if self.validate_input_data():
            user_full_name = self.user_info['first_name'] + " " + self.user_info['last_name']
            index, record = self.get_users(user_full_name)
            if not record:
                self.raise_warning(f"User doesn't exist")
            else:
                del user_data[index]
                user_data.insert(index, self.user_info)
                self.raiise_success("Updated user successfully")

    def get_users(self, full_user_name: str = None):
        if full_user_name:
            for index, record in enumerate(user_data):
                if (record['first_name'] in full_user_name) and (record['last_name'] in full_user_name):
                    return index, record
            return None, None
        else:
            return None, user_data

    def delete(self, user_name):
        # user_name = self.user_info['first_name'] + " " + self.user_info['last_name']
        index, record = self.get_users(user_name)
        print(f"index : {index}")
        if record:
            del user_data[index]
            self.raiise_success("Deleted user successfully")
        else:
            self.raise_warning(f"User doesn't exist")

    def validate_input_data(self):
        try:
            error_field = 'Age'
            self.user_info["age"] = int(self.user_info.get("age"))
            error_field = "# Competed Courses"
            self.user_info["competed_courses"] = int(self.user_info.get("competed_courses"))
            error_field = "# Semesters"
            self.user_info["semesters"] = int(self.user_info.get("semesters"))
        except:
            self.raise_warning(f"Provide valid integers of {error_field}")
            return False

        if self.user_info.get("accepted_tc") != "Accepted":
            self.raise_warning("Accepted the Terms & Conditions")
            return False
        if not (self.user_info.get("first_name") and self.user_info.get("last_name")):
            self.raise_warning("First Name and Last Name are required")
            return False
        if not (self.user_info.get("title") in self.titles):
            self.raise_warning("Provide valid Title")
            return False
        if not (self.user_info.get("age") >= 18):
            self.raise_warning("Provide valid Age")
            return False
        if not (self.user_info.get("nationality") in self.nationality):
            self.raise_warning("Provide valid Nationality")
            return False
        return True

    def raise_warning(self, error_message):
        tkinter.messagebox.showwarning(title="Error", message=error_message)

    def raiise_success(self, success_message):
        tkinter.messagebox.showinfo(title="Success", message=success_message)