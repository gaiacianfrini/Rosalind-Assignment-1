#Rosalind DNA
sequence = 'CACTTGACCTGGTCGGCTGGACCGATGGGTCCCCATAGAAAGCTGATCCTAGCCAGCTGATTACAAGGTCATTCGTTGGTGTTACGTCGGGATACCAGATTCCGGCGTAGTATTAGGAGAGAAGTAGTTGAACATGTGCTGATTCTGATCGGCTCGGCTAATAAGATCTATTCCTACGGCGGCTTTGAGTCGCTCGATCGCTGACACGGCTAAGCTCGAAGGTCATGGCGCACCGGATATACTTCACAGGTAGGCCCTATCGAAGTCAACTTCTGCAAATACCTAGCCCATTCGTTGGGGGGACCTTCCAAGAACTCTCATCCATGTTAGTCACTAGCCACATTCAGGTCTGAGAAATGCCTTTCCCCACAAAATCCCTATAGCCAGGCGAGAAGATAACATCAACTGCTTCAAGGGACCAGGTGCCCGACCGGTTATGTCTGTCTTGGCAACCATCAGTGACCACGACGCAGGTACATGGGGATAATTCCGGGGCGGCATCGCGATATTCGTCATAGTAATCATTGGTGTGAGTGGCTAAGCTTTGAGACACGTAATATTTGAGGTGGAGGAGTGCAAAGTCCGCATCCACGAAGAAAACGTTGAAGGGTTTGGTTTTGCAAATGTATGTTCAGGGCTCACGTAAGGAATGATATGCGGTTACCTTGATCTATTAGTTCGACCGTTCATTTGTTTTTTCGTCTGGGCAATTCCGTTTGTTTCTGATGTGGATAGACAAAGTAGCTGCTGCGTGGTACTTCCACGATAGTCCACCTCCCAGCGCAGCATGTTCACGAGGCGTAGCAGGACAATTAGGAACGACGAAGGTATAGGAGTAATACACCTTGGTGGACTGCCTTGGTAAGGCTATACACTCATAGATCGTTTGTTAGTTTCGCCCTCTGTATCGGTCTATCCGCCAAAGGAACCACGCGCCGCCCGCGAATCCGCTCGGATCAACGTTGCTGGCGAGGCCGTAAAATGGTAACGGAT'

a = 0
c = 0
t = 0
g = 0

for base in sequence:
    if base == 'A':
            a += 1
    elif base == 'C':
            c +=1
    if base == 'T':
            t += 1
    elif base == 'G':
            g += 1

'print (str(a)+ ' ' + str(c) + ' ' + str(t) + ' ' +str(g))'


#Rosalind RNA

t = 'GGTCGGCTACAATCCAGTGTAGTGGTTGGTCGACCCGAGCACATAGTACTGAGTGTATGTTTCTAATTCTGCGTTACTTTAAAGAATCTCACTGCTGACTAATCAGTGTGTTCGCATCGGTGGCGGGCGTGAAGCCAAAGTAACCCTTTTTCTCGTAATCTCTGCAAACGTAAGTTTGTGTCAATGATCTTGTTCTCTAGGCTCCTAGGCAATAGAGAATTAGGGGCATATGCAGAGGTTCCCGACAACGTACTCTGTTGGTCTAATCAACAGGCAGATACGCATGATGCAGCCCAGCTCGCTCCTCTAGTACTCCGCTGCGGTGGCGCCTCAAGCACGGGCCACTACGTATAACGTGAGCCGCATGGGAAGGACACGCCTGACAGGTGTGACTTCCAATTCCCCTGCGTAGCCGCTACGGGGCAGTTCCTAGCCTTTGACCTACGTATTACAATTGGCCTTCCAGGCTCTCCCGGGACAAAAATCGGCTATCGAAGTGGTTATTTCCCCAATCGTGCGGAGGGACCGGACGACTGAATGCAACTACAGGTAAAATAATTGCGTAGGGACTACAAAGGGTGTTTCCTTTCCTGACTTACATATCTGTTACTTCCTCCGTCTGGTTGGCCGAGGATTTGCTGAGAGATAATGATCCGGAGGGTCCCGGAAATTGATGCGCCAAAGCACATTACATCGCCGATAGAGGTCTTCAGAATCGATGCGACTAGTCCCCATCAACTACGTAACTAGGATTAATATAGTTGGGAAGACCGGCCCTAGGAGGACAGGTGGGCGTACCATTGAACGTCCGGAAGGTTATACGGAAGTATCGTAGGTTCAATTCCCCTATCGTAAAGCTTAGTCGTTATATCTAATCATTATCTCCGGGATGTGATCAATTGTCAATCTACCCTGCGGTCTCGGAGGCAATATGC'
u = ''

