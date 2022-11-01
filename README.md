# Algoritmo de Harris

El algoritmo de Harris tiene como objetivo identificar las esquinas; es decir la intersección entre dos líneas. 
Esto se logra mediante el calculo de los gradientes, tanto en x como en y, esto sirve para omitir las líneas verticales y horizontales.

| Gradiente en X | Gradiente en Y |
| ------ | ------ |
| ![gradX](https://user-images.githubusercontent.com/117127601/199139544-fb2413a7-fb46-4a78-b805-75415be88561.PNG) | ![gradY](https://user-images.githubusercontent.com/117127601/199139546-91e57330-45a2-4c8e-9196-b7f8896120c1.PNG) |

Después se modifica la matriz de pixeles por vecindades que son matrices de 5x5 en dónde se calcula: 
[[Ix2, IxIy], [IxIy, Iy2]]. Con la nueva imagen generada se realiza un último cálculo que es: det(M)-traza(M). 
Finalmente se plasma la imagen que contendrá las esquinas de las figuras de la imágen original.

| Figuras Originales | Resultado |
| ------ | ------ |
| ![orig](https://user-images.githubusercontent.com/117127601/199139548-a2741d5f-97ef-4574-8511-ebfb1dded43d.PNG) | ![esqui](https://user-images.githubusercontent.com/117127601/199139549-177e6a51-5a17-428a-8a3b-d9536324bffc.PNG) |
