import datetime

class AutoFillGoogleForm(object):
    def __init__(self):
        self.data = {}

        def get_date_time(self):
            date = datetime.date.today()
            self.data['year'] = date.year
            self.data['month'] = date.month
            self.data['day'] = date.day

            time = datetime.datetime.now().time()
            self.data['hour'] = time.hour
            self.data['minute'] = time.minute

        def compile_data(self):
        
        def post_data(self):



if __name__ == "__main__":
    auto_form_filler = AutoFillGoogleForm()
    auto_form_filler.post_data()
    