for symbol in t: 
    if symbol == 'T':
        u += 'U'
    else:
        u += symbol
        
print(u)



#Rosalind REVC
sequence3 = 'CGGCAGGCCAAGCCCGCGCCCGCGAGCCCCCACAACCAAAAGGGATTACCGCCATAATCTTTCTCGGATCCACCTGCGGCTTTTCCCTTCTGATTCACCACAGAGCGACACGTGGGATATGTAAACGTTCTGTTTGATAGATCTAAGTAAAGCTTCCCAAGTAATCTAAGGTGTTACTTGTGTATTACATCAAACCGAGACCCAAAGGGCAGGTGTGATAACAGATCGGTGTCCTTGTTCTTTCAAAAAACGCAATCTTATACCCATTCCTTGCGGAAGATCGGTTTCGGTGCAACGTTGACGCAAGATTACTTAATCGTTCTAAGGGCGGTTCAGCAGAAGATCCCCCAACCCAAAGATCTCGCTAGGCAGGTAGGCATGCAAGCGACGCGAATAGCGGAACGGGCAACGTCGGAGGGTACAGGGAGTATACGGGGTGCTTGTTGTTTGGGGACGCGAGATTCGGACAGCATTACGATTTACCTGGACTGACGGGCCAGCCCCCGCGTAAGTATTGGCGCAACCCCAGGGTATCTACACGAGCTAGGCCTTTCTGACAGGTGTGAAACGTGTCTAGATAGAAGAAGCACTCGACCATTGCCACCCGTTACATCAGTACTTTTAATGTAGCTTAGAATGGCCGATTGGCGGTGTGGGGACGACCACTTCTCGCCTCGACCGATGTGTTAGCCGTGCAGGTTGTAGGATCGAACCAACTTCCCACTGTCTGAACTGATCTTGAAAGCTCCACTCCGCCTCGCTTAGGGTCGAAGAACACTGGAATCCCAACCATTGTAGCGGCCGGTGGCCTCGGACTCGCAAGTACCTTAAAACAATGAAGTGTGGTATCGGGTACGCCAAAAATATTCTAAAGCCTCCGGTCGTAATGAAGTTGAGTTTTCGAATCAATCGTCTCTTTATGTTATGCGGTTTTGTACTATTCTTCGAGGGCAGAGGCTGAGTAATGCCCCAGAACATACTCGCCCTCAA'
complementary_sequence = ' '

for symbol in sequence3:
        if symbol == 'A':
                complementary_sequence += 'T'
        elif symbol == 'C':
                complementary_sequence += 'G'
        elif symbol == 'G':
                complementary_sequence += 'C'
        elif symbol == 'T':
                complementary_sequence += 'A'

print('complementary sequences: ' + complementary_sequence + '\n')
print('reversed: ' + complementary_sequence[::-1])



#Rosalind GC
with open(r'C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\rosalind_gc.txt','r') as f:
    file_content = f.read()
    print(file_content)
    
file = open(r'C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\rosalind_gc.txt','r')
a = file.read()
file.close()