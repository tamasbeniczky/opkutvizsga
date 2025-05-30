def SampleGraph(graphtype):
    nep_seed=2
    
    
    import matplotlib.pyplot as plt
    import networkx as nx
    import random as rd
    
    def NeptunDraw(G, pos):
        plt.clf()
        nx.draw_networkx(G, pos, with_labels = True)
        nx.draw_networkx_edges(G, pos,edgelist=G.edges(data=True), width=2)
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels)

    
    rd.seed(nep_seed)
    
    diff=10 #difficulty, weight size starts from this value
    
    if graphtype == "cpm" or graphtype =="shp":
        G=nx.DiGraph()
        v = ["s","a","b","c","d","e","f","g","h","i","t"]
        G.add_nodes_from(v)
        e=[("s","a"),("s","b"),("s","c"),("a","d"),("b","e"),("c","f")]
        f=[("d","g"),("e","h"),("f","i"),("g","t"),("h","t"),("i","t")]
        G.add_edges_from(e, weight=0)
        G.add_edges_from(f, weight=0)
        
        rnd=rd.uniform(0,1)
        if rnd<=0.5:
            G.add_edge("a","e", weight=0)
        else:
            G.add_edge("b","d", weight=0)
        
        rnd=rd.uniform(0,1)
        if rnd<=0.5:
            if graphtype == "shp":
                G.add_edge("d","h", weight=0)
            elif graphtype == "cpm":
                G.add_edge("h","d", weight=0)
        else:
            if graphtype == "shp":
                G.add_edge("e","g", weight=0)
            elif graphtype == "cpm":
                G.add_edge("g","e", weight=0)
            
        rnd=rd.uniform(0,1)
        if rnd<=0.5:
            G.add_edge("b","f", weight=0)
        else:
            G.add_edge("c","e", weight=0)   
            
        rnd=rd.uniform(0,1)
        if rnd<=0.5:
            if graphtype == "shp":
                G.add_edge("e","i", weight=0)
            elif graphtype == "cpm":
                G.add_edge("i","e", weight=0)
        else:
            if graphtype == "shp":
                G.add_edge("f","h", weight=0)
            elif graphtype == "cpm":
                G.add_edge("h","f", weight=0)
        
        t=[]
        for i in range(diff,len(G.edges)+diff):
            t.append(i)
        rd.shuffle(t)
        
        itr=0
        for i,j in G.edges:
            G[i][j]['weight']=t[itr]
            itr+=1
            
        #pos = nx.planar_layout(G)
        pos={}
        pos["s"]=(0,1)
        pos["a"]=(1,2)
        pos["b"]=(1,1)
        pos["c"]=(1,0)
        pos["d"]=(2,2)
        pos["e"]=(2,1)
        pos["f"]=(2,0)
        pos["g"]=(3,2)
        pos["h"]=(3,1)
        pos["i"]=(3,0)
        pos["t"]=(4,1)
        
        NeptunDraw(G, pos)
        
    elif graphtype == "mcst":
        G=nx.Graph()
        v = ["a","b","c","d","e","f","g","h","i","j","k","l"]
        G.add_nodes_from(v)
        e=[("a","b"),("c","a"),("g","c"),("k","g"),("l","k"),("j","l"),("f","j"),("b","f")]
        f=[("a","d"),("i","l"),("c","d"),("d","e"),("e","f"),("g","h"),("h","i"),("i","j")]
        G.add_edges_from(e, weight=0)
        G.add_edges_from(f, weight=0)
        
        rnd=rd.uniform(0,1)
        if rnd<=0.5:
            G.add_edge("b","d", weight=0)
        else:
            G.add_edge("b","e", weight=0)
        
        rnd=rd.uniform(0,1)
        if rnd<=0.5:
            G.add_edge("d","h", weight=0)
        else:
            G.add_edge("e","h", weight=0)
            
        rnd=rd.uniform(0,1)
        if rnd<=0.5:
            G.add_edge("e","i", weight=0)
        else:
            G.add_edge("e","j", weight=0)   
            
        rnd=rd.uniform(0,1)
        if rnd<=0.5:
            G.add_edge("h","k", weight=0)
        else:
            G.add_edge("i","k", weight=0)     
        
        t=[]
        for i in range(diff,len(G.edges)+diff):
            t.append(i)
        rd.shuffle(t)
        
        itr=0
        for i,j in G.edges:
            G[i][j]['weight']=t[itr]
            itr+=1
        
        #pos = nx.planar_layout(G)
        pos={}
        pos["a"]=(1,4)
        pos["b"]=(2,4)
        pos["c"]=(0,3)
        pos["d"]=(1,3)
        pos["e"]=(2,3)
        pos["f"]=(3,3)
        pos["g"]=(0,2)
        pos["h"]=(1,2)
        pos["i"]=(2,2)
        pos["j"]=(3,2)
        pos["k"]=(1,1)
        pos["l"]=(2,1)
        
        NeptunDraw(G, pos)
        
    elif graphtype == "maxflow":
        G=nx.DiGraph()
        v = ["s","a","b","c","d","e","f","g","h","i","t"]
        G.add_nodes_from(v)
        e=[("s","a"),("s","b"),("s","c"),("a","d"),("b","e"),("c","f")]
        f=[("d","g"),("e","h"),("f","i"),("g","t"),("h","t"),("i","t")]
        G.add_edges_from(e, weight=0)
        G.add_edges_from(f, weight=0)
        
        rnd=rd.uniform(0,1)
        if rnd<=0.5:
            G.add_edge("a","b", weight=0)
            G.add_edge("b","c", weight=0)
        else:
            G.add_edge("b","a", weight=0)
            G.add_edge("c","b", weight=0)
        
        rnd=rd.uniform(0,1)
        if rnd<=0.5:
            G.add_edge("d","e", weight=0)
            G.add_edge("e","f", weight=0)
        else:
            G.add_edge("e","d", weight=0)
            G.add_edge("f","e", weight=0)
            
        rnd=rd.uniform(0,1)
        if rnd<=0.5:
            G.add_edge("d","h", weight=0)
            G.add_edge("h","g", weight=0)
        else:
            G.add_edge("e","g", weight=0)
            G.add_edge("g","h", weight=0)  
            
        rnd=rd.uniform(0,1)
        if rnd<=0.5:
            G.add_edge("f","h", weight=0)
            G.add_edge("h","i", weight=0)
        else:
            G.add_edge("e","i", weight=0)
            G.add_edge("i","h", weight=0)     
        
        t=[]
        for i in range(diff,len(G.edges)+diff):
            t.append(i)
        rd.shuffle(t)
        
        itr=0
        for i,j in G.edges:
            if i in ["b","e","h"] or j in ["b","e","h"]:
                if (t[itr] % 2) == 0:
                    G[i][j]['weight']=int(t[itr]/2)+1
                else:
                    G[i][j]['weight']=int((t[itr]+1)/2)
            else:
                G[i][j]['weight']=t[itr]
            itr+=1
        
        #pos = nx.planar_layout(G)
        pos={}
        pos["s"]=(0,1)
        pos["a"]=(1,2)
        pos["b"]=(1,1)
        pos["c"]=(1,0)
        pos["d"]=(2,2)
        pos["e"]=(2,1)
        pos["f"]=(2,0)
        pos["g"]=(3,2)
        pos["h"]=(3,1)
        pos["i"]=(3,0)
        pos["t"]=(4,1)
        
        NeptunDraw(G, pos)
        
    else:
        print("Invalid argument")
        return
    
    return G