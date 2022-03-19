my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)
#Lo que hace un for loop

#print(type(my_iter))

#Extraer los elementos del primer iterable

print(next(my_iter)) 

def my_gen():
    a = 1
    yield a #return pero parcial que reemplaza el valor
    a = 2
    yield a
    a = 3 
    yield a

my_first_gen = my_gen() #Hacer print con next() devuelve todos los valores de la lista iterada

#Generadores con números pares del 1 al 100

def my_pair_gen():
    for i in range(0, 201):
        if i % 2 == 0:
            yield i
        

my_pair_gen = my_pair_gen()

for i in range(100):
    print(my_pair_gen)


