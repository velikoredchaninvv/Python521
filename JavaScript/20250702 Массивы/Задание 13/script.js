/* 13. Дан массив имен студентов. Вывести в консоль самое короткое имя */

let a = ['СанСаныч', 'ПетроБродский', 'СамуилГарсон', 'НасмотренныйБрундук', 'ПетропавлоскаяКрепостьСтреляла']

for (i=0;i<a.length;i++){
    b = a.reduce(
        (accumulator, currentValue) => accumulator + currentValue,
        initialValue
      );

    console.log(b)
}

/* тут не разобрался */