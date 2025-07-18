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
const tableRow = document.createElement("tr") // создаю строку

const column1 = document.createElement("td")
const column2 = document.createElement("td")
const column3 = document.createElement("td")

column1.textContent = ""
column2.textContent = ""
column3.textContent = ""

tableRow.appendChild(column1)
tableRow.appendChild(column2)
tableRow.appendChild(column3)

// Варианты вопросов и ответов
let otvet = ["Лондон", "Москва", "Киров"]
let vopros = ["Столица Лондона?", "Столица России?", "Столица Кировской области?"]

let i = 0

// Реакция на нажатие кнопки
function pushQuestion(){

    column1.textContent = vopros[i]
    column2.textContent = otvet[i]

    for(i=0;i<=2;i++){
        // questionElement.placeholder = "Столица России?"
        column1.textContent = questionElement.placeholder
        column2.textContent = questionElement.value
            if (questionElement.value === "Лондон") {
                column3.textContent = "Правильно"
            } else {
                column3.textContent = "Не правильно"
            }
    } questionElement.placeholder = voprops[i]
}


// Публикую табницу
tablecreate.appendChild(tableRow)

const tableNew = document.getElementById("div_for_table")
tableNew.appendChild(tablecreate)

console.log("Table connet...")