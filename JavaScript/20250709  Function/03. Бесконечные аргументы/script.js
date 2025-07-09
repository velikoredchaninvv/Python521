let min

function func () {
    if (arguments[0]<=arguments[1] && arguments[0]<=arguments[2]) {
        min = arguments[0] 
    } else if (arguments[1]<=arguments[0] && arguments[1]<=arguments[2]) {
        min = arguments[1]
    } else if (arguments[2]<=arguments[0] && arguments[2]<arguments[1]) {
        min = arguments[2]
    }
}
func(5,3,12)
console.log(min)