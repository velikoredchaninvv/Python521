class Man {
    constructor(age, weigh, name) {
        this.age = age
        this.weight = weigh
        this.name = name
        this.lifetime = 0
    }
    time_of_life(time){
        this.lifetime =+ time
    }
}

const nMan = new Man(39,75,'Slava')

console.log(`Age of the man ${nMan.age}`)
console.log(`Weight of the man ${nMan.weight}`)
console.log(`Name of the man ${nMan.name}`)

nMan.time_of_life(120)
console.log(`Time of life ${nMan.lifetime}`)