# -*- coding: utf-8 -*-
"""
  Name     : c10_22_binomial_graph.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import networkx as nx
import matplotlib.pyplot as plt 
#
plt.figtext(0.08,0.6,"Stock price=$20") 
plt.figtext(0.75,0.91,"Stock price=$22") 
plt.figtext(0.75,0.87,"Option price=$1")
plt.figtext(0.75,0.28,"Stock price=$18") 
plt.figtext(0.75,0.24,"Option price=0") 
n=1
def binomial_grid(n): 
    G=nx.Graph()
    for i in range(0,n+1):
        for j in range(1,i+2): 
            if i<n:
                G.add_edge((i,j),(i+1,j))
                G.add_edge((i,j),(i+1,j+1))
    posG={}
    for node in G.nodes(): 
        posG[node]=(node[0],n+2+node[0]-2*node[1])
    nx.draw(G,pos=posG) 
binomial_grid(n)
plt.show()
