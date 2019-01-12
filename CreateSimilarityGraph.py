__author__ = 'Arwa Shaker'
""" creating a similarity graph between tasks
by creating a graph where its nodes are the tasks and 
the edges are weighted by the similarities from the
similarity matrix """


import networkx as nx
from CreateJaccardMatrix import create_jaccard_sim_matrix

def create_similarity_graph(jobs_profiles):
    """this function reates a similariy graph"""

    task_jaccard_sim_matrix = create_jaccard_sim_matrix(jobs_profiles)

    # creating the similarity graph from the similarity matrix

    indices= []
    for job in jobs_profiles:
        indices.append(job[0]) # using the jobs names as an index



    # beacuse the graph nodes can not be a list
    # it has to a hashble value

    Tasks_Graph = nx.Graph()
    for index in indices:
        Tasks_Graph.add_node(index)




    """print(Tasks_Graph.nodes())
    print(Tasks_Graph.number_of_edges())
    print(Tasks_Graph.number_of_nodes())"""


    i = 0
    for node in Tasks_Graph:
        j = 0
        for other_node in Tasks_Graph:
            #if task_jaccard_sim_matrix[i][j]>= 0.75:
            Tasks_Graph.add_edge(node,other_node,weight = task_jaccard_sim_matrix[i][j]) # add a wieted edge
            if j < 12  : j = j+1
        if i < 12  : i = i+1

    # drwaing -------------------------------------------------------------------------------
    try:
        import matplotlib.pyplot as plt
    except:
        raise

    elarge =[(u,v) for (u,v,d) in Tasks_Graph.edges(data=True) if d['weight'] >= 0.75] # threshold 0.75
    esmall =[(u,v) for (u,v,d) in Tasks_Graph.edges(data=True) if d['weight'] <0.75]

    pos=nx.spring_layout(Tasks_Graph) # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(Tasks_Graph,pos,node_size=300)

    # edges
    nx.draw_networkx_edges(Tasks_Graph,pos,edgelist=elarge,
                        width=3,edge_color='b')
    nx.draw_networkx_edges(Tasks_Graph,pos,edgelist=esmall,
                        width=1,alpha=0.5,edge_color='g',style='dashed')

    # labels
    nx.draw_networkx_labels(Tasks_Graph,pos,font_size=10,font_family='sans-serif')

    plt.axis('off')
    plt.savefig("task_weighted_similarity_graph.png") # save as png
  #  plt.show() # display

    return Tasks_Graph

