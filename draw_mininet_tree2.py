import networkx as nx
import matplotlib.pyplot as plt

# Criação do grafo
G = nx.Graph()

# Adicionando switches
switches = ['s1', 's2', 's3', 's4']
G.add_nodes_from(switches)

# Adicionando hosts
hosts = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
G.add_nodes_from(hosts)

# Conectando switches conforme a imagem
edges = [
    ('s1', 's2'),
    ('s1', 's3'),
    ('s2', 's4'),
    ('s3', 's4'),
    # Conexões hosts-switches
    ('h1', 's1'),
    ('h2', 's1'),
    ('h3', 's2'),
    ('h4', 's3'),
    ('h5', 's4'),
    ('h6', 's4')
]
G.add_edges_from(edges)

# Layout manual para ficar igual à imagem
pos = {
    's1': (0, 2),
    's2': (-2, 1),
    's3': (2, 1),
    's4': (0, 0),
    'h1': (-0.7, 2.7),
    'h2': (0.7, 2.7),
    'h3': (-2.7, 0.5),
    'h4': (2.7, 0.5),
    'h5': (-0.7, -0.7),
    'h6': (0.7, -0.7),
}

# Desenhar
plt.figure(figsize=(8, 5))
nx.draw_networkx_nodes(G, pos, nodelist=switches, node_shape='s', node_color='skyblue', node_size=1000, label='Switches')
nx.draw_networkx_nodes(G, pos, nodelist=hosts, node_shape='o', node_color='lightgreen', node_size=700, label='Hosts')
nx.draw_networkx_edges(G, pos, width=2)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
plt.axis('off')
plt.title("Topologia Customizada Mininet")
plt.legend(["Switches", "Hosts"])
plt.tight_layout()
plt.show()
