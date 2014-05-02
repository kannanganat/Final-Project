#!/usr/bin/env python
import matplotlib
matplotlib.use('SVG')
from intermine.webservice import Service
from matplotlib import pyplot as plt
import random
# Please note: the descriptions of each function is given in the documentation file that is submitted.

def generate_graph():

    service = Service("http://yeastmine.yeastgenome.org/yeastmine/service")
    
    # Get a new query on the class (table) you will be querying:
    query = service.new_query("Gene")
    
    # Type constraints should come early - before all mentions of the paths they constrain
    query.add_constraint("goAnnotation.ontologyTerm", "GOTerm")
    
    # The view specifies the output columns
    query.add_view(
        "secondaryIdentifier", "symbol", "goAnnotation.ontologyTerm.identifier",
        "description", "chromosome.primaryIdentifier", "chromosomeLocation.start",
        "chromosomeLocation.end", "chromosome.length"
    )
    
    # This query's custom sort order is specified below:
    query.add_sort_order("Gene.symbol", "ASC")

    # You can edit the constraint values below
    query.add_constraint("goAnnotation.qualifier", "IS NULL", code = "C")
    query.add_constraint("goAnnotation.qualifier", "!=", "NOT", code = "B")
    query.add_constraint("goAnnotation.ontologyTerm.name", "=", "cytoplasmic translation", code = "A")
    query.add_constraint("name", "ONE OF", ["Ribosomal Protein of the Large subunit", "Ribosomal Protein of the Small subunit"], code = "D")

    # Your custom constraint logic is specified with the code below:
    query.set_logic("A and (B or C) and D")


    chromosome={}
    for row in query.rows(): # has all the data
        if row["chromosome.primaryIdentifier"] not in chromosome.keys():
            chromosome[row["chromosome.primaryIdentifier"]] = {"length":row["chromosome.length"],"genes":[]}
            
        chromosome[row["chromosome.primaryIdentifier"]]["genes"].append({'symbol':row["symbol"],'start': row["chromosomeLocation.start"], 'end':row["chromosomeLocation.end"]})
    

    all_chr_ids = chromosome.keys()
    all_chr_length = []
    for chr in all_chr_ids:
        all_chr_length.append( chromosome[chr]['length'] )
    fig = plt.figure()
    fig.set_size_inches(25,10)
    y_pos = range(len(all_chr_ids))
    plt.barh(y_pos, all_chr_length, align='center', alpha=0.4)  #draws the horizontal bar graph from every element in 'y-pos'(y-axis) to 'all_chr_length'(x-axis)
    plt.yticks(y_pos,all_chr_ids ) #Says position and label for y-axes

    plt.xlabel('Gene Positions') #sets label for x-axes
    plt.title('Ribosomal protein Genes in Yeast Genome')

    chromosome_y_axis = 0
    for chr in all_chr_ids:
        for gene in chromosome[chr]['genes']:
            posn = (gene['start']+gene['end'])/2
            plt.plot(posn,chromosome_y_axis,'ro')
            plt.annotate(gene['symbol'],(posn-2,chromosome_y_axis+0.1),rotation='vertical')
        chromosome_y_axis+= 1    
        
    fig.savefig('static/rp_positions.svg')
