# coding=utf-8
import heapq

from mrjob.job import MRJob

'''
Viktor Jacynycz García y Miguel del Andrés Herrero declaramos que esta solución es fruto
exclusivamente de nuestro trabajo personal. No hemos sido ayudados por ninguna otra persona
ni hemos obtenido la solución de fuentes externas, y tampoco hemos compartido nuestra solución
con nadie. Declaramos además que no hemos realizado de manera deshonesta ninguna otra actividad
que pueda mejorar nuestros resultados ni perjudicar los resultados de los demás.
'''


class MRWordCount(MRJob):
    # Fase MAP (line es una cadena de texto)
    def mapper(self, key, line):
        linesplit = line.split()
        word = linesplit[0]
        haverage = float(linesplit[2])
        trank = linesplit[4]
        if haverage < 2:
            if trank != "--":
                yield None, (haverage, word)

    def reducer(self, _, diccionario):
        # cada valor del diccionario es (puntuacion, palabra)
        top_n = heapq.nlargest(5, diccionario)
        for it in top_n:
            yield it


if __name__ == '__main__':
    MRWordCount.run()
