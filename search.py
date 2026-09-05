"""Este modulo define la clase LocalSearch.

LocalSearch representa un algoritmo de busqueda local general.

Las subclases que se encuentran en este modulo son:

* HillClimbing: algoritmo de ascension de colinas. Se mueve al sucesor con
mejor valor objetivo, y los empates se resuelvan de forma aleatoria.
Ya viene implementado.

* HillClimbingReset: algoritmo de ascension de colinas de reinicio aleatorio.
No viene implementado, se debe completar.

* Tabu: algoritmo de busqueda tabu.
No viene implementado, se debe completar.
"""


from __future__ import annotations
from problem import OptProblem
from random import choice
from time import time


class LocalSearch:
    """Clase que representa un algoritmo de busqueda local general."""

    def __init__(self) -> None:
        """Construye una instancia de la clase."""
        self.niters = 0  # Numero de iteraciones totales
        self.time = 0  # Tiempo de ejecucion
        self.tour = []  # Solucion, inicialmente vacia
        self.value = None  # Valor objetivo de la solucion

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion."""
        self.tour = problem.init
        self.value = problem.obj_val(problem.init)


class HillClimbing(LocalSearch):
    """Clase que representa un algoritmo de ascension de colinas.

    En cada iteracion se mueve al estado sucesor con mejor valor objetivo.
    El criterio de parada es alcanzar un optimo local.
    """

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        value = problem.obj_val(problem.init)

        while True:

            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan
            diff = problem.val_diff(actual)

            # Buscar las acciones que generan el mayor incremento de valor obj
            max_acts = [act for act, val in diff.items() if val ==
                        max(diff.values())]

            # Elegir una accion aleatoria
            act = choice(max_acts)

            # Retornar si estamos en un optimo local 
            # (diferencia de valor objetivo no positiva)
            if diff[act] <= 0:

                self.tour = actual
                self.value = value
                end = time()
                self.time = end-start
                return

            # Sino, nos movemos al sucesor
            else:

                actual = problem.result(actual, act)
                value = value + diff[act]
                self.niters += 1


class HillClimbingReset(LocalSearch):
    """Algoritmo de ascension de colinas con reinicio aleatorio."""

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas
        con reinicio aleatorio.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        value = problem.obj_val(problem.init)

        # Definimos la variable para limitar el número de reseteos
        resets = 0
        
        while resets < 5:

            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan
            diff = problem.val_diff(actual)

            # Buscar las acciones que generan el mayor incremento de valor obj
            max_acts = [act for act, val in diff.items() if val ==
                        max(diff.values())]

            # Elegir una accion aleatoria
            act = choice(max_acts)

            #Si es el primer óptimo local que encontramos almacenarlo y resetear aleatoriamente
            #Sino si es mejor que el almacenado reemplazarlo y resetear aleatoriamente
            if diff[act] <= 0:

                if self.tour == []:
                    self.tour = actual
                    self.value = value

                elif self.value < value:
                    self.tour = actual
                    self.value = value
                actual = problem.random_reset()
                value = problem.obj_val(actual)
                resets += 1

            # Sino, nos movemos al sucesor
            else:
                actual = problem.result(actual, act)
                value = value + diff[act]
                self.niters += 1

        end = time()
        self.time = end-start


class Tabu(LocalSearch):
    """Algoritmo de busqueda tabu."""
    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas
        con reinicio aleatorio.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
         # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        
        best = actual
        tabu = []
        
        # Criterio de parada 1000 iteraciones sin mejora
        i = 0
        while  i < 1000:
            
            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan
            diff = problem.val_diff(actual)
            
            # Nos quedamos con las acciones que se pueden aplicar
            # que no forman parte de la lista tabu 
            tabu_actions = [(act, val) for act, val in diff.items() if act not in tabu]
            
            # De las acciones que no forman parte de la lista tabu
            # Separamos la/s del mayor valor objetivo
            max_val = max(tupla[1] for tupla  in tabu_actions)
            max_acts =  [act for act, val in tabu_actions if val ==
                        max_val]
            act = choice(max_acts)
            
            # Comparamos el estado elegido con el mejor encontrado
            i += 1
            if problem.obj_val(problem.result(actual, act)) > problem.obj_val(best):
                best = problem.result(actual, act)
                i = 0
                
            actual = problem.result(actual, act)
            tabu.append(act)
            
            # Las acciones perduran 70 iteraciones en la lista tabu
            if len(tabu) > 70:
                tabu.pop(0)
                    
            self.niters += 1
            
        self.tour = best
        self.value = problem.obj_val(best)
        end = time()
        self.time = end-start