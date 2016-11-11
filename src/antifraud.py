import csv
import networkx as nx


"""
Creating a graph using the batch file (training data)
"""
G = nx.Graph()
with open('paymo_input/batch_payment.txt', 'rU') as csvfile:
    # ignore the first line (as it contains the header)
    csvfile.readline()

    # loop over the file to add nodes and edges to our graph
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        graph_nodes = row[1:3]
        if len(graph_nodes) > 0:
            for node in graph_nodes:
                if node not in G:
                    G.add_node(node)
            node1 = graph_nodes[0]
            if len(graph_nodes) > 1:
                node2 = graph_nodes[1]
                if not G.has_edge(node1, node2):
                    G.add_edge(node1, node2)


"""
Implementing features 1, 2 and 3 and writing the results
"""

with open('paymo_input/stream_payment.txt', 'rU') as csvfile:
    # ignore the first line (as it contains the header)
    csvfile.readline()

    reader = csv.reader(csvfile, delimiter=',')
    # opening the three files we are writing to
    file1 = open('paymo_output/output1.txt', 'w')
    file2 = open('paymo_output/output2.txt', 'w')
    file3 = open('paymo_output/output3.txt', 'w')

    # loop over the stream file to evaluate, and then add that edge to graph
    for row in reader:
        graph_nodes = row[1:3]
        for node in graph_nodes:
            if node not in G:
                G.add_node(node)

        if len(graph_nodes) > 0:
            node1 = graph_nodes[0]
            if len(graph_nodes) > 1:
                node2 = graph_nodes[1]

                # creating this try except block because if two nodes don't
                # lie in the same connected component, we wouldn't find a
                # path between them - hence an unverified transaction.

                # FEATURE 1 (direct neighbors)
                try:
                    if len(nx.shortest_path(G, node1, node2)) <= 2:
                        file1.write('trusted\n')
                    else:
                        file1.write('unverified\n')
                except:
                    file1.write('unverified\n')

                # FEATURE 2 (within 2nd degree network)
                try:
                    if len(nx.shortest_path(G, node1, node2)) <= 3:
                        file2.write('trusted\n')
                    else:
                        file2.write('unverified\n')
                except:
                    file2.write('unverified\n')

                # FEATURE 3 (within 4th degree network)
                try:
                    if len(nx.shortest_path(G, node1, node2)) <= 5:
                        file3.write('trusted\n')
                    else:
                        file3.write('unverified\n')
                except:
                    file3.write('unverified\n')

                # Adding this information to augment our graph
                if not G.has_edge(node1, node2):
                    G.add_edge(node1, node2)

# Closing all the files, so as to not keep them in the buffer.
csvfile.close()
file1.close()
file2.close()
file3.close()
