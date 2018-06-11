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
    $('#imgLoading').css({'display': 'initial'});
    $('#showProp').attr('disabled', 'disabled');
    $('#responde').text('');
    var priList = [
        document.getElementById('range1').value,
        document.getElementById('range2').value,
        document.getElementById('range3').value,
        document.getElementById('range4').value,
    ];
    var price = document.getElementById('price').value;
    console.log('Odpowiedzi: ' + ansList);
    console.log('Priorytety: ' + priList);
    console.log('Cena: ' + price);
    $('#showProp').text("Trwa szukanie, poczekaj proszę.");
    $.post({
        url: 'getData',
        data: {
            'butt': JSON.stringify(ansList),
            'prio': JSON.stringify(priList),
            'pric': price,
        },
        success: function (response) {
            $('#imgLoading').css({'display': 'none'});
            $('#responde').text('');
            console.log('Wysłano agentów.');
            console.log(response);
            //window.location = '#responde';
            $('#showProp').removeAttr('disabled');
            $('#showProp').text("Wyszukiwanie zakończone. Powtórzyć?");
            var wynik = response.response;
            console.log(wynik);
            var count = wynik.length;
            console.log(count);
            var wynikInHtml = '<table><thead>' +
                '<th>Nr</th>' +
                '<th>Model</th>' +
                '<th>Typ</th>' +
                '<th>Waga</th>' +
                '<th>CPU</th>' +
                '<th>GPU</th>' +
                '<th>Bateria</th>' +
                '<th>dB</th>' +
                '<th>Cena</th>' +
                '<th>Procesor</th>' +
                '<th>Grafika</th>' +
                '</thead><tbody>';
            for (var x = 0; x < count; x++) {
                wynikInHtml += '<tr>';
                for (var y = 0; y < wynik[x].length; y++) {
                    if (y == 0) {
                        wynikInHtml += '<td>' + x + '</td>';
                    } else if (y == 1) {
                        wynikInHtml += '';
                    } else if (y == 2) {
                        wynikInHtml += '<td>' + wynik[x][y] + '</td>';
                    } else {
                        wynikInHtml += '<td>' + wynik[x][y] + '</td>';
                    }
                }
                wynikInHtml += '</tr>';
            }
            wynikInHtml += '</tbody></table>';
            $('#responde').html(wynikInHtml);
            // $('#responde').text(response.response);
        },
        error: function (error) {
            $('#showProp').text("Coś poszło nie tak. Powtórzyć?");
            console.log('Coś poszło nie tak.');
            $('#showProp').removeAttr('disabled');
            $('#imgLoading').css({'display': 'none'});
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
    switch (ran) {
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
