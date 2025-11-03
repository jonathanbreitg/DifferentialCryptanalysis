table_data2 = [
            [0,1,2,3,4,5,6,7,8,9,0xA,0xB,0xC,0xD,0xE,0xF],
            [0xE,4,0xD,1,2,0xF,0xB,8,3,0xA,6,0xC,5,9,0,7],
        ]
def s(n):
    return table_data2[1][n]

def s_inv(n):
    return table_data2[1].index(n)

#print(s(0xC))

K1 = 0xB #0xA

K2 = 0X7 #0x5

K3 = 0x2

def Net(x): #simple 3-layer SPN
    return s(s(x ^ K1) ^ K2) ^ K3

count = [0]*16 #count occurrences for each key
for key in range(16): #try all possible keys
    for x in range(16): #try all possible inputs
        y1 = Net(x)
        y2 = Net(x ^ 0xB) #input diff is 0xB
        if (s_inv(y1 ^ key) ^ s_inv(y2 ^ key)) == 0x2: #output diff before S-box is 0x2
            count[key] += 1      
    print(f"Key: {hex(key).upper()}, Count: {count[key]}")

'''max_count = max(count)
best_keys = [i for i, c in enumerate(count) if c == max_count]
print(f"Best Key(s): {[hex(k).upper() for k in best_keys]} with Count: {max_count}")

avg_cnt_excluding_best = sum(c for i, c in enumerate(count) if i not in best_keys) / (16 - len(best_keys))
print(f"Average Count Excluding Best Key(s): {avg_cnt_excluding_best}")'''