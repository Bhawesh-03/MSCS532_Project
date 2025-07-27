from graph import Graph
from metrics import UserMetrics
from heap import MaxHeap

def calculate_influence(graph):
    user_score = {}
    for user in graph.adj_list:
        score = 0
        for followers in graph.adj_list.values():
            if user in followers:
                score += 1
        user_score[user] = score
    return user_score

# Sample influencer connections
connections = [
    ("ElonMusk", "lexfridman"),
    ("lexfridman", "elonmusk"),
    ("BarackObama", "BillGates"),
    ("BillGates", "BarackObama"),
    ("elonmusk", "BarackObama"),
    ("taylorswift13", "selenagomez"),
    ("selenagomez", "taylorswift13"),
    ("Cristiano", "elonmusk"),
    ("Cristiano", "taylorswift13"),
    ("BillGates", "lexfridman"),
    ("elonmusk", "Cristiano"),
    ("IsolatedUser", "NoOne")  # edge case
]

# Build the graph
graph = Graph()
for from_user, to_user in connections:
    graph.add_connection(from_user, to_user)

# Calculate influence
metrics = UserMetrics()
heap = MaxHeap()
scores = calculate_influence(graph)

for user, score in scores.items():
    metrics.update_score(user, score)
    heap.insert(user, score)

# Output top 5 influencers
print("Top Influential Users:")
for score, user in heap.extract_top_k(5):
    print(f"{user}: {-score}")
