


f = open(r"C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\rosalind_iprb (1).txt", 'r')
ints = f.readline()
ints = ints.split(" ")
k = float(ints[0])
m = float(ints[1])
n = float(ints[2])
tot = k + m + n

k_first = k / tot
kk = k_first * (k-1)/(tot-1)
km = k_first * m/(tot-1)
kn = k_first * n/(tot-1)

m_first = m / tot
mk = m_first * k/(tot-1)
mm = m_first * (m-1)/(tot-1) * 0.75
mn = m_first * n/(tot-1) * 0.5

n_first = n / tot
nk = n_first * k/(tot-1)
nm = n_first * m/(tot-1) * 0.5
nn = n_first * (n-1)/(tot-1) * 0

result = kk + km + kn + mk + mm + mn + nk + nm + nn

print(result) 

 
