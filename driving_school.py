from maxselen import Maxselen


class DrivingScholl(Maxselen):
    def __init__(self):           #, wd="Chrome"):
        super().__init__()


if __name__ == "__main__":
    drv_obj = DrivingScholl()
    drv_obj.WebDriver.get("https://google.com")
    print("test 3")
