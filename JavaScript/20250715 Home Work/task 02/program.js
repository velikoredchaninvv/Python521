//напишите функцию, выбирающую наименьшее из всех переданных фунцкии чисел, используя только ветвление и цикл. Нажмите на название задания, чтобы показать ответ.

function sMin(a,b,c){
    if(arguments.length === 0){
        return undefined;
    }

    let min = arguments[0]
    for(i=1;i<arguments.length;i++){
        if(arguments[i]<min) {
            min=arguments[i]
        }
    }
    return min;
}

console.log(sMin(123,41,1243))