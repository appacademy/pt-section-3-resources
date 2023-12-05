// let mapperFunc = (el) =>{
//     return el * 3
// }
// let arr = [1,2,3]

// let mappedArr = arr.map(mapperFunc)

// console.log(mappedArr)

// let filterFunc = (el) =>{
//     console.log("was I called?")
//     return !(el % 2)
// }

// let evenNumbers = mappedArr.filter(filterFunc)
// console.log(evenNumbers)



let scoresArr = [90, 86, 75, 91, 62, 99, 88, 90]

let myFunc = (el) => {
    return el >= 90
}

let filterdArr = scoresArr.filter(myFunc)

// let filterdArr = scoresArr.filter(el => el >= 90)



console.log(filterdArr)
