<div align='center'>

## System wieloagentowy

### Temat:
Doradca zakupu sprzętu komputerowego ( Tablet / Laptop / PC )

Aleksander Sinkowski
</div>
<div align="justify">

### Opis:
* Projekt powstał na potrzeby zajęć.
* W czym pisać? W Pythonie i Flasku.
* Całość będzie śmigała web'owo.
* System wyświetli listę pytań oraz gotowych odpowiedzi. 
* Po interakcji z użytkownikiem, zbierze informacje i ustali jaki zakres parametrów przydzielić agentom.

__Pomysł 1:__ Odpowiedź na pytanie ustali jakieś wytyczne dla agenta na zasadzie jedno pytanie, jeden agent. Jest około 6 pytań, więc na poszukiwania wyruszy 6 agentów. Gdy wybiorą sobie jakiś sprzęt to porównają z innymi agentami, tym samym zmieniając parametry odnośnie różnić we wskazówkach. Odbędzie się to na zasadzie przyjęcia parametru z wybranego sprzętu i skorygowanie wartości. Np. gtx 760 to za mało więc ustawia sobie agent parametr na lepsze niż gtx 760 i wraca szukać dalej. Gdy znajdzie, skieruje się do następnego agenta po kolejną korektę. Prawdopodobnie w ten sposób wielu agentów przedstawi różne propozycje. Przydałby się system wag. Mógłby działać na zasadzie podnoszenia ważności parametru, gdy owy parametr powtarza się u innego agenta.

__Pomysł 2:__ Każde pytanie ustala jeden parametr priorytetorwy dla jednego agenta, po czym agenci szukający zgłaszają się do agentów bazodanowych podając swój priorytet. Każdy agent szukający dostanie propozycję w odpowiedzi, a agent bazodanowy dopisze sobie do wskazówek priorytet agenta szukającego. Tym sposobem kolejni agenci szukający dostaną inne, bardziej precyzyjne wedle wytycznych użytkownika propozycje.

Parametr, np. cena : waga od 1 do 5

Cena `do 2000zł` : warunek powtórzył się 3x więc `waga 3`
* ...

</div>
