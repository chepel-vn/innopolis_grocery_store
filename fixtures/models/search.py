from faker import Faker

fake = Faker("en_US")


class SearchData:
    def __init__(self, search_string=None):
        self.search_string = search_string

    def random(self):
        s = fake.pystr()
        return SearchData(s)
