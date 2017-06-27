

class DateUtil():
    def get_weeks(self, new_date, old_date):
        weeks = new_date - old_date
        return weeks.days/7.0