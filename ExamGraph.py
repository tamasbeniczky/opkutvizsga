def ExamGraph(task):

    import matplotlib.pyplot as plt
    import networkx as nx
    import random as rd
    import pandas as pd

    def NeptunDraw(G, pos, lpos):
        plt.clf()
        nx.draw_networkx(G, pos, with_labels = True)
        nx.draw_networkx_edges(G, pos,edgelist=G.edges(data=True), width=2)
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels, label_pos = lpos)
    
    if task == "1":
        gep_ind = ['G1','G2','G3','G4']
        termek_ind = ['T1','T2','T3','T4']
        gepek = 4
        termekek = 4
        A=[[0]*gepek]*termekek
        for i in range(termekek):
            a = [0]*gepek
            for j in range(gepek):
                a[j] = rd.randint(7,29)
            A[i] = a
        
        print("\n1. Egy vállalatnak van 4 gépe, melyekkel 4 különböző terméket tud gyártani.")
        print("Mindegyik gép minden termék gyártására alkalmas, de a beállítás miatt gépenként csak 1 adott termékre.")
        print("A gyártás során egy gép egy termékből előállít bizonyos mennyiséget, mely termék értékesítéséből a vállalat bevételre tesz szert.")
        print("Az alábbi táblázat mutatja, hogy az egyes gépek az egyes termékek esetén mekkora mennyiséget tudnak előállítani.")
        print('\n', pd.DataFrame(A,index=termek_ind,columns=gep_ind))
        print("\na) Határozzunk meg egy gyártási tervet, mely maximalizálja az előállított termékek mennyiségét! Mennyi össz. terméket állít elő a vállalat, és melyik gép melyik termék gyártását végzi?")
        
        ar = []
        for i in range(termekek):
            ar.append(rd.randint(4,11))
            
        print("\nb) A termékek értékesítési árai az alábbiak:",ar)
        print("Hogyan változik a megoldás, ha a vállalat már a maximális árbevétel szerint osztja be a gépeket a termékek előállítására?")
        
        uj_gep = []
        for i in range(termekek):
            uj_gep.append(rd.randint(13,31))
            
        rnd = rd.uniform(0,1)
        rnd2 = rd.randint(1,4)
        if rnd > 0.5:
            print("\nc) Tegyük fel, hogy a vállalatnak van lehetősége egy 5. gépet is beszerezni, mely a 4 termékből az alábbi mennyiségeket állítja elő:",uj_gep)
            print("Legfeljebb mennyit hajlandó a cég az 5. gép megvásárlására áldozni (a b) pontban megadott árak mellett), és miért?")
        else:
            print("\nc) Tegyük fel, hogy a vállalat a "+str(rnd2)+". gépet 2 termék gyártására is tudja egyidejűleg használni.")
            print("Hogyan változik ekkor a b) pontban megkapott megoldás?")
        return
    elif task == "2":
        print("\n2. Négy frissen végzett orvostanhallgató jelentkezik a rezidens gyakornoki programba, ahol négy kórházban keresnek 1-1 gyakornokot.")
        print("A hallgatók rendelkeznek preferenciákkal a kórházi helyek között.")
        print("(1-es a leginkább, 4-es a legkevésbé preferált)\n")
        x1 = list(range(1,5))
        rd.shuffle(x1)
        x2 = list(range(1,5))
        rd.shuffle(x2)
        x3 = list(range(1,5))
        rd.shuffle(x3)
        x4 = list(range(1,5))
        rd.shuffle(x4)
        df = pd.DataFrame([x1, x2, x3, x4])
        df2 = df.transpose()
        df2.columns=['1. hallgató', '2. hallgató', '3. hallgató', '4. hallgató']
        df2.index=['1. kórház', '2. kórház', '3. kórház', '4. kórház']
        df2 = df2.rename_axis('Hallgató preferenciák', axis=1)
        print(df2)
        print("\nHasonlóan a kórházak is rendelkeznek preferenciákkal az egyes hallgatók között.")
        print("(1-es a leginkább, 4-es a legkevésbé preferált)\n")
        y1 = list(range(1,5))
        rd.shuffle(y1)
        y2 = list(range(1,5))
        rd.shuffle(y2)
        y3 = list(range(1,5))
        rd.shuffle(y3)
        y4 = list(range(1,5))
        rd.shuffle(y4)
        df = pd.DataFrame([y1, y2, y3, y4])
        df.columns=['1. hallgató', '2. hallgató', '3. hallgató', '4. hallgató']
        df.index=['1. kórház', '2. kórház', '3. kórház', '4. kórház']
        df = df.rename_axis('Kórház preferenciák', axis=1)
        print(df)
        
        rnd=rd.uniform(0,1)
        
        if rnd<0.5:
            print("\na) Adjon meg egy hallgató-optimális stabil párosítást!")
            print("\nb) Tegyük fel, hogy a kórházak véletlenül fordítva adták meg a preferenciáikat, azaz a 4-es a leginkább, az 1-es a legkevésbé preferált hallgató (a hallgatók preferenciái változatlanul helyesek). Ekkor mi lenne egy kórház-optimális stabil párosítás?")
        else:
            print("\na) Adjon meg egy kórház-optimális stabil párosítást!")
            print("\nb) Tegyük fel, hogy a hallgatók véletlenül fordítva adták meg a preferenciáikat, azaz a 4-es a leginkább, az 1-es a legkevésbé preferált kórház (a kórházak preferenciái változatlanul helyesek). Ekkor mi lenne egy hallgató-optimális stabil párosítás?")
        return
    elif task == "3":
        print("\n3/1. Színezzük ki a Last FM Asia gráf éleit. Ha egy él mindkét csúcsának azonosító száma kisebb mint 4000, akkor legyen az él színe 'magenta', ellenkező esetben legyen a színe 'navy'.")
        print("\n3/2. Mekkorának kell válasszuk egy 110 csúcsú Erdős-Rényi gráf 'p' paraméterét, hogy várhatóan ugyanannyi csúcsunk legyen, mint egy (n=110, m=6) paraméterekkel rendelkező Barabási-Albert gráfnak?")
        print("\n3/3. Teszteljük szimulációval, hogy egy (n=200,m=4) paraméterezéső Barabási-Albert és egy (megközelítőleg) azonos csúcs- és élszámú Erdős-Rényi hálózatok esetén melyik gráftípusban nagyobb a rövidutak átlagos hossza.")
        print("\n3/4. Irányítsuk meg a korvett gráf éleit mindkét irányba és számoljuk ki a csúcsok pagerank értékeit 0.85-ös párologtatási paraméter mellett egy LP segítségével!")
        print("\n3/5. Szimuláció segítségével vizsgáljuk meg, hogy a top 10 pagerank csúcs (alpha=0.8) melyik gráftípusban ér el több csúcsot a független kaszkád terjedési mechanizmuson keresztül, az (n=120,m=8) paraméterezésű Barabási-Albert gráf, vagy az (n=120,p=0.1254) paraméterezésű Erdős-Rényi gráf?")
        return
    elif task == "4":
        nep=input("Kérem adja meg a NEPTUN kódját, majd üssön ENTER-t!")
        nep_seed=1
        for i in nep:
            j=str(i).upper()
            nep_seed=nep_seed*ord(str(j)) % 2687 #Prime number as modulus
    

        rd.seed(nep_seed)

        diff=67
        
        G=nx.Graph()
        e=[(1,2),(3,1),(7,3),(11,7),(12,11),(10,12),(6,10),(2,6), (1,4),(9,12),(3,4),(4,5),(5,6),(7,8),(8,9),(9,10),(5,9),(4,8)]
        G.add_edges_from(e, weight=0)

        
        rnd=rd.uniform(0,1)
        if rnd<=0.5:
            G.add_edge(2,4, weight=0)
        else:
            G.add_edge(2,5, weight=0)
        
        rnd=rd.uniform(0,1)
        if rnd<=0.5:
            G.add_edge(7,4, weight=0)
        else:
            G.add_edge(3,8, weight=0)
            
        rnd=rd.uniform(0,1)
        if rnd<=0.5:
            G.add_edge(5,10, weight=0)
        else:
            G.add_edge(9,6, weight=0)   
            
        rnd=rd.uniform(0,1)
        if rnd<=0.5:
            G.add_edge(8,11, weight=0)
        else:
            G.add_edge(9,11, weight=0)     
        
        t=[]
        for i in range(diff,len(G.edges)+diff):
            t.append(i)
        rd.shuffle(t)
        
        itr=0
        for i,j in G.edges:
            G[i][j]['weight']=t[itr]
            itr+=1
        
        pos={}
        pos[1]=(1,4)
        pos[2]=(2,4)
        pos[3]=(0,3)
        pos[4]=(1,3)
        pos[5]=(2,3)
        pos[6]=(3,3)
        pos[7]=(0,2)
        pos[8]=(1,2)
        pos[9]=(2,2)
        pos[10]=(3,2)
        pos[11]=(1,1)
        pos[12]=(2,1)
        
        
        print("4.a) Számítsa ki a H gráf minimális súlyú feszítő fáját! Mekkora a fa összköltsége és milyen élek alkotják?\nb) Irányítsa meg a gráf éleit a legnagyobb sorszámú csúcstól a legkisebb sorszámú csúcsba! Tegyük fel, hogy az élsúlyok az éleken való áthaladás idejét jelképezik. Írjon fel egy LP feladatot, amely kiszámolja a legrövidebb utat a 12-es csúcsból az 1-es csúcsba. Mennyi idő alatt lehet átjutni? Milyen éleken halad keresztül a legrövidebb út?\nc) Színezze kékre ('blue') azokat az éleket, amelyek a 12-es csúcsból indított szélességi keresés első 9 éléhez tartoznak, pirosra ('red') azokat, amelyek a legrövidebb úton vannak rajta és magentával ('magenta'), amelyek mindkettőn megtalálhatóak, a többi él maradjon fekete. Ábrázolja a gráfot!")

        
        
        NeptunDraw(G, pos, lpos = 0.5)

        return pos, G