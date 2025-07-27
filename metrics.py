class UserMetrics:
    def __init__(self):
        self.metrics = {}

    def update_score(self, user, score):
        self.metrics[user] = score

    def get_score(self, user):
        return self.metrics.get(user, 0)
