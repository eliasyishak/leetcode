"""
Helper to create graphs from an adjacency list
"""

import matplotlib.pyplot as plt
import networkx as nx

adj = {
    0: [2],
    1: [0],
    2: [0],
}

G = nx.DiGraph()  # type: ignore


for src, dests in adj.items():
    for dest in dests:
        G.add_edge(src, dest)  # type: ignore

nx.draw(G, with_labels=True, node_color="lightblue", arrows=True)  # type: ignore
plt.show()  # type: ignore
