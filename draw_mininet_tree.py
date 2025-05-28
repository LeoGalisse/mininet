import networkx as nx
import matplotlib.pyplot as plt

depth = 4
fanout = 3

G = nx.Graph()

def add_switches_and_hosts(parent, current_depth, sw_count, host_count):
    if current_depth < depth:
        for i in range(fanout):
            sw_count[0] += 1
            child_sw = f"s{sw_count[0]}"
            G.add_edge(parent, child_sw)
            add_switches_and_hosts(child_sw, current_depth + 1, sw_count, host_count)
    else:
        for i in range(fanout):
            host_count[0] += 1
            host = f"h{host_count[0]}"
            G.add_edge(parent, host)

sw_count = [1]
host_count = [0]
G.add_node("s1")
add_switches_and_hosts("s1", 1, sw_count, host_count)

plt.figure(figsize=(18, 9))
pos = nx.spring_layout(G, k=0.25)
switch_nodes = [n for n in G.nodes if n.startswith('s')]
host_nodes = [n for n in G.nodes if n.startswith('h')]

nx.draw_networkx_nodes(G, pos, nodelist=switch_nodes, node_shape='s', node_color='lightblue', label="Switches")
nx.draw_networkx_nodes(G, pos, nodelist=host_nodes, node_shape='o', node_color='lightgreen', label="Hosts")
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=8)
plt.axis('off')
plt.title("Mininet Topologia tree,depth=4,fanout=3")
plt.legend()
plt.tight_layout()
plt.show()
