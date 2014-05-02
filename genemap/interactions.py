#!/usr/bin/env python
import matplotlib
matplotlib.use('SVG')
import networkx as nx
from matplotlib import pyplot as plt
from intermine.webservice import Service
# Please note: the descriptions of each function is given in the documentation file that is submitted.
def getInteractions():
    service = Service("http://yeastmine.yeastgenome.org/yeastmine/service")

    # Get a new query on the class (table) you will be querying:
    query = service.new_query("Gene")

    # Type constraints should come early - before all mentions of the paths they constrain
    query.add_constraint("goAnnotation.ontologyTerm", "GOTerm")

    # The view specifies the output columns
    query.add_view(
        "symbol", "interactions.details.experimentType",
        "interactions.gene2.symbol", "interactions.gene2.briefDescription"
    )

    # You can edit the constraint values below
    query.add_constraint("goAnnotation.qualifier", "IS NULL", code = "C")
    query.add_constraint("goAnnotation.qualifier", "!=", "NOT", code = "B")
    query.add_constraint("goAnnotation.ontologyTerm.name", "=", "cytoplasmic translation", code = "A")
    query.add_constraint("name", "ONE OF", ["Ribosomal Protein of the Large subunit", "Ribosomal Protein of the Small subunit"], code = "D")
    query.add_constraint("interactions.details.annotationType", "=", "manually curated", code = "E")

    # Your custom constraint logic is specified with the code below:
    query.set_logic("A and (B or C) and E and D")

    
    interactions = {}
    
    for row in query.rows():
        if row["symbol"] not in interactions.keys():
            interactions[row["symbol"]] = [{ "expt" : row["interactions.details.experimentType"], "gene2": row["interactions.gene2.symbol"],"desc":row["interactions.gene2.briefDescription"]}]
        else:
            interactions[row["symbol"]].append({ "expt": row["interactions.details.experimentType"], "gene2": row["interactions.gene2.symbol"],"desc":row["interactions.gene2.briefDescription"]})
    return interactions

def get_interaction(interactions,gene):
    G=nx.Graph()
    fig = plt.figure()
    fig.set_size_inches(25,10)
    labels = {}
    edge_labels = {}
    labels[gene]=""
    colors = []
    for v in interactions[gene]:
        G.add_edge(gene,v["gene2"])
        labels[v["gene2"]] = v["desc"]
        edge_labels[(gene,v["gene2"])] = v["expt"]
            
    layout= nx.spring_layout(G,iterations=100)
    layout1 = dict((n,(d[0,],d[1,]+0.08)) for n,d in layout.items())
    
    for n in G.nodes():
        if n == gene:
            colors.append('c')
        else:
            colors.append('r')
        
    nx.draw(G,layout,node_size=2500,node_color=colors,edge_color='b',style='dashed')
    nx.draw_networkx_labels(G,layout1,labels=labels,font_color='g')
    nx.draw_networkx_edge_labels(G,layout,edge_labels=edge_labels,font_color='y',font_size=14)
    fig.savefig('static/rp_interactions.svg')
    
    

