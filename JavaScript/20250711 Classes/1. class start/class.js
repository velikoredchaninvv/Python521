class MyClass {
    constructor(param1,param2) {
    this.property1 = param1
    this.property2 = param2
}
}

// Экземляры класса
const myInstance = new MyClass("Значение 1", 123)

console.log(myInstance.property1)
console.log(myInstance.property2)