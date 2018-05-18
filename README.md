<div align='center'>

# System wieloagentowy

## Temat:
Doradca zakupu sprzętu komputerowego ( Tablet / Laptop / PC )

Aleksander Sinkowski

<div align="justify">

### 1.Opis:
* Projekt powstał na potrzeby zajęć.
* W czym pisać? W Pythonie i Flasku.
* Całość będzie śmigała web'owo.
* System wyświetli listę pytań oraz gotowych odpowiedzi.
* Po interakcji z użytkownikiem, zbierze informacje i ustali jaki zakres parametrów przydzielić agentom.

__:-1:Pomysł 1 (jeden typ agenta):__ Każde pytanie ustali jeden parametr priorytetowy dla dla jednego agenta, po czym agencie ruszą do poszukiwać. Po wybraniu sobie jakichś propozycji, agent zapamięta parametr (np. gtx 760), po którym będzie porównywał się do innych agentów, korygując tym samym swoje dane oraz uzupełniając niewiadome na zasadzie tworzenia zakresu. Przykładowo: agent nastawiony na sprzęt gameingowy przyjmie wartość energooszczędności, przez co będzie szukał wydajnej karty graficznej o niskim zapotrzebowaniu energii.

__:-1:Pomysł 2 (dwa typy agenta):__ Każde pytanie ustala jeden parametr priorytetowy dla jednego agenta, po czym agenci szukający zgłaszają się do agentów bazodanowych podając swój priorytet. Każdy agent szukający dostanie propozycję w odpowiedzi, a agent bazodanowy dopisze sobie do wskazówek priorytet agenta szukającego. Tym sposobem kolejni agenci szukający dostaną inne, bardziej precyzyjne wedle wytycznych użytkownika propozycje.

__:-1:Pomysł 3 (trzy typy agenta):__ Jak wyżej z tym, że będzie trzeci agent reprezentujący użytkownika rozdający parametry, po których agenci będą szukać propozycji. Po znalezieniu propozycji wrócą i zdadzą raport trzeciemu, gdzie ten wprowadzi modyfikację różne dla każdego agenta i wyśle ich raz jeszcze na poszukiwania optymalnych propozycji.

:warning: __:+1:Pomysł 4 (Tak powinno być):__ Na podstawie wybranych opcji agencie dostaną te same parametry i ruszą do agenta odpowiedzialnego za bazę danych. Agent bazodanowy będzie zmieniał swoje parametry tak by miał jak największy zyst z transakcji. Np. nauczył się, że agenci szukają sprzętu gameingowego więc próbuje wcisnąć droższy lub słabszy jak mu zalega na magazynie.

<pre>
        < "Poka towary" >
            (^ - ^)                  (^ - ^) < "Poka towary" >
                    \                /
          (^ - ^) ___\_             /  ______(^ - ^)
                        \          / /
           (^ - ^) ____  <( - u - )v  < "Oto moje towary" >
                       /          | \
      (^ - ^) ________/           |  \__ (^ - ^)
                                 /                              
           < "Poka towary" > (^ - ^)
</pre>

<div align="left">

### 2. Pytania i odpowiedzi:
| Pytanie | Opcja 1 | Opcja 2 | Opcja 3|
| - | - | - | - |
| 1. Jakiej wagi sprzęt? | Bardzo lekki | Do 3kg | Obojętnie |
| 2. Przeznaczenie? | Przeglądarka i dokumenty | Uniwersalny | PC Gaming Master Race |
| 3. Żywotność baterii? | Stawiam na długi czas pracy | Fajnie by było jakby na baterii wytrzymał co najmniej jeden film | Obojętnie |
| 4. Głośność pracy? | Cichy jak ninja | Niech mruczy aż miło | Obojętnie |
| 5. Cena? | Cena podana przez użytkownika | - | - |

### 3. Tabele wartości
| Pytanie | opcja 1 | opcja 2 | opcja 3 |
| - | - | - | - |
| 1. Jakiej wagi sprzęt? | Bardzo lekki | Do 3kg | Obojętnie |
|  | ~<1.5 | 1.5<3 | * |
| 2. Przeznaczenie? | Przeglądarka i dokumenty | Uniwersalny | PC Gaming Master Race |
|  | CPU 0 do 3000, GPU 0 do 3000 | CPU 3000 do 7000, GPU 3000 do 6000 | CPU 5000 do 100000, GPU 5000 do 100000 |
| 3. Żywotność baterii? | Stawiam na długi czas pracy | Fajnie by było jakby na baterii wytrzymał co najmniej jeden film | Obojętnie |
|  | więcej niż 5h | więcej niż 2h | więcej niż 0h |
| 4. Głośność pracy? | Cichy jak ninja | Niech mruczy aż miło | Obojętnie |
|  | do 30 dB | do 100 dB | do 100 dB |
| 5. Orientacja cenowa? | Cena | status | - |
|  | Podaje user | negocjacje | - |

Legenda:
- `-` none
- `*` wszystko
- `~` więcej/mniej

### 4. Pohandlujmy
#### Komunikacja agentów krok po kroku
* Agenci klienci mający identyczne parametry wysyłają żądanie z wartością reprezentującą typ urządzenia (np. gaming) do agenta sklepikarza.
* Agent sklepikarz ma jakieś swoje parametry, po których ustala jak szukać sprzętu "Gameingowego". Przykładowo przeszukuje wartości benchmark dla CPU i GPU, by wyciągnąć te większe od np. 5000 jednostek.
* Agent sklepikarz zwraca dane sprzętowe wybranego urządzenia.
* Agent klient sprawdza czy wartości, które otzrymał spełniają warunki jakie ustalił klient.
* Jeśli warunki nie zostały spełnione, agent klient wysyła żądanie, w którym informuje o warunku parametru o największym priorytecie. Np. jeśli cena to około 2000 i ma priorytet 5, to taki warunek zostanie przedstawiony sprzedawcy.
* Agent sprzedawca dodaje do sortowania nowy warunek i bardziej precyzyjnie wybiera kolejny sprzęt. Zwraca odpowiedź.
* Agent klient sprawdza ponownie czy sprzęt pasuje do wymagań. Jeśli nie to wysyła parametr kolejny o podobnym lub niższym priorytecie. I tak w kółko.
* Jeśli agent klient uzna, że sprzęt pasuje to zaczyna negocjować cenę ze sprzedawcą.
* Jak będą negocjować agenci? Nie wiem , _ ,
* Gdy agent klient uzna sprzęt za godny, sprawdza czy na liście takowy istnieje i jeśli nie to dorzuca.
* Ostatecznie lista jest wyświetlona użytkownikowi.
