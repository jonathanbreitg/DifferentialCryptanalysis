from ActualMansour import *
plaintexts = []
ciphertexts = []
N=2**((n/2))
delta_ws = {} # hashmap for output XOR's
for i in range(2*N,step=2): # i=0,2,4,6,...2N-2
    delta_ws[ciphertexts[i] ^ ciphertexts[i+1]] = i #set key of hashmap to be the output xor and the value the index

for potential_v in range(2**n): # generate all potential pairs
    potential_delta_w = F(potential_v) ^ F(potential_v ^ delta_m)
    if potential_delta_w in delta_ws: # pair is potentially valid
        if check(potential_v,delta_m,plaintexts,ciphertexts,delta_ws[potential_delta_w]): # confirmed definitely valid pair
            index = delta_ws[potential_delta_w]
            K_1 = potential_v ^ plaintexts[index]  # type: ignore # recover K_1
            K_2 = F(potential_v) ^ ciphertexts[index]  # type: ignore # recover K_2
            #print(f"Recovered keys: K_1 = {K_1:08b}, K_2 = {K_2:08b}")