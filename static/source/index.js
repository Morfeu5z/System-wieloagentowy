/**
 * Lista wskazujaca na zaznaczone przyciski
 * @type {number[]}
 */
ansList = [
    0, 0, 0,
    0, 0, 0,
    0, 0, 0,
    0, 0, 0
];

/**
 * Zmiana listy wartości po kliknięciu
 * @param butt
 */
function buttClick(butt) {
    var name = butt.name;
    var elem = document.getElementsByName(name);
    elem[0].className = "btn btn-outline-info";
    elem[1].className = "btn btn-outline-info";
    elem[2].className = "btn btn-outline-info";
    var x = parseInt(butt.id[1]);
    var y = parseInt(butt.id[0]);
    pos = ((y * 3) - 3) + 0;
    ansList[pos] = false;
    pos = ((y * 3) - 3) + 1;
    ansList[pos] = false;
    pos = ((y * 3) - 3) + 2;
    ansList[pos] = false;
    pos = ((y * 3) - 3) + (x - 1);
    ansList[pos] = true;
    butt.className = "btn btn-info";
}

/**
 * Wyślij dane
 */
function showAns() {
    var priList = [
        document.getElementById('range1').value,
        document.getElementById('range2').value,
        document.getElementById('range3').value,
        document.getElementById('range4').value,
        document.getElementById('range5').value
    ];
    var price = document.getElementById('price').value;
    console.log('Odpowiedzi: ' + ansList);
    console.log('Priorytety: ' + priList);
    console.log('Cena: ' + price);
    $.post({
        url: 'getData',
        data: {
            'butt': JSON.stringify(ansList),
            'prio': JSON.stringify(priList),
            'pric': price,
        },
        success: function (response) {
            console.log('Wysłano agentów.');
            console.log(response);
            $('#responde').text(response.response);
            window.location = '#responde';
        },
        error: function (error) {
            console.log('Coś poszło nie tak.');
            console.log(error);
        }
    });
}

/**
 * Update priorytetów
 * @param range
 */
function rangeChange(range) {
    var ran = range.value;
    console.log(ran);
    switch (ran){
        case "1":
            document.getElementById('span' + range.name).innerText = 'niski';
            break;
        case "2":
            document.getElementById('span' + range.name).innerText = 'sredni';
            break;
        case "3":
            document.getElementById('span' + range.name).innerText = 'wysoki';
            break;
        default:
            document.getElementById('span' + range.name).innerText = 'niski';
            break;
    }
}
