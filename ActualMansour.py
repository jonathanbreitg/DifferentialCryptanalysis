table_data2 = [
            [0,1,2,3,4,5,6,7,8,9,0xA,0xB,0xC,0xD,0xE,0xF],
            [0xE,4,0xD,1,2,0xF,0xB,8,3,0xA,6,0xC,5,9,0,7],
        ]
def F(n):
    return table_data2[1][n]

def check(potential_v,delta_m,M_1,Z_1,Z_2,Z_3):
    potential_K_2 = F(potential_v) ^ Z_1 # try to recover K_2 by using first pair
    potential_K_1 = potential_v ^ M_1  # try to recover K_1 by using first pair
    if F(M_3 ^ potential_K_1) ^ potential_K_2 != Z_3: # check if keys also work for third pair
        return False
    if F(potential_v ^ delta_m) ^ potential_K_2  != Z_2: # check if keys also work for second pair
        return False
    else:
        return True

n=4 # key bit length

M_1 = 0b1101 # example message 1
M_2 = 0b0111 # example message 2
delta_m = M_1^M_2 # = 0b10101010 example input difference
M_3 = 0b0000 # example message 3

Z_1 =  0b0111 # example ciphertext for message 1
Z_2 =  0b1001 # example ciphertext for message 2
delta_w = delta_z = Z_1^Z_2 # = 0b11001000 example output difference
Z_3 = 0b0110 # example ciphertext for message 3

for potential_v in range(2**n): # generate all potential pairs
    if F(potential_v) ^ F(potential_v ^ delta_m) == delta_w: # pair is potentially valid
        if check(potential_v,delta_m,M_1,Z_1,Z_2,Z_3): # confirmed definitely valid pair
            K_1 = potential_v ^ M_1  # recover K_1
            K_2 = F(potential_v) ^ Z_1  # recover K_2
            print(f"Recovered keys: K_1 = {K_1:08b}, K_2 = {K_2:08b}")

"""print(F(M_1 ^ 1) ^ 2)
print(F(M_2 ^ 1) ^ 2)
print(F(M_3 ^ 1) ^ 2)"""