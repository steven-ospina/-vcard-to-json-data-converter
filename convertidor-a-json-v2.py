import json


def run():
    
    dictionarys_father = dict()
    dictionary = {}
    dictionary_update = {}
    data_clean = []
    multiple_data = []
    two_points = ['']
    count1 = 1
    count2 = 0
    count3 = 0
    count4 = 0
    flag = ''
    url_archive = '00001.vcf'
    reading_method = 'r'
    number_photo = 0


    with open(url_archive, reading_method, encoding="utf-8") as fe:

        list_data = fe.readlines()

        max_index = len(list_data)

        # Run the data you get from the ".vcf" file and delete the new line breaks
        # Recorre los datos que obtiene del archivo ".vcf" y les elimina los saltos nuevos de línea
        for i in range(max_index):
            data_without_new_line = list_data[i].rstrip('\n')
            data_clean.append(data_without_new_line)

        max_index_two = len(data_clean) - 1

        while count4 <= max_index_two:

            flag = True

            only_one_data = data_clean[count4]

            search_by_two_points = ':' in only_one_data
            search_by_semicolons = only_one_data.count(';')

            if search_by_semicolons == 1:
                semicolons = data_clean[count4].split(';', 1)
            if search_by_two_points:
                two_points = data_clean[count4].split(':')

            try:
                if two_points[0] == 'TEL;CELL' or two_points[0] == 'TEL;WORK':

                    while flag:

                        count3 = count3 + 1

                        search = data_clean[count4].split(':')

                        dict_tel = {f'{search[0]}-{count3}' : search[1]}
                        
                        multiple_data.append(dict_tel)

                        count4 = count4 + count1

                        search = data_clean[count4].split(':')

                        if search[0] == 'TEL;CELL' or search[0] == 'TEL;WORK':
                            pass
                        else:
                            dictionary = {'TEL:' : multiple_data}
                            dictionary_update.update(dictionary)
                            flag = False
                            dictionary = {}
                            multiple_data = []
                            count4 = count4
                            count3 = 0
                            continue
                            
                    continue
            except Exception as error:
                print('error en buscar telefono', error)

            try:
                if two_points[0] == 'EMAIL;X-INTERNET' or two_points[0] == 'EMAIL;HOME' or two_points[0] == 'EMAIL;WORK':

                    while flag:

                        count3 = count3 + 1

                        search = data_clean[count4].split(':')

                        dict_tel = {f'{search[0]}-{count3}' : search[1]}
                        
                        multiple_data.append(dict_tel)

                        count4 = count4 + count1

                        search = data_clean[count4].split(':')

                        email = search[0].split(';')

                        if email[0] != 'EMAIL':
                            dictionary = {'EMAILS:' : multiple_data}
                            dictionary_update.update(dictionary)
                            flag = False
                            dictionary = {}
                            multiple_data = []
                            count4 = count4
                            count3 = 0
                            continue
                    continue
            except Exception as error:
                print('error en buscar telefono', error)

            try:
                if two_points[0] == 'PHOTO;ENCODING=BASE64;JPEG':

                    data_base = two_points[1]

                    while flag:

                        count4 = count4 + count1

                        search = data_clean[count4]

                        # if search == ' nBQjZH//Z':
                        #     print('t')

                        if search == '':
                            number_photo = number_photo + 1
                            dictionary_photo = {f'{number_photo}-{two_points[0]}' : data_base}
                            dictionary_update.update(dictionary_photo)
                            search = ''
                            flag = False
                            dictionary = {}
                            count4 = count4
                            two_points[0] = ''
                            dictionary_photo = {}
                            continue
                        else:
                            data_base += search.strip()

                    continue
            except Exception as error:
                print('error en PHOTO', error)

            try:

                if search_by_two_points:
                    dictionary = {two_points[0] : two_points[1]}
                elif search_by_semicolons == 1:
                    dictionary = {semicolons[0] : semicolons[1]}

                dictionary_update.update(dictionary)

                if only_one_data == 'END:VCARD':
                    count2 += 1
                    dictionarys_father[str(count2)] = dictionary_update
                    dictionary_update = {}
                    dictionary = {}
                    number_photo = 0
                    continue
            except Exception as err:
                print('error', err)
            finally:
                count4 = count4 + 1

    try:
        with open('data_vcard.json', 'w') as f:
            json.dump(dictionarys_father, f)
    except:
        print('no se pudo escribir el archivo')


if __name__ == '__main__':
    run()