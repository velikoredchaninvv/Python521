
function check(){ // начало блока
    // console.log(age.valueAsNumber)
    age_from_range = age.valueAsNumber


// if (age_from_range >=7) {
//     console.log('Школьник')
//         if (age_from_range >= 18) {
//             console.log('Студент')
//         }
//             if (age_from_range >= 24) {
//                 console.log('Трудящийся')
//             }
//                 if (age_from_range >= 65) {
//                     console.log('Ветеран')
//                 }
// } else {
//     console.log('Дошкольник')
// }

if (age_from_range >=7) { // Начало if мультиблока
    if (age_from_range <= 18) {
        console.log('Школьник')
        }
        if (age_from_range >=19 && age_from_range <= 25) {
            console.log('Студент')
            }
            if (age_from_range >= 26 && age_from_range <= 65) {
                console.log('Человек труда') 
                }
                if (age_from_range >= 66) {
                        console.log('Веетран труда')
                        }

} else { // завершение if мультиблока
    console.log('Дошкольник')
}

} // завершение блока