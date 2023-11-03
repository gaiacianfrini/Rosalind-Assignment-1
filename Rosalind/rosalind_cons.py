

from Bio import SeqIO, motifs


sequence=[]


for seq_record in SeqIO.parse(r"C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind\rosalind_cons (1).txt", "fasta"):
    sequence.append(seq_record.seq)
cons_seq= motifs.create(sequence)
matrix=cons_seq.counts

print(cons_seq.consensus)  

int_matrix = {}
for base, values in matrix.items():
    integer_values = [int(value) for value in values]
    int_matrix[base] = integer_values

for base, values in int_matrix.items():
    print(base + ":  " + " ".join(map(str, values)))


