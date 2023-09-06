from maxselen import *
from config import *
from security import *


class DrivingScholl(Maxselen):
    def __init__(self):
        super().__init__()

    def login(self):
        self.Web.get(URL)
        self.Web.find_element(NAME, "username").send_keys(USER)
        self.Web.find_element(NAME, "password").send_keys(PASSWORD)
        self.Web.find_element(CLASS, "submit-row").find_element(TAG, "input").click()
        time.sleep(1)


    def add_person(self):
        self.login()
        self.Web.find_element(CLASS, "model-person").find_element(CLASS, "addlink").click()

        self.Web.find_element(XPATH, f_name).send_keys(fake.first_name)

        self.type_to_xpath(l_name, fake.last_name)
        self.type_to_xpath(mid_name, fake.first.name)

        self.select_id("id_sex", str(random.randint(0, 2)))




if __name__ == "__main__":
    drv_obj = DrivingScholl()
    drv_obj.add_person()

