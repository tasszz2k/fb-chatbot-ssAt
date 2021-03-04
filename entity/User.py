class User:
    id = 0
    name = ''
    first_name = ''
    last_name = ''
    profile_pic = ''
    locale = ''
    timezone = 7
    gender = ''

    def __init__(self, id, name, first_name, last_name, profile_pic, locale, timezone, gender):
        self.id = id
        self.name = name
        self.first_name = first_name
        self.last_name = last_name
        self.profile_pic = profile_pic
        self.locale = locale
        self.timezone = timezone
        self.gender = gender


