function pognali() {
    console.log(fio.value)
    console.log(age.value)

    a = fio.value
    b = age.value

}

function add_kid() {
    let li = document.createElement('li')
    kids.appendChild(li)
    console.log(fio.value)
    li.textContent = 'Новый посетитель ' + fio.value + ' возраст ' + age.value
}