class Sleep {
    constructor(time){
        this.time = time
        this.currentTime = 0
    }
    need_sleep(currentTime){
        this.currentTime = currentTime
    }
}

const my = new Sleep(22)
console.log(`Time for sleeping ${my.time}`)

my.need_sleep(24)
console.log(`Curret time ${my.currentTime}`)

if (my.currentTime > my.time) {
    console.log(`Need sleep`)
} else {
    console.log(`Let's go work`)
}