class PassEntry(object):


    def  __init__(self, site, username, password):
        self._site = site
        self._user = username
        self._pass = password

    def __str__(self):
        retrive = "Website: " + self._site + "\n"
        retrive += "Username: " + self._user + "\n"
        retrive += "Password: " + self._pass + "\n"

        return retrive
    def set_site(self, site):
        self._site = site

    def get_site(self):
        return self._site

    def set_user(self,user):
        self._user = user

    def get_user(self):
        return self._user

    def set_pass(self, password):
        self._pass = password

    def get_pass(self):
        return self._pass


class PassDB(object):
    def __init__(self):
        self._database = {}

    def add_entry(self, entry):
        self._database[entry._site] = entry

    def del_entry(self, site):
        self._database[site].pop()

    def get_(self, name):
        if name in self._database:
            return self._database[name]._pass
        else:
            return "Entry is not available."


