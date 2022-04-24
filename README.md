<p align="center">
  <a href="https://github.com/nahuelbrandan/SaganSat"><img src="./resources/img/SaganSat_banner.png" alt="SaganSat banner"></a>
</p>
<p align="center">
    <em>SaganSat, simulate the tasking of a satellites fleet.</em>
</p>

---
>> Somewhere, something incredible is waiting to be known. ― Carl Sagan.
---

## Description

El sistema de vuelo consiste de una estación terrena y de dos satelites de vuelo. 
Cada uno de estos elementos es un proceso independiente del sistema operativo.

La estacion terrena recibe una lista de tareas, y éste le indica a cada uno de los satelites que tareas tendra que realizar.

Las tareas tienen los siguientes atributos:
- nombre
- recursos: Lista de identificadores de recursos que necesita una tarea. Éstos funcionan
como locks excluyentes. Un satélite no puede ejecutar dos tareas que usen algún mismo
recurso. No hay un límite a la cantidad de recursos que una tarea puede usar o la cantidad
de recursos distintos que hay.
- payoff: El beneficio que genera ejecutar la tarea.

### Ejemplo

* task1
  * name="fotos"
  * recursos=[1, 5]
  * payoff=10
* task2
  * name="mantenimiento"
  * recursos=[1, 2]
  * payoff=1
* task3
  * name="pruebas" 
  * recursos=[5, 6]
  * payoff=1
* task4
  * name="fsck"
  * recursos=[1, 6]
  * payoff=0.1

En este caso una buena asignación sería la siguiente:

- La estación terrena le da task1 al satélite 1.
- La estación terrena le da task2 y task3 al satélite 2.
- La task4 no se puede realizar.

**La asignación de tareas debe maximizar el payoff.**

---

**Cuando el satélite recibe las tareas debe responder qué tareas pudo realizar y cuáles no en función
de una llamada a random diciendo que no pudo realizar una tarea el 10% de las veces.**

---

**TODO** mejorar la descripcion.

![TODO imagen con descripcion de la arquitectura]()

## Pre requisites

* Python>=3.6

This project was only tested with Python 3.6, but could theoretically run with Python >= 3.6.

## Installation

Steps to install the project:

### Manual
* Clone this repository.
* It's recommended create and activate a *virtual environment*, based in Python>=3.6.
* `make install`

## Run

* `make run`
* Access to [http://localhost:8000/](http://localhost:8000/) for see details of how to make requests to the API.

## Usage

Examples of requests to use the project:

TODO. 

## Test

`make test`

In addition to executing the test suite, this command generates a coverage report too.

## To improve

* Through performance testing, using a list of tasks with required resources of the order of millions of elements, 
a considerable drop in performance is obtained, the system taking a long time to finish processing.

## Licence

This project is licensed under the terms of the GNU GENERAL PUBLIC LICENSE, Version 3.
