import requests
import datetime

class AutoFillGoogleForm(object):
    def __init__(self):
        # Actual URL
        self.url = "https://docs.google.com/forms/d/e/1FAIpQLSfMtt0kvol72F9A2BaLJacr8Xzm9n51KBxVfS8YkDe8SfS5GA/formResponse"
        
        # Test URL
        # self.url = "https://docs.google.com/forms/d/e/1FAIpQLSeZ42rcO3nr7-b-EMJvx_bsCp2b3_zNUj_NuRsEc2HafGXcWA/formResponse"
        
        # Actual data fields
        self.data = {
                # Name
                'entry.650249987': "Benjamin Ho",
                # Contact Number
                'entry.159891337': "98764968",
                # Affiliate/Organisation/School
                'entry.1965888248': "Individual Training",
                # Number of 1 Star
                'entry.1522705696': "1",
                # Number of Non-certified
                'entry.923232455': "0",
                # Location
                'entry.1917318237': "The Paddle Lodge @ MacRitchie Reservoir",
                # Disclaimer Agreement
                'entry.1234664796': "I read and agree to the disclaimer note"
            }

        # # Test data fields
        # self.data = {
        #         # Short Text Field
        #         'entry.1971069311': "1",
        #         # Multiple Choice Field
        #         'entry.1235339495': "Multiple Choice 1",
        #         # Checkbox Field
        #         'entry.1322518108': "Option 1"
        #     }

    def get_date_time(self):
        datetime = {}
        date = datetime.date.today()
        datetime['entry.2082654990_year'] = str(date.year)
        datetime['entry.2082654990_month'] = str(date.month)
        datetime['entry.2082654990_day'] = str(date.day)

        starttime = datetime.datetime.now().time()
        # Start time
        datetime['entry.76258493_hour'] = str(starttime.hour)
        datetime['entry.76258493_minute'] = str(starttime.minute)

        # End time
        endtime_hour = starttime.hour + 1
        endtime_minute = starttime.minute
        datetime['entry.1960199521_hour'] = str(endtime_hour)
        datetime['entry.1960199521_minute'] = str(endtime_minute)
        return datetime

    def compile_data(self):
        self.data.update(self.get_date_time())
        
    def post_data(self):
        self.compile_data
        for d in self.data:
            try:
                requests.post(self.url, self.data)
                print("Data submitted")
            except:
                print("Error filling in data")


if __name__ == "__main__":
    auto_form_filler = AutoFillGoogleForm()
    auto_form_filler.post_data()
    
