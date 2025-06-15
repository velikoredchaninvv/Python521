// 1. С помощью арифметических присваиваний просто арифметических операторов
// и инкремента и декремента (--) выполнить следующие преобразования:
// Создать переменную номер секунды (больше 30). Прибавить к ней 580 секунд.
// Не применяя ветвления (if), а только с помощью арифметики, сказать,
// сколько получилось минут и секунд?

// 2. Поставить вопросы компьютеру:

// 2.1 Правда ли, что 5800 секунд больше часа? Больше 2х часов?
// 2.2 Правда ли, что если цена составляет 230 рублей за штуку
//     и купили 27 штук, то хватит 500 рублей? 5000 рублей? 7000 рублей?
// 2.3 Правда ли, что 5000 рублей хватит, а 7000 НЕ хватит 
// (использовать отрицание, конъюнкцию и дизъюнкцию на свое усмотрение)

// НЕПРАВИЛЬНАЯ ДОМАШКА:
// console.log(6210 < 5000, 'ПРАВДА!')

// Задание #1
peremennaya_secundi = 60; // sec
constanta_vremeni = 580; // sec
minuti = (peremennaya_secundi + constanta_vremeni) / 60; // minut
secundi = (peremennaya_secundi + constanta_vremeni) % 60;
console.log('минуты ',Math.floor(minuti));
console.log('секунды ', secundi);

// Задание 2.1
odinchas = 60; // minut
chislo = 5800/60; // minut
if (chislo > odinchas) {
    console.log('Да, 5800 секунд больше часа');
}
else {
    console.log('Нет, 5800 секунд меньше часа');
}

odinchas2 = 120; // minut
chislo = 5800/60; // minut
if (chislo > odinchas2) {
    console.log('Да, 5800 секунд больше двух часов');
}
else {
    console.log('Нет, 5800 секунд меньше двух часов');
}

// Задание 2.2
shtuka = 230;
kolvo = 27;
summa = shtuka*kolvo;

if (summa > 500){
    console.log('Нет, 500 не хватит');
}
else {
    console.log('500 хватит');
}

if (summa > 5000){
    console.log('Нет, 5000 не хватит');
}
else {
    console.log('Похоже что 5000 хватит');
}

if (summa > 7000){
    console.log('Нет, 7000 не хватит');
}
else {
    console.log('Похоже что 7000 точно хватит');
}

// 2.3 Правда ли, что 5000 рублей хватит, а 7000 НЕ хватит 
// (использовать отрицание, конъюнкцию и дизъюнкцию на свое усмотрение)

a = 5000;
b = 7000;

// console.log(a||b);
// console.log(a&&b);
// Задача на False и True

// if (summa > 5000 && summa > 7000) {
//     console.log ();
// }

vopros1 = summa > 5000; // false
vopros2 = summa < 5000; // true
vopros3 = summa > 7000; // false
vopros4 = summa < 7000; // true

if (vopros1) {
    console.log('Правда, что 5000 хватит');
}
else {
    console.log('Неправда, 5000 не хватит');
}

if (vopros3) {
    console.log('Правда, что 7000 хватит');
}
else {
    console.log('Неправда, 7000 не хватит');
}

// otvet
// otvet = ;

// console.log('Правда ли, что 5000 рублей хватит, а 7000 НЕ хватит ',otvet);