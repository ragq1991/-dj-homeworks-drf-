import datetime


# Если в прошлый раз я решил попрактиковаться,то в этот я не нашел что бы в пагинаторе можно было указать
# итерацию по датам и поэтому написал свой. Конвертор кстати тоже написал свой, но когда решил положить его на место
# обнаружил что зря писал...
class DatePaginator:
    def __init__(self, list_date, page_date):
        self.list_date = list_date
        self.page_date = self.get_real_date(page_date)

    def get_real_date(self, page_date):
        page_date = datetime.datetime.strptime(page_date, '%Y-%m-%d').date()
        if page_date not in self.list_date:
            space = 365 * 3000
            page_date_real = page_date
            for dt in self.list_date:
                if abs((page_date - dt).days) < space:
                    space = abs((page_date - dt).days)
                    page_date_real = dt
            return page_date_real
        else:
            return page_date

    def has_next(self):
        if self.list_date.index(self.page_date) < len(self.list_date) - 1:
            return True
        else:
            return False

    def has_previous(self):
        if self.list_date.index(self.page_date) > 0:
            return True
        else:
            return False

    def previous_page_number(self):
        idx = self.list_date.index(self.page_date) - 1
        return self.list_date[idx]

    def next_page_number(self):
        idx = self.list_date.index(self.page_date) + 1
        return self.list_date[idx]