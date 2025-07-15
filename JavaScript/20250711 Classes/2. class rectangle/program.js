class Rectangle {
    constructor(width, height) {
        this.width = width
        this.height = height
    }

    calculateArea() {
        return this.width * this.height
    }

    decribe() {
        console.log('Rectangle: width=${this.width}, height=${this.height}, area=${this.calculateArea()}')
    }

    icreaseWidth(amount) {
        this.width += amount
    }
}

const myRectangle = new Rectangle(10,5)

console.log("Area:", myRectangle.calculateArea())
myRectangle.decribe()

myRectangle.icreaseWidth(3)
myRectangle.decribe()