from datetime import datetime
from subsystem.database_interface import add_plan, add_report, add_crisis


class Asset:
    """Asset Data Object
    Data attributes structure:
        [...,
        (
            asset_id: int,
            name: str,
            availability: int
        ),
        ...]
    """

    def __init__(self, data):
        try:
            self.json = dict()
            for _ in data:
                assert type(_[1]) == str
                assert type(_[2]) == int
                self.json[_[0]] = {
                    "Name": _[1],
                    "Availability": _[2],
                }
        except AssertionError:
            print("Found an issue in the Database")
            raise TypeError("Wrong type for Asset attributes")


class Plan:
    """Plan Data Object
    Data attributes structure:
        [...,
        (
            plan_id: int,
            crisis_id: int
            details: str,
            timestamp: datetime.datetime
        ),
        ...]
    """

    def __init__(self, data):
        try:
            self.json = dict()
            for _ in data:
                assert type(_[2]) == str
                assert type(_[3]) == datetime
                self.json[_[0]] = {
                    "crisis_id": _[1],
                    "details": _[2],
                    "time": str(_[3]),
                }
        except AssertionError:
            print("Found an issue in the Database")
            raise TypeError("Wrong type for Plan Attributes")

    def addPlan(self, plan_id, plan_data):
        self.json[plan_id] = plan_data
        add_plan(plan_id, plan_data["crisis_id"], plan_data["details"],
                 plan_data["time"])


class Crisis:
    """Crisis Data Object
    Data attributes structure:
        [...,
        (
            crisis_id: int,
            type: str,
            details: str,
            timestamp: datetime.datetime
        )
        ...]
    """

    def __init__(self, data):
        try:
            self.json = dict()
            for _ in data:
                assert type(_[1]) == str
                assert type(_[2]) == str
                assert type(_[3]) == datetime
                self.json[_[0]] = {
                    "type": _[1],
                    "description": _[2],
                    "time": str(_[3]),
                }
        except AssertionError:
            print("Found an issue in the Database")
            raise TypeError("Wrong type for Plan Attributes")

    def addCrisis(self, crisis_id, crisis_data):
        self.json[crisis_id] = crisis_data
        add_crisis(crisis_id, crisis_data['crisis_type'],
                   crisis_data['description'], crisis_data['time'])


class Report:
    """Report Data Object
    Data attributes structure:
        [...,
        (
            report_id: int,
            crisis_id: int,
            summary: str,
            date: datetime.datetime
        ),
        ...]
    """

    def __init__(self, data):
        try:
            self.json = dict()
            for _ in data:
                assert type(_[2]) == str
                assert type(_[3]) == datetime
                self.json[_[0]] = {
                    "crisis_id": _[1],
                    "details": _[2],
                    "time": str(_[3]),
                }
        except AssertionError:
            print("Found an issue in the Database")
            raise TypeError("Wrong type for Report attributes")

    def addReport(self, report_data):
        add_report(report_data['crisis_id'], report_data['summary'],
                   report_data['time'])


class User():
    """User Instance Class
    """

    def __init__(self, username):
        self.username = username
        self.__is_admin = False
        self.__token = None
        self.__is_authenticated = False
        self.__is_active = False
        self.__is_anonymous = True

    def is_authenticated(self):
        return self.__is_authenticated

    def set_authenticated(self, value):
        self.__is_authenticated = value

    def is_active(self):
        return self.__is_active

    def set_active(self, value):
        self.__is_active = value

    def is_anonymous(self):
        return self.__is_anonymous

    def set_anonymous(self, value):
        self.__is_anonymous = value

    def is_admin(self):
        return self.__is_admin

    def set_admin(self, value):
        self.__is_admin = value

    def get_token(self):
        return self.__token

    def set_token(self, value):
        self.__token = value

    def get_id(self):
        return self.username
