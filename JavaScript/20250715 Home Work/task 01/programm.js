function fn(a,b,c){
    if (a>b){
        if(b>c){
            return c
        } else {
            return b
        }
    } else {
        if(c>a){
            return a
        } else {
            return c
        }
    }
}

console.log(`Меньшее число ${fn(15,17,7)}`)