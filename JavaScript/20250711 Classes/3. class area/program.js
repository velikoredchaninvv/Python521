class cArea {
    constructor(height, width, side) {
        this.height = height
        this.width = width
        this.side = side
    }

        describe() {
            console.log(`The described object has a side property: ${this.side}, a height of: ${this.height}, and a width: ${this.width}`)
        }

        calculateArea() {
            return this.height * this.width * this.side
        }

}

const mobj = new cArea(3,7,9)
console.log(mobj.height, typeof mobj.height)
console.log(mobj.width, typeof mobj.width)
console.log(mobj.side, typeof mobj.side)

console.log(mobj.calculateArea())

console.log(mobj.describe())

// console.log(mobj.describe)

// const myObject = new Area(3,7,2)
// console.log(myObject.calculateArea())

// const test = 1
// console.log(tapeof test)