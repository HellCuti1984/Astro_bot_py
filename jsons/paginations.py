import os.path

from jsons import jsons
from keyboards.inline import pagination


class Pagination:

    def __init__(self, content, limit_on_page, last_page):
        # ИНИЦИАЛИЗАЦИЯ ФАЙЛА ПАГИНАЦИИ
        self.path_to_pagination_file = jsons.FILES['path_to_pagination_file']

        if os.path.exists(self.path_to_pagination_file) is False:
            self.cur_page = 1
            self.last_page = 1

            pagination = {
                'cur_page': self.cur_page,
                'last_page': self.last_page
            }

            jsons.write_to_file(pagination, self.path_to_pagination_file)

    def get_pagi_row(self, markup):
        pagination.pagination_row(markup, self.cur_page, self.last_page)
        return markup

    def update_pagi_file(self, pagi):
        jsons.write_to_file(pagi, self.path_to_pagination_file)
