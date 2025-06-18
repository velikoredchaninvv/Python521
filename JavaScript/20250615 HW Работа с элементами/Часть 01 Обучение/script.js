// Задание 1 Добавить в html 2 абзаца
// // Для создания элемента вызываем
// let p = document.createElement('p')
// // Для прикрепления элемента вызываем
// document.body.appendChild(p)
// p.textContent = 'Текст вашего абзаца'
// p = document.createElement('p')
// document.body.appendChild(p)
// p.textContent='Текст другого абзаца'

// Задание 2 Добавить в html 2 заголовка
// let h2 = document.createElement('h2')
// document.body.appendChild(h2)
// h2.textContent = 'Заголовок 1'
// h2 = document.createElement('h2')
// document.body.appendChild(h2)
// h2.textContent = 'Заголовок 2'

// Пример с тегом
// console.log(first_name.value)

// Прикрепление одного готового элемента внутрь другого
// let ol = document.createElement('ol')
// document.body.appendChild(ol)

// let li = document.createElement('li')
// ol.appendChild(li)
// li.textContent='Текст элемента списка'

// li = document.createElement('li')
// ol.appendChild(li)
// li.textContent='Текст второго элемента списка'

// Задание 2: Создание неупорядоченного списка, содержащего 2 элемента;
// let ul = document.createElement('ul')
// document.body.appendChild(ul)

// let li = document.createElement('li')
// ul.appendChild(li)
// li.textContent='Пункт один'

// li = document.createElement('li')
// ul.appendChild(li)
// li.textContent='Пункт два'

// Задание 3 Повышенной сложности: Создайте таблицу из одной строки и двух ячеек.
// Добавьте CSS, что бы было видно края таблицы

let table = document.createElement('table')
document.body.appendChild(table)

let tr = document.createElement('tr')
document.body.appendChild(tr)

let td = document.createElement('td')
tr.appendChild(td)
td.textContent='Ячейка 01'

td = document.createElement('td')
tr.appendChild(td)
td.textContent='Ячейка 02'