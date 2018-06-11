from random import randint, random, choice, uniform


def rG():
    data =[]
    firma = ['Lenovo', 'HP', 'Asus', 'Acer', 'Dell', 'MSi', 'Samsung', 'LG', 'Apple']
    typ = ['Notebook', 'Tablet', 'PC']
    model = ['AX', 'VIa', 'TH', 'Extrem Nano V', 'Game X', 'S', 'veGa c']
    item_name = choice(firma) + ' ' + choice(model) + str(randint(10,1000))
    data.append(choice(typ))
    data.append(item_name)
    if data[0] == 'Tablet':
        data.append(round(uniform(0.1, 1.2),2))
        data.append(randint(500, 2500))
        data.append(randint(500, 2500))
        data.append(randint(6, 30))
        data.append(0)
        data.append(randint(500, 2500))
    elif data[0] == 'Notebook':
        data.append(round(uniform(0.6, 4.5),2))
        data.append(randint(1000, 8000))
        data.append(randint(1000, 8000))
        data.append(randint(3, 10))
        data.append(randint(5, 30))
        data.append(randint(800, 10000))
    else:
        data.append(round(uniform(3, 8),2))
        data.append(randint(1000, 20000))
        data.append(randint(1000, 20000))
        data.append(0)
        data.append(randint(15, 30))
        data.append(randint(800, 20000))

    procesor = ['i', 'Pentium G', 'Celeron G', 'Ryzen', 'AMD A']
    proc = choice(procesor)
    if proc == 'i':
        proc = proc + choice(['3-', '5-', '7-']) + str(randint(1000, 10000)) + choice(['', 'K'])
    elif proc == 'Pentium G' or 'Celeron G':
        proc = proc + str(randint(1000, 10000))
    elif proc == 'Ryzen':
        proc = proc + ' ' + str(randint(1,9)) + ' ' + str(randint(1000, 10000)) + choice(['', 'G'])
    else:
        proc = proc + str(randint(1,10)) + '-' + str(randint(1000, 10000)) + choice(['','K'])
    data.append(proc)

    graf = choice(["nVidia", "Radeon"])
    if graf == 'nVidia':
        graf = graf + ' ' + choice(['GTX ', 'GT ', 'G']) + str(randint(100, 1100)) + choice(['', 'Ti', 'OC'])
    else:
        graf = graf + ' ' + choice(['Pro ', 'M', 'S', '']) + choice(['WX', 'S', '']) + str(randint(100, 10000))
    data.append(graf)

    print("Rand: {0} {1} {2}kg {3}CPU {4}GPU {5}h {6}dB {7}PLN {8} {9}".format(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]))
    return data