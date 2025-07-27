class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_user(self, user):
        if user not in self.adj_list:
            self.adj_list[user] = []

    def add_connection(self, from_user, to_user):
        self.add_user(from_user)
        self.add_user(to_user)
        self.adj_list[from_user].append(to_user)
