class Homework:

    def __init__(self, due_date):
        self.done = False
        self.did_expire = False
        self.due_date = due_date

    def turn_in(self):
        self.done = True

    def is_done(self):
        return self.done

    def update(self, current_date):
        self.did_expire = self.due_date < current_date

    def is_missing(self):
        return (not self.done) and self.did_expire

    def is_late(self):
        return self.done and self.did_expire
