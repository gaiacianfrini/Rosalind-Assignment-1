#Rosalind GC
#apro il file, lo leggo, tolgo gli spazi e lo inserisco in una lista
with open(r'C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\rosalind_gc (1).txt','r') as f:
    lines = [line.strip() for line in f.readlines()]   
    
    
    #lista vuota per memorizzare i dati e organizzarli al suo interno.
    #L'obiettivo di questo blocco è quello di raggruppare tutti i dati al
    #loro interno dividendoli per rosalind e dna string
    result = []
    # Inizializza le variabili chiave e valore iniziali
    current_key = None
    current_value = []
    # Itera sulle linee e costruisci la lista di liste
    for line in lines:
        if line.startswith(">Rosalind"):
            if current_key is not None:
                result.append([current_key, ''.join(current_value)])
            current_key = line
            current_value = []
        else:
            current_value.append(line)
    # Aggiungi l'ultimo set di dati alla lista
    if current_key is not None:
        result.append([current_key, ''.join(current_value)])
    
    
    
    #calcolo percentuale per ogni singolo elemento in lista [[rosalind, dna string], [rosalind_2, dna string]....]
    for data_pair in result: 
        g_count = data_pair[1].count('G')
        c_count = data_pair[1].count('C')
        # Calculate the total length of the sequence
        total_length = len(data_pair[1])
        # Calculate the percentage of G and C content
        gc_percentage = ((g_count + c_count) / total_length) * 100
        data_pair.append(gc_percentage)

    #cerco il massimo della gc_percentage e l'id di riferimento per quel gc_percentage in cui è contenuto  
    highest_gc_id = ''
    highest_gc = 0.00
    for data_pair in result:
        #print(data_pair[0])
        if data_pair[2] > highest_gc:
            highest_gc_id = data_pair[0]
            highest_gc = data_pair[2]


    print(highest_gc_id)
    print(highest_gc) 
    
    
    
    '''
    #lunghezza della lista
    n = len(result)
    
    for i in result:
        min = i
        for j in range(i+1, n):
            if result[j][1]<result[min][-1]:
                min=j
        result[i], result[min] = result[min], result[i]
    
    print(result)
    '''

