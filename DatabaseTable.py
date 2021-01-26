class DatabaseTable:
    def __init__(self):
        self.id = 0
        self.created = ""
        self.modified = ""

    def set(self, id, created, modified):
        self.set_id(id)
        self.set_created(created)
        self.set_modified(modified)

    def get_id(self):
        return self.id

    def set_id(self, id):
        if id is not None:
            self.id = id

    def get_created(self):
        return self.created

    def set_created(self, created):
        if created is not None:
            self.created = created

    def get_modified(self):
        return self.modified

    def set_modified(self, modified):
        if modified is not None:
            self.modified = modified
