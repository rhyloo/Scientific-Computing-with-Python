### Assignment

Complete the `Category` class in `budget.py`. It should be able to instantiate objects based on different budget categories like *food*, *clothing*, and *entertainment*. When objects are created, they are passed in the name of the category. The class should have an instance variable called `ledger` that is a list. The class should also contain the following methods:

* A `deposit` method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of `{"amount": amount, "description": description}`.
* A `withdraw` method that is similar to the `deposit` method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return `True` if the withdrawal took place, and `False` otherwise.
* A `get_balance` method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
* A `transfer` method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return `True` if the transfer took place, and `False` otherwise.
* A `check_funds` method that accepts an amount as an argument. It returns `False` if the amount is greater than the balance of the budget category and returns `True` otherwise. This method should be used by both the `withdraw` method and `transfer` method.

When the budget object is printed it should display:
* A title line of 30 characters where the name of the category is centered in a line of `*` characters.
* A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
* A line displaying the category total.

Here is an example of the output:
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

Besides the `Category` class, create a function (outside of the class) called `create_spend_chart` that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

The unit tests for this project are in `test_module.py`.

### Development

Write your code in `budget.py`. For development, you can use `main.py` to test your `Category` class. Click the "run" button and `main.py` will run.

### Testing 

We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

### Submitting

Copy your project's URL and submit it to freeCodeCamp.


## Traducción

### Asignación

Completa la clase `Category` en` budget.py`. Debería poder crear instancias de objetos basados ​​en diferentes categorías de presupuesto como * comida *, * ropa * y * entretenimiento *. Cuando se crean objetos, se pasan con el nombre de la categoría. La clase debe tener una variable de instancia llamada "ledger" que es una lista. La clase también debe contener los siguientes métodos:

* Un método de "depósito" que acepta una cantidad y una descripción. Si no se proporciona una descripción, debería ser una cadena vacía por defecto. El método debe agregar un objeto a la lista del libro mayor en forma de `{" monto ": monto," descripción ": descripción}`.
* Un método de "retiro" que es similar al método de "depósito", pero la cantidad transferida debe almacenarse en el libro mayor como un número negativo. Si no hay fondos suficientes, no se debe agregar nada al libro mayor. Este método debería devolver "Verdadero" si se realizó el retiro y "Falso" en caso contrario.
* Un método "get_balance" que devuelve el saldo actual de la categoría de presupuesto en función de los depósitos y retiros que se han producido.
* Un método de "transferencia" que acepta una cantidad y otra categoría de presupuesto como argumentos. El método debe agregar un retiro con el monto y la descripción "Transferencia a [Categoría de presupuesto de destino]". Luego, el método debe agregar un depósito a la otra categoría de presupuesto con el monto y la descripción "Transferencia desde [Categoría de presupuesto de origen]". Si no hay fondos suficientes, no se debe agregar nada a ninguno de los libros de contabilidad. Este método debería devolver "True" si la transferencia se realizó y "False" en caso contrario.
* Un método `check_funds` que acepta una cantidad como argumento. Devuelve "Falso" si la cantidad es mayor que el saldo de la categoría de presupuesto y devuelve "Verdadero" en caso contrario. Este método debe utilizarse tanto con el método de "retirada" como con el método de "transferencia".

Cuando se imprime el objeto de presupuesto, debería mostrar:
* Una línea de título de 30 caracteres donde el nombre de la categoría se centra en una línea de caracteres `*`.
* Una lista de los elementos del libro mayor. Cada línea debe mostrar la descripción y el monto. Deben mostrarse los primeros 23 caracteres de la descripción, luego la cantidad. La cantidad debe estar alineada a la derecha, contener dos decimales y mostrar un máximo de 7 caracteres.
* Una línea que muestra el total de la categoría.

A continuación, se muestra un ejemplo de la salida:
''
*************Comida*************
depósito inicial 1000,00
comestibles -10.15
restaurante y más foo -15,89
Transferencia a la ropa -50.00
Total: 923,96
''

Además de la clase `Category`, crea una función (fuera de la clase) llamada` create_spend_chart` que tome una lista de categorías como argumento. Debería devolver una cadena que sea un gráfico de barras.

El gráfico debe mostrar el porcentaje gastado en cada categoría transferida a la función. El porcentaje gastado debe calcularse solo con retiros y no con depósitos. Abajo, en el lado izquierdo del gráfico, deben estar las etiquetas 0 - 100. Las "barras" en el gráfico de barras deben estar hechas con el carácter "o". La altura de cada barra debe redondearse hacia abajo a la décima más cercana. La línea horizontal debajo de las barras debe ir dos espacios más allá de la barra final. El nombre de cada categoría debe escribirse verticalmente debajo de la barra. Debe haber un título en la parte superior que diga "Porcentaje gastado por categoría".

Esta función se probará con hasta cuatro categorías.

Mire la salida de ejemplo a continuación muy de cerca y asegúrese de que el espaciado de la salida coincida exactamente con el ejemplo.

''
Porcentaje gastado por categoría
100 |
 90 |
 80 |
 70 |
 60 | o
 50 | o
 40 | o
 30 | o
 20 | o o
 10 | o o o
  0 | o o o
    ----------
     F C A
     o l u
     o o t
     d t o
        h
        I
        norte
        gramo
''

Las pruebas unitarias para este proyecto están en `test_module.py`.

### Desarrollo

Escriba su código en `budget.py`. Para el desarrollo, puede usar `main.py` para probar su clase` Category`. Haga clic en el botón "ejecutar" y se ejecutará `main.py`.

### Pruebas

Importamos las pruebas de `test_module.py` a` main.py` para su conveniencia. Las pruebas se ejecutarán automáticamente cada vez que presione el botón "ejecutar".

### Envío

Copie la URL de su proyecto y envíelo a freeCodeCamp.