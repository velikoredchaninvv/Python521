let arr = [2, 4, 6, 8, 333, 55, 77]
let brr = [2, 4, 6, 8, 333, 55, 77]
let crr = [2, 4, 66, 7]

/* Ниже разобрался с массивами
for (let viewtwo in brr) {
    console.log(viewtwo)
}

for (let view of brr) {
    console.log(view)
}
*/

// Проверить, равны ли массивы arr, brr
/*
for (arr in brr) {
    console.log('Равны')
} console.log('В массиве arr значения ${arr}, а в массиве brr значения ${brr}')
*/
// Проверить, равны ли массивы arr, crr

/*
Сравниваем количество элементов в массивах
Пока количество элементов не достигло длины массива 1
И пока количество элементов массива 1 совпадает с количеством элементов массива 2
Цикл продолжается

Если цикл выполнен, и условия верны то мы пишем что циклы совпадают

Если цикл не выполнен, то пишем что количество элементов в массивах разные;
*/

// for (i=0; i < arr[i] && arr[i] == brr[i]; i++) {
//     console.log('Равны')
// }

// for (i=0; i < arr[i] && arr[i] == brr[i]; i++) {
//     console.log('Равны')
// }

/* Главное решение
let check
if (arr.length == crr.length) {
    console.log('Равны')
} else {
    console.log('Не равны')
    //  Знаем что не равны, нужно посчитать на каком номере элемента происходит разрыв;
    for (i=0; arr[i]==crr[i]; i++) {
        check = i
        if (arr[i]!=crr[i]) {
            break
            console.log('Проверка')
        }
    }
} console.log(check)
*/


let my_car = {
    speed: 97,         // km /h
    color: 'red',
}
let your_car = {
    speed: 97,         // km /h
    color: 'red',
}
let bus = {
    speed: 43,         // km /h
    color: 'red',
}

//Проверить, равны ли моя и твоя машины

console.log(my_car==your_car)

// Проверить, равна ли моя машина автобусу
