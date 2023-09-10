import time
from faker import Faker
from config import *
from security import *
from unittest import TestCase
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import random

from selenium.webdriver.support import expected_conditions as EC
import string


# fake = Faker()


class LetCodeTest(TestCase):



    def test_pos_reg(self):
        driver = self.driver
        driver.get("http://99.153.249.66/")
        time.sleep(1)
        driver.find_elements(By.CLASS_NAME, "btn-outline-warning")[1].click()

        time.sleep(1)

        names_list = [
            "Eloise O'Reilly", "Leandre D'Amico", "Chloe D'Angelo", "Zoe O'Connell", "Celeste O'Malley",
            "Leo O'Leary", "Theodore D'Souza", "Anais O'Mara", "Ismael D'Costa", "Maelys O'Sullivan",
            "Noemie O'Malley", "Celine D'Arcy", "Nehemie O'Neal", "Cedric O'Dwyer", "Oceane D'Lorenzo",
            "Leonard D'Amore", "Zoe O'Brian", "Celia D'Agostino", "Matheo O'Callaghan", "Maelle O'Grady",
            "Theophile D'Angelo", "Lea O'Malley", "Raphael D'Costa", "Melodie O'Reilly", "Hugo D'Amico",
            "Lena O'Sullivan", "Nicolas O'Dwyer", "Leandro D'Souza", "Sarah O'Neal", "Baptiste O'Leary",
            "Ines D'Lorenzo", "Maxime D'Arcy", "Isabelle O'Mara", "Octave O'Connell", "Clara O'Brian",
            "Timeo O'Reilly", "Manon O'Leary", "Robin D'Amico", "Leo O'Neal", "Valentin O'Dwyer",
            "Margaux D'Costa", "Nathan O'Connell", "Oceane D'Souza", "Melina O'Malley", "Lucas O'Leary",
            "Roxane D'Arcy", "Gabriel O'Dwyer", "Emma D'Lorenzo", "Cedric O'Reilly", "Zoe O'Mara",
            "Leon D'Angelo", "Manon D'Amico", "Simon O'Sullivan", "Juliette D'Costa", "Ethan O'Connell",
            "Clemence O'Neal", "Maxence D'Souza", "Leane O'Reilly", "Antoine D'Amico", "Camille O'Dwyer",
            "Jules D'Lorenzo", "Raphael D'Souza", "Lena O'Malley", "Leo O'Reilly", "Margaux D'Arcy",
            "Theo O'Connell", "Emma O'Leary", "Alexandre D'Angelo", "Lena O'Mara", "Clement O'Dwyer",
            "Lucas D'Amico", "Manon D'Costa", "Hugo O'Connell", "Lou D'Souza", "Romain O'Neal",
            "Chloe D'Lorenzo", "Lea O'Dwyer", "Baptiste D'Angelo", "Oceane O'Reilly", "Raphael O'Connell",
            "Mathilde D'Amico", "Victor D'Souza", "Leonie D'Costa", "Noe O'Neal", "Maelle O'Leary",
            "Theo O'Dwyer", "Leon D'Lorenzo", "Juliette D'Angelo", "Jules O'Connell", "Lea O'Neal",
            "Maxime O'Dwyer", "Hugo D'Amore", "Lou D'Souza", "Manon D'Costa", "Leo O'Connell",
            "Celeste O'Neal", "Raphael D'Lorenzo", "Oceane D'Amico", "Lucas D'Arcy", "Chloe D'Souza"
        ]

        def generate_positive_email():  # random email for positive email
            letters_and_digits = string.ascii_letters + string.digits
            local_part_length = random.randint(1, 10)
            local_part = ''.join(random.choice(letters_and_digits) for _ in range(local_part_length))
            domain_part_length = random.randint(1, 10)
            domain_part = ''.join(random.choice(letters_and_digits) for _ in range(domain_part_length))
            tld = random.choice(["com", "net", "org"])

            return f"{local_part}@{domain_part}.{tld}"

        positive_emails = [generate_positive_email() for _ in range(100)]

        for email in positive_emails:
            print(email)

        for i in range(10):
            f_name = driver.find_element(By.ID, "id_first_name")
            l_name = driver.find_element(By.ID, "id_last_name")
            email = driver.find_element(By.ID, "id_email")
            password = driver.find_element(By.ID, "id_password1")
            conf_pass = driver.find_element(By.ID, "id_password2")
            register_button = driver.find_elements(By.CLASS_NAME, "waves-light")[-1]

            random_name = names_list[fake.random_int(0, len(names_list))]
            first_name, last_name = random_name.split(" ")
            random_email = positive_emails[fake.random_int(0, len(positive_emails))]

            f_name.send_keys(first_name)
            l_name.send_keys(last_name)
            fake_password = fake.password()
            password.send_keys(fake_password)
            conf_pass.send_keys(fake_password)
            email.send_keys(random_email)
            register_button.click()
            time.sleep(1)
            driver.find_elements(By.CLASS_NAME, "waves-light")[-2].click()
            time.sleep(2)

        time.sleep(2)

    def test_neg_reg(self):
        driver = self.driver
        driver.get("http://99.153.249.66/register/")
        time.sleep(1)
        driver.find_elements(By.CLASS_NAME, "btn-outline-warning")[1].click()

        time.sleep(1)

        names_list = [
            "Eloise O'Reilly", "Leandre D'Amico", "Chloe D'Angelo", "Zoe O'Connell", "Celeste O'Malley",
            "Leo O'Leary", "Theodore D'Souza", "Anais O'Mara", "Ismael D'Costa", "Maelys O'Sullivan",
            "Noemie O'Malley", "Celine D'Arcy", "Nehemie O'Neal", "Cedric O'Dwyer", "Oceane D'Lorenzo",
            "Leonard D'Amore", "Zoe O'Brian", "Celia D'Agostino", "Matheo O'Callaghan", "Maelle O'Grady",
            "Theophile D'Angelo", "Lea O'Malley", "Raphael D'Costa", "Melodie O'Reilly", "Hugo D'Amico",
            "Lena O'Sullivan", "Nicolas O'Dwyer", "Leandro D'Souza", "Sarah O'Neal", "Baptiste O'Leary",
            "Ines D'Lorenzo", "Maxime D'Arcy", "Isabelle O'Mara", "Octave O'Connell", "Clara O'Brian",
            "Timeo O'Reilly", "Manon O'Leary", "Robin D'Amico", "Leo O'Neal", "Valentin O'Dwyer",
            "Margaux D'Costa", "Nathan O'Connell", "Oceane D'Souza", "Melina O'Malley", "Lucas O'Leary",
            "Roxane D'Arcy", "Gabriel O'Dwyer", "Emma D'Lorenzo", "Cedric O'Reilly", "Zoe O'Mara",
            "Leon D'Angelo", "Manon D'Amico", "Simon O'Sullivan", "Juliette D'Costa", "Ethan O'Connell",
            "Clemence O'Neal", "Maxence D'Souza", "Leane O'Reilly", "Antoine D'Amico", "Camille O'Dwyer",
            "Jules D'Lorenzo", "Raphael D'Souza", "Lena O'Malley", "Leo O'Reilly", "Margaux D'Arcy",
            "Theo O'Connell", "Emma O'Leary", "Alexandre D'Angelo", "Lena O'Mara", "Clement O'Dwyer",
            "Lucas D'Amico", "Manon D'Costa", "Hugo O'Connell", "Lou D'Souza", "Romain O'Neal",
            "Chloe D'Lorenzo", "Lea O'Dwyer", "Baptiste D'Angelo", "Oceane O'Reilly", "Raphael O'Connell",
            "Mathilde D'Amico", "Victor D'Souza", "Leonie D'Costa", "Noe O'Neal", "Maelle O'Leary",
            "Theo O'Dwyer", "Leon D'Lorenzo", "Juliette D'Angelo", "Jules O'Connell", "Lea O'Neal",
            "Maxime O'Dwyer", "Hugo D'Amore", "Lou D'Souza", "Manon D'Costa", "Leo O'Connell",
            "Celeste O'Neal", "Raphael D'Lorenzo", "Oceane D'Amico", "Lucas D'Arcy", "Chloe D'Souza"]

        def generate_random_email():
            symbols = string.ascii_letters + string.digits + "!#$%&'*+-/=?^_`{|}~."
            local_part_length = random.randint(1, 20)
            local_part = ''.join(random.choice(symbols) for _ in range(local_part_length))
            domain_part_length = random.randint(1, 20)
            domain_part = ''.join(random.choice(symbols) for _ in range(domain_part_length))
            tld = random.choice(["com", "net", "org", "c", "comm", "_comm", "---", "..com", "...com"])

            return f"{local_part}@{domain_part}.{tld}"

        negative_emails = [generate_random_email() for _ in range(100)]

        for i in range(10):
            f_name = driver.find_element(By.ID, "id_first_name")
            l_name = driver.find_element(By.ID, "id_last_name")
            email = driver.find_element(By.ID, "id_email")
            password = driver.find_element(By.ID, "id_password1")
            conf_pass = driver.find_element(By.ID, "id_password2")
            register_button = driver.find_elements(By.CLASS_NAME, "waves-light")[-1]

            random_name = names_list[fake.random_int(0, len(names_list))]
            first_name, last_name = random_name.split(" ")
            random_email = negative_emails[fake.random_int(0, len(negative_emails))]

            f_name.send_keys(first_name)
            l_name.send_keys(last_name)
            fake_password = fake.password()
            password.send_keys(fake_password)
            conf_pass.send_keys(fake_password)
            email.send_keys(random_email)
            register_button.click()
            time.sleep(1)
            invalid_email = driver.find_elements(By.CLASS_NAME, "invalid-feedback")[2].text

            if invalid_email == "Enter a valid email address.":
                print("Negative test Pass with incorecct email:", random_email)
            else:
                print("Negative Email is Fail with invalid email:", random_email)

    def test_fill_form_fixture(self):
        driver = self.driver
        driver.get("http://99.153.249.66/register/")
        time.sleep(1)

        fixture_data = [
            {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "password": "P@ssw0rd!1"
            },
            {
                "first_name": "Jane",
                "last_name": "Smith",
                "email": "jane.smith@example.com",
                "password": "Uncommon#Pass2"
            },
            {
                "first_name": "Alex",
                "last_name": "Wilson",
                "email": "alex.wilson@example.com",
                "password": "SecurePwd$3"
            },
            {
                "first_name": "Emily",
                "last_name": "Brown",
                "email": "emily.brown@example.com",
                "password": "MyP@ssw0rd4"
            },
            {
                "first_name": "Daniel",
                "last_name": "Johnson",
                "email": "daniel.johnson@example.com",
                "password": "12345!Pass"
            },
            {
                "first_name": "Olivia",
                "last_name": "Martinez",
                "email": "olivia.martinez@example.com",
                "password": "Qwerty123$"
            },
            {
                "first_name": "Liam",
                "last_name": "Davis",
                "email": "liam.davis@example.com",
                "password": "Pa$$w0rd678"
            },
            {
                "first_name": "Sophia",
                "last_name": "Miller",
                "email": "sophia.miller@example.com",
                "password": "SecurePwd#9"
            },
            {
                "first_name": "Noah",
                "last_name": "Garcia",
                "email": "noah.garcia@example.com",
                "password": "Uncommon@Pass10"
            },
            {
                "first_name": "Ava",
                "last_name": "Rodriguez",
                "email": "ava.rodriguez@example.com",
                "password": "P@ssw0rd!11"
            },
            # Add more items as needed...
        ]
        for item in fixture_data:
            driver.get("http://99.153.249.66/register/")
            time.sleep(1)
            f_name = driver.find_element(By.ID, "id_first_name")
            l_name = driver.find_element(By.ID, "id_last_name")
            email = driver.find_element(By.ID, "id_email")
            password = driver.find_element(By.ID, "id_password1")
            conf_pass = driver.find_element(By.ID, "id_password2")
            register_button = driver.find_elements(By.CLASS_NAME, "waves-light")[-1]

            f_name.send_keys(item["first_name"])
            l_name.send_keys(item["last_name"])
            password.send_keys(item["password"])
            conf_pass.send_keys(item["password"])
            email.send_keys(item["email"])
            register_button.click()
            # Accessing the data from the fixture
        # for item in fixture_data:
        #     print("First Name:", item["first_name"])
        #     print("Last Name:", item["last_name"])
        #     print("Email:", item["email"])
        #     print("Password:", item["password"])
        #     print("-----------------------")

        time.sleep(1)

    def test_neg_names(self):
        driver = self.driver
        driver.get("http://99.153.249.66/register/")
        time.sleep(1)

        def generate_negative_name(length=8):
            symbols = '!@#$%^&*()_-+=<>?'
            numbers = '0123456789'
            letters = string.ascii_letters
            characters = letters + symbols + numbers
            negative_name = ''.join(random.choice(characters) for _ in range(length))
            return negative_name

        for i in range(20):
            neg_first = driver.find_element(By.ID, "id_first_name")
            neg_last = driver.find_element(By.ID, "id_last_name")

            generated_name = generate_negative_name()

            neg_first.send_keys(generated_name)
            neg_last.send_keys(generated_name)
            driver.find_elements(By.CLASS_NAME, "waves-light")[-1].click()
            time.sleep(1)

            invalid_first = driver.find_elements(By.CLASS_NAME, "invalid-feedback")[0].text

            invalid_last = driver.find_elements(By.CLASS_NAME, "invalid-feedback")[1].text

            expected_error_message1 = "Only English alphabet letters, spaces, single dots, single dashes, and single " \
                                      "apostrophes are allowed."
            if invalid_first == expected_error_message1:
                print("Negative test Pass with incorrect first name:", generated_name)
            else:
                print("Negative test Fail with invalid first name:", generated_name)
            expected_error_message2 = "This field is required."
            if invalid_last == expected_error_message1:
                print("Negative test Pass with incorrect first name:", generated_name)
            else:
                print("Negative test Fail with invalid first name:", generated_name)
            driver.get("http://99.153.249.66/register/")
            time.sleep(1)

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
