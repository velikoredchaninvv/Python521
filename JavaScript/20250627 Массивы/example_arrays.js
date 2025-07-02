    // const subjects = ['HTML', 'CSS', 'JavaScript', 'Python', 'SQL', 'DbT', 'Django', 'Telegram-Bot'];
    // console.log('Первый предмет: ', subjects[0])
    // console.log('Самый сложный предмет: ', subjects[6])

    // const school_marks = [2, 3, 4, 5]
    // console.log('Лучшая оценка: ', school_marks[3])

    // let favourite_holidays = [
    //     new Date(2025, 11, 31),
    //     new Date(2025, 8, 1),
    //     new Date(2025, 7, 6)
    // ];

// Задание:
// [+] Создать массив чисел от 1 до 10 
// [+] Вручную, прописав каждую циферку
// [] Заменить в массиве все четные числа на числа в 100 раз больше
// [] [1, 200, 3, 400, ....., 800, 9]

const array = ['1','2','3','4','5','6','7','8','9','10']
let i
for (i=0; i<array.length; i++){
    if (array[i]%2==0) {
    array[i] *= 100;
    }
    console.log(array[i])
}