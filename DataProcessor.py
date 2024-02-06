
def innerProduct(v1, v2):
    dotProduct = 0.0
    if(len(v1) != len(v2)):
        print("VECTORS ARE NOT IN THE SAME DIMENSION SUBSPACE")
    else:
        for i in range(len(v1)):
            dotProduct = dotProduct+(v1[i]*v2[i])
    return dotProduct

def normOf(v):
    norm = 0.0
    for i in range(len(v)):
        norm += v[i]**2
    norm = norm**0.5
    return norm

def multiplyScalarToVector(s, v):
    ret = v
    for i in range(len(v)):
        ret[i] = v[i]*s
    return ret

ljData = [2.96,1.28]
shirtData = [5.71,1.49]
playerName = 'aidan'
printData(ljData,playerName)

dotProd = innerProduct(ljData, shirtData)
normSquared = normOf(shirtData)**2
projectedVector = multiplyScalarToVector((dotProd/normSquared),shirtData)
print("DOT PRODUCT: ",dotProd)
print("NORM SQUARED: ",normSquared)
print(projectedVector)

