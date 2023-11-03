#TRANS rosalind
from Bio import SeqIO

s1 = ()
s2 = ()

for seq_record in SeqIO.parse(r"C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind\rosalind_tran.txt", "fasta"):
    if not s1:
        s1 = seq_record.seq
    else:
        s2 = seq_record.seq

transversions = {'A': ['C', 'T'], 'C': ['A', 'G'], 'G': ['T', 'C'], 'T': ['G', 'A']}
transitions = {'A': 'G', 'G': 'A', 'C': 'T', 'T': 'C'}

transitions_nr = 0
transversions_nr = 0


for i in range(len(s1)):
    if s1[i] != s2[i]:
        if s2[i] in transitions[s1[i]]:
            transitions_nr += 1
        elif s2[i] in transversions[s1[i]]:
            transversions_nr += 1

if transversions_nr!= 0:
    ratio = transitions_nr / transversions_nr
    print(ratio)