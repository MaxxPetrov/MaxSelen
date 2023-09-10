import time

from maxselen import *
from config import *
from security import *


class DrivingScholl(Maxselen):
    def __init__(self):
        super().__init__()

    def login_admin(self):
        self.Web.get(URL)
        self.Web.find_element(NAME, "username").send_keys(USER)
        self.Web.find_element(NAME, "password").send_keys(PASSWORD)
        self.Web.find_element(CLASS, "submit-row").find_element(TAG, "input").click()
        time.sleep(2)

    def add_person(self):
        self.login()
        self.Web.find_element(CLASS, "model-person").find_element(CLASS, "addlink").click()
        time.sleep(2)

        self.type_to_xpath(l_name, fake.last_name())
        self.type_to_xpath(f_name, fake.first_name())
        self.type_to_xpath(mid_name, fake.first_name())
        self.type_to_xpath(birthday, fake.date_of_birth(minimum_age=10, maximum_age=130).strftime("%Y-%m-%d"))
        self.type_to_xpath(street, fake.street_address())
        self.type_to_xpath(unit, fake.random_number(digits=3))
        self.type_to_xpath(city, fake.city())
        self.type_to_xpath(zipcode, fake.postcode())
        self.type_to_xpath(idNumber, fake.random_number(digits=8))
        self.type_to_xpath(idIssued, fake.past_date().strftime("%Y-%m-%d"))
        self.type_to_xpath(idExp, fake.future_date().strftime("%Y-%m-%d"))
        self.type_to_xpath(emergContact, fake.name())

        self.select_id("id_sex", str(random.randint(0, 2)))
        # self.select_name("state", str(random.randint(7, 15)))
        # self.select_id("id_ID_state", str(random.randint(0, 2)))
        self.Web.find_element(NAME, "_save").click()
        time.sleep(1)

    def add_persons(self, count):
        for i in range(count):
            self.add_person()


    def state_fill(self):
        self.login_admin()
        # self.Web(CLASS, "model-state current-model") # не могу найти класс в классе
        self.click_to_xpath("//a[contains(text(),'States')]")
        time.sleep(1)
        self.click_to_xpath('//a[contains(.,"Add state")]')
        for PN, state_item in states_info.items():
            self.type_to_xpath(postal, PN)
            self.type_to_xpath(state, state_item[0])
            print(state_item[1])
            time.sleep(1)
            self.select_id("id_time_zone", state_item[1])
            time.sleep(2)
            self.click_to_name("_addanother")
            time.sleep(2)



if __name__ == "__main__":
    obj = DrivingScholl()
    # obj.add_person()
    obj.state_fill()
