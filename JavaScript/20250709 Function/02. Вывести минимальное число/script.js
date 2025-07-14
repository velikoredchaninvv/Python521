function push(a,b,c) {
    a = 1
    b = 12
    c = 5

    if (a<b && a<c){
        console.log('Минимальное число а ', a, 'Проверка 1')
    } else if (b<a && b<c) {
        console.log('Минимальное число b ', b, 'Проверка 2')
    } else if (c<a && c<b) {
        console.log('Минимальное число c ', c, 'Проверка 3')
    }
}