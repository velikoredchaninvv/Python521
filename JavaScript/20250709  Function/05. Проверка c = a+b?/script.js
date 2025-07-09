console.log('coonect... start')

function clck() {

    // Переменные Функции
    let nm01 = num01.valueAsNumber
    let nm02 = num02.valueAsNumber
    let nm03 = num03.valueAsNumber
    let sum

    sum = nm01+nm02

    // Условие

    if (sum == nm03) {
        console.log('Сумма чисел a + b равны c')
    } else {
        console.log('Сумма чисел a + b не равны c')
    }

    // Проверка входящего типа данных из value
    console.log(num01.value, typeof num01.valueAsNumber)
    console.log(num02.value, typeof num02.valueAsNumber)
    console.log(num03.value, typeof num03.valueAsNumber)
}