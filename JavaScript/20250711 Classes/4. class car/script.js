class Car {
    constructor(carcolor, number_of_wheels, max_speed){
        this.carcolor = carcolor;
        this.number_of_wheels = number_of_wheels;
        this.max_speed = max_speed;
        this.currentSpeed = 0;
    }

    setSpeed(speed) {
        this.currentSpeed = speed
    }

    drive(hours) {
        this.hoursDrive = hours
    }
}

// нужно уможнить скорость на время в пути, так получу расстояние для движущегося автомобиля
// это возвращение метода, вычислние можно выполнить за границей объявленного класса

const myCar = new Car("yellow", 4, 120)

console.log(`Color of the car: ${myCar.carcolor}`)
console.log(`Speed of the car ${myCar.currentSpeed}`)

myCar.setSpeed(120)
console.log(`Speed of the car ${myCar.currentSpeed}`)