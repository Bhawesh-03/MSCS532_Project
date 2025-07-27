# Social Network Analysis: Identifying Influential Users

This project implements a simplified social network analysis tool to identify influential users using Python. The core functionality focuses on representing user connections as a directed graph, calculating in-degree influence scores, and extracting the top-K influential users using a max heap.

## 🔍 Project Objective

To build a foundational system capable of modeling social network interactions and identifying influential users (e.g., in a Twitter-like network) using core data structures.

## 🧱 Implemented Data Structures

- **Graph (Adjacency List):** Models the user relationships (who follows whom).
- **Hash Table (UserMetrics):** Stores and retrieves influence scores efficiently.
- **Max Heap (Priority Queue):** Helps retrieve the top-K influential users.

## 📂 Project Structure

```
├── graph.py         # Defines the Graph class
├── metrics.py       # Defines the UserMetrics class
├── heap.py          # Defines the MaxHeap class
├── main.py          # Driver script to build graph, calculate influence, and print top influencers
```

## 📊 Demonstration Output

```
Top Influential Users:
BarackObama: 2
elonmusk: 2
taylorswift13: 2
lexfridman: 2
BillGates: 1
```

## 🔬 Test Cases

- Real-world inspired influencer data
- Circular and mutual connections (e.g., Elon Musk ↔ Lex Fridman)
- Edge case with isolated user

## 🚀 How to Run

Make sure all `.py` files are in the same folder. Then run:

```bash
python main.py
```

## 📈 Future Enhancements

- Incorporate engagement metrics (likes, shares)
- Live data from Twitter API
- Sentiment-weighted influence scores
- Graph visualizations using NetworkX
- Web dashboard using Flask/Streamlit

## 📚 References

1. Aral, S., & Walker, D. (2012). *Science*, 337(6092), 337–341. https://doi.org/10.1126/science.1215842  
2. Tang, J. et al. (2016). *SIAM Data Mining Conference*. https://doi.org/10.1137/1.9781611974348.7  
3. Kwak, H. et al. (2010). *WWW Conference*. https://doi.org/10.1145/1772690.1772751

---

© 2025 Bhawesh Shrestha | University of the Cumberlands
