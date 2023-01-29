# Binary Tree in Python

class Node:
    def __init__(self, key): #
        self.left = None     # este es el proceso que me permite
        self.right = None    # realizar los nodos 
        self.val = key       #

    
    def traversePreOrder(self):             #
        print(self.val, end=' ')            #
        if self.left:                       # este apartado me permite ordenar  
            self.left.traversePreOrder()    # los caracteres ingresados proximamente
        if self.right:                      # para que sean en preorden
            self.right.traversePreOrder()   #

    
    def traverseInOrder(self):              #
        if self.left:                       #
            self.left.traverseInOrder()     # este apartado me permite ordenar
        print(self.val, end=' ')            # los caracteres ingresados proximamente
        if self.right:                      # para que sean en inorden
            self.right.traverseInOrder()    #

   
    def traversePostOrder(self):            #
        if self.left:                       # este apartado me permite ordenar los caracteres
            self.left.traversePostOrder()   # ingresados proximamente 
        if self.right:                      # para que sean en posorden
            self.right.traversePostOrder()  #
        print(self.val, end=' ')            #

###########################################
root = Node("S")                          #
                                          #
root.left = Node("A")                     #
root.left.right = Node("Q")               #  
root.left.left = Node("C")                #
root.left.left.right = Node("I")          #
root.left.left.right.left = Node("T")     # 
root.left.left.right.right = Node("P")    #   EN ESTE APARTADO SE INGRESAN LOS DATOS EN CADA NODO INGRESADO MANUALMENTE
root.left.left.left = Node("F")           #                    PARA QUE EL SISTEMA RECONOSCA EL NODO
root.left.left.left.left = Node("H")      #   SE DEVE PONER TAL Y COMO SE VE "UNA RAMA ISQUIERDA SE PONE COMO LEFT Y DERECHA RIGHT"
                                          #   SI LA RAMA ISQUIERDA TIENE UN HIJO O UNA CONTINUACION POR LA DERECHA SE EXPRESA COMO 
root.right = Node("W")                    #                                 EJEMPLO
root.right.left = Node("M")               #                           ROOT.LEFT.RIGHT = NODE("Q")
root.right.left.left = Node("N")          #   LA "S" YA FUE DETERMINADA COMO PUNTO DE INICIO POR LO CUAL LA RAMA ISQUIERDA QUE SIGE ES "A" Y AL LADO DERECHO DE A 
root.right.right = Node("Y")              #   VIENE "Q" EL CUAL SERIA LA LETRA CORRESPONDIENTE A ESE NODO.
root.right.right.left = Node("Z")         #   
root.right.right.left.left = Node("X")    # 
root.right.right.right = Node("R")        #
root.right.right.right.right = Node("L")  #
###########################################
print("=============================================================================")
print()
print()
print("              UNIVERSIDAD TECNICA DE COTOPAXI                                      ")
print()
print(" NOMBRE ALUMNO: JOSTIN MAISINCHO")
print(" FECHA: 20/07/2021")
print(" TEMA: PROGRAMA ARBOL BIANRIO    ")
print(" Nota: los resultados dentro de las opciones del menu")
print(" estan basadas en el grafico propuesto en el apartado del deber")
print(" Por lo que solo representa los resultados de dicho grafico segun la opcion")
print()                                   
print()
print("=============================================================================")

menu=int(input("MENU ARBOL BINARIO:  \n 1- Solucion Inorden \n 2- Solucion Preorden \n 3- Solucion Postorden \n 0- SALIR \n Ingrese Opcion: "))

while menu!=0:
    if menu==1:
        print("=====================================================================")
        print("\nINORDEN: ", end="")
        root.traverseInOrder()
        print("\n")
        print("\n=====================================================================")       
    if menu==2:
        print("=====================================================================")
        print("PREORDEN: ", end="")
        root.traversePreOrder()
        print("\n")
        print("\n=====================================================================")
    if menu==3:
        print("=====================================================================")
        print("\nPOSORDEN: ", end="")
        root.traversePostOrder()
        print("\n")
        print("\n=====================================================================")    
   
    menu=int(input("INGRESE NUEVAMENTE UNA OPCION:  \n 1- Solucion Inorden \n 2- Solucion Preorden \n 3- Solucion Postorden \n 0- SALIR \n Ingrese una opcion: "))    






#sadsadasdasdsad saddsa 


#jostin





