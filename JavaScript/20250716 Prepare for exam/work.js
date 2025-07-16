console.log("Начинается")

// div
function tam() {
    console.log(numinput.value)
    return numinput.value
}

// div
function answer() {
    console.log(`Там ${answerlink.value}`)
    return answerlink.value
}

// div
function listCreate(){
    let li = document.createElement('li')
    tble.appendChild(li)
    li.textContent=`Я тоже вижу значение ${answerlink.value}`
}

// div
function mylist(){
    let num = document.getElementById("mlist")
    if(num){
        for(i=answerlink.value; i>0; i--){
            console.log(i)
        }
    }
    
}