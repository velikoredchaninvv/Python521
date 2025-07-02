function search() {
chislo = me.valueAsNumber // что ищем
array = [2,4,6,8,14,16,18]
left = 0
right = array.length-1
middle = -1

while (right - left > 1) {
    // ищем середину той части массива 
    middle = Math.floor((right+left)/2)
    if (chislo < array[middle]) {
        // Ищем влевой половине - сдвигаем правый край левее середины
        right = middle - 1
    } else {
        // Ищем вправой половине - сдвигаем левый край до середины
        left = middle
    }
    console.log(left, right)
}
}