import json
import requests
import datetime

class AutoFillGoogleForm(object):
    def __init__(self, cfg):
        # Get url to google form
        self.url = cfg["url"]
        assert requests.get(self.url).status_code == 200, "The url is invalid, please check."
        
        # Load data fields and their entry IDs
        self.form_fields = cfg["fields"]

    def get_date_time(self):
        date = datetime.date.today()
        self.form_fields["date_year"]["value"] = str(date.year)
        self.form_fields["date_month"]["value"] = str(date.month)
        self.form_fields["date_day"]["value"] = str(date.day)

        starttime = datetime.datetime.now().time()
        # Start time
        self.form_fields["start_time_hour"]["value"] = str(starttime.hour)
        self.form_fields["start_time_minute"]["value"] = str(starttime.minute)

        # End time
        endtime_hour = starttime.hour + 1
        endtime_minute = starttime.minute
        self.form_fields["end_time_hour"]["value"] = str(endtime_hour)
        self.form_fields["end_time_minute"]["value"] = str(endtime_minute)

    def compile_data(self):
        self.get_date_time()
        self.submission = {}
        for field in self.form_fields:
            entry_id = self.form_fields[field]["entry_id"]
            value = self.form_fields[field]["value"]
            self.submission[entry_id] = value

        print(self.submission)
        
    def post_data(self):
        self.compile_data()
        response = requests.post(self.url, self.submission)

        if response.status_code == 200:
            print("Success")
        else:
            print("Failed")


if __name__ == "__main__":
    with open("paddle_lodge_log_sheet.json", "r") as file:
        config = json.load(file)
    auto_form_filler = AutoFillGoogleForm(config)
    auto_form_filler.post_data()
    
