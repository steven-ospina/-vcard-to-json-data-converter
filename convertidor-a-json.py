import json

def run():

    url_archive = '00001.vcf'
    reading_method = 'r'
    dictionary = {}
    dictionary_update = {}
    dictionarys = dict()
    data = []
    bd = []
    jsonn = []
    count = 0
    count2 = 0

    with open(url_archive, reading_method, encoding="utf-8") as fe:

        list_data = fe.readlines()

        max_index = len(list_data) - 1

        print(max_index)

        while count <= max_index:
            datos = list_data[count].rstrip('\n')
            bd.append(datos)
            # print(datos)
            count = count + 1

        count = 0
        max_index_two = len(bd) - 1

        while count <=max_index_two:
            dato_solo = bd[count]
            search_dos_puntos = ':' in dato_solo
            search_punto_coma = dato_solo.count(';')

            if search_punto_coma == 1:
                dato_punto_coma = bd[count].split(';', 1)
            if search_dos_puntos:
                dato_dos_puntos = bd[count].split(':')

            try:

                if search_dos_puntos:
                    dictionary = {dato_dos_puntos[0] : dato_dos_puntos[1]}
                if search_punto_coma == 1:
                    dictionary = {dato_punto_coma[0] : dato_punto_coma[1]}
                
                dictionary_update.update(dictionary)

                # print(dictionarys)
                # print(dictionary_update)
                if dato_solo == 'END:VCARD':
                    # jsonn.append(dictionary_update)
                    count2 += 1
                    dictionarys[str(count2)] = dictionary_update
                    dictionary_update = {}
                    dictionary = {}
                    # print(jsonn)
                    continue
            except:
                print('la cagaste')
            finally:
                count = count + 1
                if count == 25857:
                    print('hola')
                    
        # dotocos = json.dumps(dictionarys)
        # print(dotocos)

        try:
            with open('datos_sin_saltos.json', 'w') as f:
                json.dump(dictionarys, f)
        except:
            print('no se pudo escribir el archivo')


if __name__ == '__main__':
    run()