class WakeUp {
    constructor(time, eye){
        this.time = time
        this.eye = eye
    }
}

let wake = new WakeUp(5,1)

if (wake.eye>0) {
    console.log(`I'm open my eye in ${wake.time}`)
} else {
    console.log(`I'm sleeping`)
}