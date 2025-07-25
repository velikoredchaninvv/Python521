// Создаю поле для вопроса
const questionElement = document.createElement("input")
questionElement.type = "text"
questionElement.id = "questId"
questionElement.placeholder = "Столица Англии?"
questionElement.value = ""

const createQuest = document.getElementById("div_for_program")
createQuest.appendChild(questionElement)


// Создаю кнопку
const buttonElement = document.createElement("input")
buttonElement.type = "button"
buttonElement.value = "Нажми"
buttonElement.onclick = pushQuestion

const createButton = document.getElementById("div_for_program")
createButton.appendChild(buttonElement)


// Создаю таблицу
const tablecreate = document.createElement("table")
const tableRow1 = document.createElement("tr") // создаю строку
const tableRow2 = document.createElement("tr") // создаю строку

const column1 = document.createElement("td")
const column2 = document.createElement("td")
const column3 = document.createElement("td")

column1.textContent = ""
column2.textContent = ""
column3.textContent = ""

tableRow1.appendChild(column1)
tableRow1.appendChild(column2)
tableRow1.appendChild(column3)

// tableRow2.textContent = "ХоХо" // Создаю новую строку

// Варианты вопросов и ответов
let otvet = ["Лондон", "Москва", "Киров"]
let vopros = ["Столица Лондона", "Столица России?", "Столица Кировской области?"]

let i = 0

// Реакция на нажатие кнопки
function pushQuestion(){

    column1.textContent = vopros[i]
    column2.textContent = otvet[i]

    if (questionElement.value === otvet[i]) {
        column3.textContent = "Правильно"
    } else {
        column3.textContent = "Не правильно"
    }

    i++

    if(i<vopros.length){
        questionElement.placeholder = vopros[i]
        column1.textContent = vopros[i-1]
        column2.textContent = questionElement.value
    }
    questionElement.placeholder = voprops[1]
}


// Публикую табницу
tablecreate.appendChild(tableRow1)
// tablecreate.appendChild(tableRow2) // создаю новую строку

const tableNew = document.getElementById("div_for_table")
tableNew.appendChild(tablecreate)

console.log("Table connet...")