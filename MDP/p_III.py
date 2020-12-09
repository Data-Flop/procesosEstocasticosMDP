import numpy

def main():

    piscina = numpy.array([[1,  5 , 12, 10],
                         [40,  8 , 1 , 3 ],
                         [6,  13, 5 , 2 ],
                         [11, 4 , 14, 15]])
    print('profundidadPiscina', piscina, sep='\n')
    
    # Get the maximum value from complete 2D numpy array
    maxValue = numpy.amax(piscina)
    print('nivelMaximoDeProdundidad : ', maxValue)
    
    # Get the maximum values of each column i.e. along axis 0
    maxInColumns = numpy.amax(piscina, axis=0)
    print('maximoValorDeCadaColumna: ', maxInColumns)
    
    # Get the maximum values of each row i.e. along axis 1
    maxInRows = numpy.amax(piscina, axis=1)
    print('maximoValorDeCadaFila: ', maxInRows)
    print('*** profundidadMaximaDeLaPiscina ***')
    
    # Find index of maximum value from 2D numpy array
    result = numpy.where(piscina == numpy.amax(piscina))
    print('tuplaMaxima : ', result)
    print('coordenadasDelMaximoValorDeLaPiscina : ')
    
    # zip the 2 arrays to get the exact coordinates
 #   
 #   i = 1
#while i <= maxValue:
#    print(i)
#    i += 1
#print("Programa terminado")

   #         if maxValue=piscina[c][f]:
   #         result = numpy.where(piscina[c][f] == numpy.amax(piscina[c][f]))
   #         print('tuplaMaxima : ', result)
            

    #listOfCordinates = list(zip(result[0], result[1]))
    # travese over the list of cordinates
    #for cord in listOfCordinates:
    #    print(cord)
    #print('*** numpy.amax() & NaN ***')
    #arr = numpy.array([11, 12, 13, 14, 15], dtype=float)
    #arr[3] = numpy.NaN
    #print('Max element from Numpy Array : ', numpy.amax(arr))
if __name__ == '__main__':
    main()


piscina = numpy.array([[1,  5 , 12, 10],
                         [40,  8 , 1 , 3 ],
                         [6,  13, 5 , 2 ],
                         [11, 4 , 14, 15]])

maxValue = numpy.amax(piscina)
print('nivelMaximoDeProdundidad0000 : ', maxValue)

print (piscina)

#for c in range(len(piscina[0])):
#    for f in range(len(piscina)):
#        if piscina[c][f]=maxValue
#            print(piscina[c][f])




#print ("****")
#v=[[3, 5, 8], [4, 9, 11]]#
#
#for i in range(len(v[0])):
#    for j in range(len(v)):
#        print(v[j][i])


data = [[1,10], [2, 3], [4, 4]]
output = [element for each_list in data
                if len(each_list) == 2
                for element in each_list
                if element != 5]
print(output)
# Out: [2, 3, 4]