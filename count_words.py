#! -*- encoding: utf8 -*-


import argparse
import re
import sys
from typing import Counter


def sort_dic_by_values(d, asc=True):
    return sorted(d.items(), key=lambda a: (-a[1], a[0]))

class WordCounter:

    def __init__(self):
        """
           Constructor de la clase WordCounter
        """
        self.clean_re = re.compile('\W+')

    def write_stats(self, filename, stats, use_stopwords, full):
        """
        Este método escribe en fichero las estadísticas de un texto
            
        :param 
            filename: el nombre del fichero destino.
            stats: las estadísticas del texto.
            use_stopwords: booleano, si se han utilizado stopwords
            full: boolean, si se deben mostrar las stats completas

        :return: None
        """

        with open('stats.txt', 'w') as fh:
            #Escribir en el documento las estadisticas
            fh.write('Numero de lineas = ' + str(stats['nlines']) + '\n')
            if use_stopwords: fh.write('Numero de palabras (sin stopwords) = ' + str(stats['nwords']) + '\n')
            else: fh.write('Numero de palabras (con stopwords)= ' + str(stats['nwords']) + '\n')
            fh.write('Tamaño del vocabulario = ' + str(len(stats['word'])) + '\n')
            fh.write('Numero de simbolos = ' + str(stats['nsymbols']) + '\n')
            fh.write('Numero de simbolos diferentes = ' + str(len(stats['symbol'])) + '\n')
            #Palabras
            if full:
                fh.write('Palabras contenidas (orden alphabetico)= ' + '\n')
                for w in sorted(stats['word']): fh.write('\t' + str(w) + ':' + str(stats['word'][w]) + '\n') 
            else:  
                fh.write('Palabras contenidas (orden alphabetico)= ' + '\n')
                cont = 0
                for w in sorted(stats['word']): 
                    if cont < 3:
                        fh.write('\t' + str(w) + ':' + str(stats['word'][w]) + '\n')    
                    elif cont == 3:fh.write('...'+ '\n')
                    elif cont > len(stats['word']) - 4:
                        fh.write('\t' + str(w) + ':' + str(stats['word'][w]) + '\n')
                    cont +=1
            if full: 
                fh.write('Palabras contenidas (orden por frecuencia)= ' + '\n')
                for w in sorted(stats['word'], key=stats['word'].get, reverse=True): fh.write('\t' + str(w) + ':' + str(stats['word'][w]) + '\n')
            else: 
                fh.write('Palabras contenidas (orden por frecuencia)= ' + '\n')
                cont = 0
                for w in sorted(stats['word'], key=stats['word'].get, reverse=True): 
                    if cont < 3:
                        fh.write('\t' + str(w) + ':' + str(stats['word'][w]) + '\n')
                    elif cont == 3:fh.write('...'+ '\n')
                    elif cont > len(stats['word']) - 4:
                        fh.write('\t' + str(w) + ':' + str(stats['word'][w]) + '\n')
                    cont +=1
            #Simbolos
            if full: 
                fh.write('Simbolos contenidos (orden alfabetico)= ' + '\n')
                for w in sorted(stats['symbol']): fh.write('\t' + str(w) + ':' + str(stats['symbol'][w]) + '\n')
            else: 
                fh.write('Simbolos contenidos (orden alfabetico)= ' + '\n')
                cont = 0
                for w in sorted(stats['symbol']): 
                    if cont < 3:
                        fh.write('\t' + str(w) + ':' + str(stats['symbol'][w]) + '\n')
                    elif cont == 3:fh.write('...'+ '\n')
                    elif cont > len(stats['symbol']) - 4:
                        fh.write('\t' + str(w) + ':' + str(stats['symbol'][w]) + '\n')
                    cont +=1
            if full: 
                fh.write('Simbolos contenidos (orden por frecuencia)= ' + '\n')
                for w in sorted(stats['symbol'], key=stats['symbol'].get, reverse=True): fh.write('\t' + str(w) + ':' + str(stats['symbol'][w]) + '\n')
            else: 
                fh.write('Simbolos contenidos (orden por frecuencia)= ' + '\n')
                cont = 0
                for w in sorted(stats['symbol'], key=stats['symbol'].get, reverse=True): 
                    if cont < 3:
                        fh.write('\t' + str(w) + ':' + str(stats['symbol'][w]) + '\n')
                    elif cont == 3:fh.write('...'+ '\n')
                    elif cont > len(stats['symbol']) - 4:
                        fh.write('\t' + str(w) + ':' + str(stats['symbol'][w]) + '\n')
                    cont +=1
            #Bigramas
            if 'biword' in stats:
                if full:    
                    fh.write('Bigramas (orden alfabetico)=' + '\n')
                    for w in sorted(stats['biword']): fh.write('\t' + str(w) + ':' + str(stats['biword'][w]) + '\n')
                    fh.write('Bigramas (orden por frequencia)=' + '\n')
                    for w in sorted(stats['biword'], key=stats['biword'].get, reverse=True): fh.write('\t' + str(w) + ':' + str(stats['biword'][w]) + '\n')
                else:
                    fh.write('Bigramas (orden alfabetico)=' + '\n')
                    cont = 0
                    for w in sorted(stats['biword']): 
                        if cont < 3:
                            fh.write('\t' + str(w) + ':' + str(stats['biword'][w]) + '\n')
                        elif cont == 3:fh.write('...'+ '\n')
                        elif cont > len(stats['biword']) - 4:
                            fh.write('\t' + str(w) + ':' + str(stats['biword'][w]) + '\n')
                        cont +=1
                    fh.write('\t' + str(w) + ':' + str(stats['biword'][w]) + '\n')
                    fh.write('Bigramas (orden por frequencia)=' + '\n')
                    cont = 0
                    for w in sorted(stats['biword'], key=stats['biword'].get, reverse=True): 
                        if cont < 3:
                            fh.write('\t' + str(w) + ':' + str(stats['biword'][w]) + '\n')
                        elif cont == 3:fh.write('...'+ '\n')
                        elif cont > len(stats['biword']) - 4:
                            fh.write('\t' + str(w) + ':' + str(stats['biword'][w]) + '\n')
                        cont +=1
                if full:    
                    fh.write('Bisimbolos (orden alfabetico)=' + '\n')
                    for w in sorted(stats['bisymbol']): fh.write('\t' + str(w) + ':' + str(stats['bisymbol'][w]) + '\n')
                    fh.write('Bisimbolos (orden por frequencia)=' + '\n')
                    for w in sorted(stats['bisymbol'], key=stats['bisymbol'].get, reverse=True): fh.write('\t' + str(w) + ':' + str(stats['bisymbol'][w]) + '\n')
                else:
                    fh.write('Bisimbolos (orden alfabetico)=' + '\n')
                    cont = 0
                    for w in sorted(stats['bisymbol']): 
                        if cont < 3:
                            fh.write('\t' + str(w) + ':' + str(stats['bisymbol'][w]) + '\n')
                        elif cont == 3:fh.write('...'+ '\n')
                        elif cont > len(stats['bisymbol']) - 4:
                            fh.write('\t' + str(w) + ':' + str(stats['bisymbol'][w]) + '\n')
                        cont +=1
                    fh.write('\t' + str(w) + ':' + str(stats['bisymbol'][w]) + '\n')
                    fh.write('Bisimbolos (orden por frequencia)=' + '\n')
                    cont = 0
                    for w in sorted(stats['bisymbol'], key=stats['bisymbol'].get, reverse=True): 
                        if cont < 3:
                            fh.write('\t' + str(w) + ':' + str(stats['bisymbol'][w]) + '\n')
                        elif cont == 3:fh.write('...'+ '\n')
                        elif cont > len(stats['bisymbol']) - 4:
                            fh.write('\t' + str(w) + ':' + str(stats['bisymbol'][w]) + '\n')
                        cont +=1

    def file_stats(self, filename, lower, stopwordsfile, bigrams, full):
        """
        Este método calcula las estadísticas de un fichero de texto
        :param 
            filename: el nombre del fichero.
            lower: booleano, se debe pasar todo a minúsculas?
            stopwordsfile: nombre del fichero con las stopwords o None si no se aplican
            bigram: booleano, se deben calcular bigramas?
            full: booleano, se deben montrar la estadísticas completas?

        :return: None
        """
        stopwords = [] if stopwordsfile is None else open(stopwordsfile).read().split()

        # variables para los resultados
        sts = {
                'nwords': 0,
                'nlines': 0,
                'word': {},
                'nsymbols' : 0,
                'symbol': {}
                }
        print(bigrams)

        if bigrams:
            sts['biword'] = {}
            sts['bisymbol'] = {}

        # completar
        new_filename = open(filename, 'r', encoding= 'utf8')    #Abres el archivo que quieres leer en modo lectura.

        #Divides el archivo en las filas que tienes, asi consigues librarte del salto de linea(\n)
        lines_split = new_filename.read().splitlines()
        
        #Recorres cada linea del archivo para sacar las estadisticas
        for l in lines_split: 
            if lower: l = l.lower()         #Si opcion lower activada, entonces pasas cada linea a minusculas
            l_no_symbols = re.sub(self.clean_re, ' ', l)    #Te guardas las palabras sin simbolos
            l_symbols = re.findall(self.clean_re, l)        #Te guardas los simbolos
            l_symbols = list(filter(lambda a: a != ' ', l_symbols))     #Filtras de los simbolos los espacions
            sts['symbol'] = Counter(l_symbols) + Counter(l_no_symbols)      #Diccionario de todos los simbolos y su frecuencia
            sts['nsymbols'] = sts['nsymbols'] + len(l_symbols)  #Añades al num. de simbolos de la fila anterior los de esta fila
            words = l_no_symbols.split()                        #Pasas el string de palabras sin simbolos a una lista
            for word in words:                                  #Recorres la lista de palabras
                if stopwords is not [] and word in stopwords:        #Si opcion -s, se eliminan las stopwords de la linea
                    word = ''
                sts['nwords'] = sts['nwords'] + 1               #Para cada palabra recorrida se lleva un contador
                #Para cada palabra se mira si esta en el diccionario, si no esta, se inicializa a 1, si esta se incrementa el contador en 1.
                if word in sts['word']:sts['word'][word] = sts['word'][word] + 1 
                else: sts['word'][word] = 1
            sts['nlines'] = sts['nlines'] + 1               #Contador del numero de lineas
        
        sts['symbol'].pop(' ')
        sts['nsymbols'] = sts['nsymbols'] + sts['nwords']       #Contador de numero de simbolos + palabras
        #Si opcion bigrama
        if bigrams:  
            bigramas = []
            bisimb = []
            for l in lines_split:
                l = '$ '+ l +' $'   #Añades los simbolos a inicio y final 
                if lower: l = l.lower()     #Si -l pasas a minusculas
                big = [b for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]   #Obtienes bigramas palabras
                simb = [b for b in zip(list(l)[:-1], list(l)[1:])]          #Obtienes bigramas simbolos
                bigramas = bigramas + big       
                bisimb = bisimb + simb
            sts['biword'] = Counter(bigramas)       #Pasas lista de bigramas a diccionario
            sts['bisymbol'] = Counter(bisimb)       #Pasas lista de bigramas a diccionario
        self.write_stats(new_filename, sts, stopwordsfile is not None, full)


    def compute_files(self, filenames, **args):
        """
        Este método calcula las estadísticas de una lista de ficheros de texto

        :param 
            filenames: lista con los nombre de los ficheros.
            args: argumentos que se pasan a "file_stats".

        :return: None
        """

        for filename in filenames:
            self.file_stats(filename, **args)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Compute some statistics from text files.')
    parser.add_argument('file', metavar='file', type=str, nargs='+',
                        help='text file.')

    parser.add_argument('-l', '--lower', dest='lower',
                        action='store_true', default=False, 
                        help='lowercase all words before computing stats.')

    parser.add_argument('-s', '--stop', dest='stopwords', action='store',
                        help='filename with the stopwords.')

    parser.add_argument('-b', '--bigram', dest='bigram',
                        action='store_true', default=False, 
                        help='compute bigram stats.')

    parser.add_argument('-f', '--full', dest='full',
                        action='store_true', default=False, 
                        help='show full stats.')

    args = parser.parse_args()
    wc = WordCounter()
    wc.compute_files(args.file,
                     lower=args.lower,
                     stopwordsfile=args.stopwords,
                     bigrams=args.bigram,
                     full=args.full)


