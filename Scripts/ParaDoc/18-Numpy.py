vector1 = range(7)
    vector2 = range(7,14)    
    vector1 = list(vector1)
    vector2 = list(vector2)
    vector3 = [9,6,1,3,7,4,9]
    # fn.detailVar(vector1)
    # fn.detailVar(vector2)

    m1 = np.array(vector2)
    print(m1)
    fn.detailVar(m1)
    print(m1.shape)

    #aceder a un vector o matriz por indice
    print(m1[0],m1[6],m1[2])

    m1[2]+=5

    print(m1[0],m1[6],m1[2])
    print("Matriz rango 2".center(50,'-'))
    m2 = np.array([vector1,vector2])
    print(m2.shape)
    print(m2)
    print("\n",m2[0,4],m2[1,6],m2[0,6])

    #creando matrices con funciones
    print("Matriz zeros".center(50,'-'))
    matriz0 = np.zeros((5,5))
    print(matriz0)
    print("Matriz ones".center(50,'-'))
    matriz1 = np.ones((5,5))
    print(matriz1)
    print("Matriz full".center(50,'-'))
    matrizf = np.full((5,5),7)
    print(matrizf)
    print("Matriz Identidad".center(50,'-'))
    matrizI = np.eye(7)
    print(matrizI)
    print("Matriz Random".center(50,'-'))
    matrizR = np.random.random((3,3))
    print(matrizR)

    #creando matrices con funciones
    print("Rebanadas Matriz".center(50,'-'))
    m3 = np.array([vector1,vector2,vector3])
    print(m3,m3.shape)
    #rebanada
    print("Rebanada".center(50,'-'))
    m4 = m3[:2,1:4]
    print(m4,m4.shape)
    #Actualizando valores en las rebanadas
    m4[1,2]=99
    print("Rebanada".center(50,'-'))
    print(m4,m4.shape)
    #Actualiza por defecto la matriz general
    print("Sin rebanar pero actualizada".center(50,'-'))
    print(m3,m3.shape)

    #otra indexacion
    print("Rebanadas Matriz".center(50,'-'))
    m5 = np.array([vector1,vector2,vector3])
    print(m5,m5.shape)
    print("Get row1".center(50,'-'))
    row1 = m5[1,:]
    print(row1,row1.shape)
    print("Get row2".center(50,'-'))
    row2 = m5[1:2,:]
    print(row2,row2.shape)
    #indexacion para columnas
    print("Get col1".center(50,'-'))
    col1 = m5[:,1]
    print(col1,col1.shape)
    print("Get col2".center(50,'-'))
    col2 = m5[:,1:2]
    print(col2,col2.shape)
    #indexacion por enteros por pos

    print("Index por enteros".center(50,'-'))
    print(m5,m5.shape)
    '''
    [   [ 0  1  2  3  4  5  6]
        [ 7  8  9 10 11 12 13]
        [ 9  6  1  3  7  4  9]  ] (3, 7)
    '''
    y=[0,1,2]
    x=[6,1,5]
    print(m5[y,x]) # es lo mismo q print(m5[[0,1,2],[6,1,5]])    
    #lo mismo en optra sintaxis
    print( [m5[0,6],m5[1,1],m5[2,5]] )
    #Otra indexacion similar
    print(m5[[0,0],[1,1]])
    #
    print([m5[0,0],m5[1,1]])
        
    print("Index por enteros y mutacion".center(50,'-'))
    a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
    print(a)
    '''
    [   [ 1  2  3]
        [ 4  5  6]
        [ 7  8  9]
        [10 11 12]  ]
    '''
    ar = np.arange(4)
    posColEdit = np.array([1,0,0,1])
    editColum = np.array([1,1,1,1])
    a[ar,editColum]+=10
    print(a)

    print("Index por enteros y mutacion".center(50,'-'))
    a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
    print(a)
    '''
    [   [ 1  2  3]
        [ 4  5  6]
        [ 7  8  9]
        [10 11 12]  ]
    '''
    bool_idx = (a>3)
    print(bool_idx)
    print(a[bool_idx])

    
    print("operaciones etre matrices".center(50,'-'))
    x = np.array([[1,2],[3,4]], dtype=np.float64)
    y = np.array([[5,6],[7,8]], dtype=np.float64)

    print(x)    
    print(y)    
    print("Suma".center(50,'-'))
    # np.add
    print(x+y)
    print("Resta".center(50,'-'))
    # np.subtract
    print(x-y)
    print("Multiplicacion".center(50,'-'))
    # np.multiply
    print(x*y)
    print("Division".center(50,'-'))
    # np.divide
    print(x/y)
    print("Raiz".center(50,'-'))
    print(np.sqrt(y))

    print("Suma total o por ejes".center(50,'-'))
    a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
    print(a)
    '''
    [   [ 1  2  3]
        [ 4  5  6]
        [ 7  8  9]
        [10 11 12]  ]
    '''
    print(np.sum(a))
    print(np.sum(a,axis=0))
    print(np.sum(a,axis=1))
    print("Trasnposicion".center(50,'-'))
    print(a.T)

    print("Broadcasting".center(50,'-'))
    print(a)
    v = np.array([1,0,1])
    vv = np.tile(v,(4,1))
    print(vv)
    y = a+vv
    print(y)
    

    # a = np.array([[1,2],[3,4],[5,6]])
    # print(a)
    # print(range(4))