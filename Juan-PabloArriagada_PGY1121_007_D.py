#https://github.com/JuanPabloArriagada/ExamenPGY1211
from os import system
system("cls")

ubicaciones=[]
for i in range(1,101):
    ubicaciones.append(i)
asistentes=[]
entradas=[]
ganancias=platinum=gold=silver=0

def pausa():
    print('Oprima "Enter" para seguir... ')
    input()
    system("cls")



def comprar(rut:int,ubicacion:int):
    if ubicaciones[int(ubicacion)-1]!="X":
        ubicaciones[int(ubicacion)-1]="X"
        assistente=[rut,ubicacion]
        asistentes.append(assistente)
        return True
    else:
        return False
    
def ubicacionesdisponibles():
    cant=0
    for i in range(100):
        print(ubicaciones[i], end="\t")
        cant+=1
        if cant%10==0:
            print()
        
    



while True:
    cant=1
    print("""

        1. Comprar entradas
        2. Mostrar ubicaciones disponibles
        3. Ver listado de asistentes
        4. Mostrar ganancias totales

        5. "Salir"
    """)
    op=input("Ingrese opción: ")
    match op:
        case "1": #comprar entradas (1-3) mostrar ubicaciones y ocupadas con x
            print("""
        1. Platinum    $120.000     (Asientos del 1 al 20).
        2. Gold        $80.000      (Asientos del 21 al 50).
        3. Silver      $50.000      (Asientos del 51 al 100).
    """)
            pausa()
            ubicacionesdisponibles()
            while True:
                cantidad=int(input("Ingrese la cantidad de entradas a comprar: "))
                if cantidad <=3 and cantidad >=1:
                    break
                else:
                    print("Maximo de entras (3)")
            while cant <= cantidad:
                cant+=1
                while True:
                    ubicacionesdisponibles()
                    ubicacion=int(input("Ingrese número de ubicación: "))
                    if ubicacion <= 100 and ubicacion >=1:
                        entradas.append(ubicacion)
                        break
                    else:
                        print("Ubicación no valida")
                        pausa
                while True:    
                    rut=int(input("Ingrese rut del Asistente (Ejemplo: 12345678): "))
                    if rut >=10000000 and rut <= 99999999:
                        break
                    else:
                        print("Rut no valido...")
                if comprar(rut,ubicacion):
                    print("compra realizada")
                    pausa()
                else:
                    print("No es posible Comprar la ubicacion")
                    pausa()

        case "2": #mostrar ubicaciones disponibles
            ubicacionesdisponibles()

        case "3": #ver listado de asistentes
            print("     Rut | Ubicación")
            for i in asistentes:
                print(f"""
{i[0]} | \t {i[1]}
                  """  )
        
        case "4": #mostrar ganancias totales
            for i in entradas:
                ganancias=int(i)
                if ganancias >=1 and ganancias <= 20:
                    platinum+=1
                elif ganancias >= 21 and ganancias <= 50:
                    gold+=1
                elif ganancias >= 51 and ganancias <= 100:
                    silver+=1
                ganancias+=ganancias  
            
            print(f"""
           | Tipo Entrada | Cantidad | Total |
                Platinum  |\t{platinum}    |\t {platinum*120000}
                Gold      |\t{gold}    |\t {gold*80000}
                Silver    |\t{silver}    |\t {silver*50000}
            
                TOTAL: {(platinum*120000)+(gold*80000)+(silver*50000)}

           """)
        
        case "5": 
            print('Gracias por visitar |Creativos.cl|.')
        case other:
            print("Opción no valida...")
            pausa()
