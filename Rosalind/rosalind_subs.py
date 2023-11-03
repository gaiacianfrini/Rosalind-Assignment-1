#subs
s = 'ATTGGATCGGTCCCGGCAATCGGTCATCGGTCGTGAATCGGTCATCCAAGCTCATCGGTCTATCGGTCTAAAGATCGGTCAATATCGGTCATCGGTCCCATCGGTCTCCAACCATCGGTCATCGGTCACGGATCGGTCAATCGGTCAGCCTGATCGGTCATCGGTCAATGAGGATCGGTCCATCGGTCAATCGGTCCTGCGCGATCGGTCCTGCATCGGTCATCGGTCATCGGTCCATCGGTCGATCGGTCGCATCGGTCTATGCTCATCGGTCCCACCCATCGGTCAATCGGTCGATCGGTCAAATCGGTCATCGGTCATCGGTCCTCTGAATCGGTCATAATCGGTCATCGGTCATCGGTCATCGGTCGGCGCATCGGTCATCGGTCTATCACATCGGTCTGACGCGTCTATCGGTCATCGGTCATCGGTCATCGGTCTGGGCAATCGGTCAATCGGTCATCGGTCATCGGTCGATCGGTCATCGGTCCATCGGTCTCAAAGTCATCGGTCATCGGTCAATCGGTCAATCGGTCCATCGGTCTTGAAGGTAGGCACTCCACCCATCGGTCTCATCGGTCACATCGGTCATCGGTCGCCGATCGGTCATCGGTCATCGGTCCTCCAATCGGTCCTAATCGGTCGACTCGCTCTATCGGTCATCGGTCAGAACATCGGTCTCATCGGTCCCAATCGGTCATCGGTCATCGGTCATCGGTCCCCGAAATCGGTCCCCCGGGATCGGTCGTATCGGTCGGGCATCGGTCCGATCGGTCATCGGTCCGAAATCGGTCATCGGTCGTCAATCGGTCATCGGTCCGGCCTATATCGGTCTGAGTTGACGGTTGGAATCGGTCCATCGGTCATCGGTCATCGGTCGCATCGGTCGATCGGTCAGGATCGGTCATCGGTCCTATCGGTCATCGGTCTGATCGGTCCTAATCGGTCATCGGTCGGACAGGGGATCGGTCATACATCGGTC'
t = 'ATCGGTCAT'

location = []
for i in range(len(s) - len(t) + 1):
    if s[i:i+len(t)] == t:
        location.append(i+1)
        
for i in location:
    print(i)





