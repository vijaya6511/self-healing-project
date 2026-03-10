import json
from locator_utils import get_selector
from engine.healer import heal_locator
from utils.reporter import HealingReporter


class LoginPage:

    def __init__(self, page):
        self.page = page
        self.reporter = HealingReporter()

        # Load locators from JSON
        with open("textdata/inputdata.json") as f:
            data = json.load(f)["loginpage"]

        self.username = get_selector(data["username"]["by"], data["username"]["value"])
        self.password = get_selector(data["password"]["by"], data["password"]["value"])
        self.login_button = get_selector(data["login_button"]["by"], data["login_button"]["value"])

    # NEW FUNCTION: update JSON file
    def update_json_locator(self, element_name, new_value):
        file_path = "textdata/inputdata.json"

        with open(file_path, "r") as f:
            data = json.load(f)

        data["loginpage"][element_name]["value"] = new_value

        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

        print(f"[JSON UPDATED] {element_name} updated to {new_value}")

    def _perform_action(self, locator, element_name, action_type, value=None):

        try:
            print(f"[INFO] Trying original locator for {element_name}: {locator}")

            if action_type == "fill":
                self.page.fill(locator, value)
            elif action_type == "click":
                self.page.click(locator)

            print(f"[SUCCESS] Original locator worked for {element_name}")

            # REPORT PASS
            self.reporter.log(element_name, "PASS", locator)

            return locator

        except Exception as e:
            print(f"[ERROR] Original locator FAILED for {element_name}")
            print(f"Reason: {e}")
            print(f"[INFO] Healing locator for {element_name}...")

            try:
                # HEALING
                new_loc = heal_locator(
                    self.page,
                    {"by": "id", "value": locator.replace("#", "")},
                    action_type=action_type,
                    value=value
                )

                healed_locator = f"#{new_loc['value']}"
                score = new_loc.get("score", "N/A")

                print(f"[HEALED] New locator for {element_name}: {healed_locator}")

                # UPDATE SAME JSON FILE HERE
                self.update_json_locator(element_name, new_loc['value'])

                # retry with healed locator
                if action_type == "fill":
                    self.page.fill(healed_locator, value)
                elif action_type == "click":
                    self.page.click(healed_locator)

                print(f"[SUCCESS] Healed locator worked for {element_name}")

                # REPORT HEALED
                self.reporter.log(
                    element_name,
                    "HEALED",
                    locator,
                    healed_locator,
                    score
                )

                return healed_locator

            except Exception as e2:
                print(f"[FAIL] Healing also failed for {element_name}")
                print(f"Reason: {e2}")

                # REPORT FAIL
                self.reporter.log(element_name, "FAIL", locator)

                return locator

    def fill_username(self, user):
        self.username = self._perform_action(
            self.username,
            "username",
            action_type="fill",
            value=user
        )

    def fill_password(self, pwd):
        self.password = self._perform_action(
            self.password,
            "password",
            action_type="fill",
            value=pwd
        )

    def click_login(self):
        self.login_button = self._perform_action(
            self.login_button,
            "login_button",
            action_type="click"
        )

    def login(self, username, password):
        print("\n========== LOGIN TEST STARTED ==========\n")

        self.fill_username(username)
        self.fill_password(password)
        self.click_login()

        print("\n========== LOGIN TEST COMPLETED ==========\n")






# import json
# from locator_utils import get_selector
# from engine.healer import heal_locator
# from utils.reporter import HealingReporter


# class LoginPage:

#     def __init__(self, page):
#         self.page = page
#         self.reporter = HealingReporter()

#         # Load locators from JSON
#         with open("textdata/inputdata.json") as f:
#             data = json.load(f)["loginpage"]

#         self.username = get_selector(data["username"]["by"], data["username"]["value"])
#         self.password = get_selector(data["password"]["by"], data["password"]["value"])
#         self.login_button = get_selector(data["login_button"]["by"], data["login_button"]["value"])

 

#     def _perform_action(self, locator, element_name, action_type, value=None):

#         try:
#             print(f"[INFO] Trying original locator for {element_name}: {locator}")

#             if action_type == "fill":
#                 self.page.fill(locator, value)
#             elif action_type == "click":
#                 self.page.click(locator)

#             print(f"[SUCCESS] Original locator worked for {element_name}")

#             # REPORT PASS
#             self.reporter.log(element_name, "PASS", locator)

#             return locator

#         except Exception as e:
#             print(f"[ERROR] Original locator FAILED for {element_name}")
#             print(f"Reason: {e}")
#             print(f"[INFO] Healing locator for {element_name}...")

#             try:
#                 # HEALING
#                 new_loc = heal_locator(
#                     self.page,
#                     {"by": "id", "value": locator.replace("#", "")},
#                     action_type=action_type,
#                     value=value
#                 )

#                 healed_locator = f"#{new_loc['value']}"
#                 score = new_loc.get("score", "N/A")

#                 print(f"[HEALED] New locator for {element_name}: {healed_locator}")

#                 # retry with healed locator
#                 if action_type == "fill":
#                     self.page.fill(healed_locator, value)
#                 elif action_type == "click":
#                     self.page.click(healed_locator)

#                 print(f"[SUCCESS] Healed locator worked for {element_name}")

#                 # REPORT HEALED
#                 self.reporter.log(
#                     element_name,
#                     "HEALED",
#                     locator,
#                     healed_locator,
#                     score
#                 )

#                 return healed_locator

#             except Exception as e2:
#                 print(f"[FAIL] Healing also failed for {element_name}")
#                 print(f"Reason: {e2}")

#                 # REPORT FAIL
#                 self.reporter.log(element_name, "FAIL", locator)

#                 return locator


#     def fill_username(self, user):
#         self.username = self._perform_action(
#             self.username,
#             "username",
#             action_type="fill",
#             value=user
#         )

#     def fill_password(self, pwd):
#         self.password = self._perform_action(
#             self.password,
#             "password",
#             action_type="fill",
#             value=pwd
#         )

#     def click_login(self):
#         self.login_button = self._perform_action(
#             self.login_button,
#             "login_button",
#             action_type="click"
#         )

   

#     def login(self, username, password):
#         print("\n========== LOGIN TEST STARTED ==========\n")

#         self.fill_username(username)
#         self.fill_password(password)
#         self.click_login()

#         print("\n========== LOGIN TEST COMPLETED ==========\n")


