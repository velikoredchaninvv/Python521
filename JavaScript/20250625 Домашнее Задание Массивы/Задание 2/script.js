let array = ['Ася', 'Вася', 'Мася']

// Какой номер позиции имеет Ася?

for (let i = 0; i < array.length; i++) {
    if (array[i] === 'Ася') {
        console.log(`Номер позиции Ася ${i}`)
    }
}