def interpolationsearch( array, element):
    menor = 0
    maior = len(array) - 1

    while menor <= maior:
        interpolation = menor + (((maior - menor)* (element-array[menor]))//(array[maior]-array[menor]))
        if interpolation >= menor and interpolation <= maior:
            if array[interpolation] == element:
                return f'Elemento encontrado no index {interpolation}.'
            elif array[interpolation] > element:
                maior = interpolation -1    
            elif array[interpolation] < element:
                menor = interpolation + 1
        else:
            return 'Elemento não encontrado!'
        return 'Elemento não encotrado!'  

array = [10,15,54,77,88,90,101]  
print(interpolationsearch(array,88))    