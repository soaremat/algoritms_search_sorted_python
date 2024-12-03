import math

def jumpSerach(array, alvo, length):
    step = int(math.sqrt(length))
    ultimo_index = 0
    while array[int(min(step, length)-1)] < alvo:
        ultimo_index = step
        step += math.sqrt(length)
        if ultimo_index >= length:
            return -1
    
    while array[int(ultimo_index)]< alvo:
        ultimo_index += 1


        if ultimo_index == min(step, lenght):
            return -1
        
    if array[int(ultimo_index)] == alvo:
        return ultimo_index    
    
    return -1



array = [1,2,5,8,10,26,30,44,58,62,203]
alvo = 30
length = len(array)

index = jumpSerach(array, alvo, length)

print(f"Numero {alvo} está no index {int(index)}")