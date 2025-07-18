const tablecreate = document.createElement("table")
const tableRow = document.createElement("tr") // создаю строку

const column1 = document.createElement("td")
const column2 = document.createElement("td")
const column3 = document.createElement("td")

column1.textContent = "Ответ 1"
column2.textContent = "Ответ 2"
column3.textContent = "Ответ 3"

tableRow.appendChild(column1)
tableRow.appendChild(column2)
tableRow.appendChild(column3)

tablecreate.appendChild(tableRow)

const tableNew = document.getElementById("div_for_table")
tableNew.appendChild(tablecreate)

console.log("Table connet...")