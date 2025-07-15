/* Написать функцию, которая сравнивает, равны ли два массива поэлементно */

function comparisen(a,b) {
    console.log(`COMPARISEN`)
    console.log(`interface start`)
    console.log(a,b)
    console.log(a.length,b.length)
    console.log(comparisen.length)
    console.log(`interface end`)

    if (a.length==b.length) {
        console.log(`Массивы ${a} и ${b} равны`)
    } else {
        console.log(`Массивы ${a} и ${b} не равны`)
    }
}

// console.log([1,2,3],[1,2,3])
// console.log([1,2],[8,6,[2]])

comparisen([1,2,3],[1,2,3])
comparisen([1,2],[8,6,[2]])