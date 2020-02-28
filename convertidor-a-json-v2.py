import json

def run():

    url_archive = '00001.vcf'
    reading_method = 'r'
    dictionary = {}
    dictionary_update = {}
    dictionarys_father = dict()
    data_clean = []
    count1 = 1
    count2 = 0
    count3 = 0
    seguimiento = 0
    two_ponits = ['']
    bandera = ''
    tel_list = []
    swicht = False


    with open(url_archive, reading_method, encoding="utf-8") as fe:

        list_data = fe.readlines()

        max_index = len(list_data)

        # Run the data you get from the ".vcf" file and delete the new line breaks
        # Recorre los datos que obtiene del archivo ".vcf" y les elimina los saltos nuevos de línea
        for i in range(max_index):
            data_without_new_line = list_data[i].rstrip('\n')
            data_clean.append(data_without_new_line)

        max_index_two = len(data_clean)

        for i in range(max_index_two):
            print(data_clean[i])
            if swicht == True:
                swicht = False
                continue

            bandera = True

            only_one_data = data_clean[i]

            search_by_two_points = ':' in only_one_data
            search_by_semicolons = only_one_data.count(';')

            if search_by_semicolons == 1:
                semicolons = data_clean[i].split(';', 1)
            if search_by_two_points:
                two_ponits = data_clean[i].split(':')
            
            # try:
            #     print(dictionary_update['TEL:'])
            #     if dictionary_update['TEL:']:
            #         continue
            # except:
            #     print('')

            try:
                if two_ponits[0] == 'TEL;CELL' or two_ponits[0] == 'TEL;WORK':
                    seguimiento = i

                    while bandera:
                        # print(i)

                        count3 = count3 + 1

                        search = data_clean[i].split(':')

                        dict_tel = {f'{search[0]}{count3}' : search[1]}
                        
                        tel_list.append(dict_tel)

                        i = i + count1

                        search = data_clean[i].split(':')

                        if search[0] == 'TEL;CELL' or search[0] == 'TEL;CELL':
                            print('hola')
                        else:
                            print(data_clean[i])
                            # print(seguimiento)
                            dictionary = {'TEL:' : tel_list}
                            dictionary_update.update(dictionary)
                            bandera = False
                            seguimiento = i
                            swicht = True
                            dictionary = {}
                            tel_list = []
                            continue
                    continue
            except:
                print('error en buscar telefono')

            try:

                if search_by_two_points:
                    dictionary = {two_ponits[0] : two_ponits[1]}
                elif search_by_semicolons == 1:
                    dictionary = {semicolons[0] : semicolons[1]}

                dictionary_update.update(dictionary)

                # print(dictionary_update)
                if only_one_data == 'END:VCARD':
                    count2 += 1
                    dictionarys_father[str(count2)] = dictionary_update
                    dictionary_update = {}
                    dictionary = {}
                    continue
            except:
                print('error')
            finally:
                if i == 25857:
                    print('hola')


        try:
            with open('data_vcard.json', 'w') as f:
                json.dump(dictionarys_father, f)
        except:
            print('no se pudo escribir el archivo')


if __name__ == '__main__':
    run()