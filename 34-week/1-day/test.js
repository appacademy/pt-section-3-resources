let mapperFunc = (el) =>{
    return el * 3
}
let arr = [1,2,3]

let mappedArr = arr.map(mapperFunc)

console.log(mappedArr)

let filterFunc = (el) =>{
    console.log("was I called?")
    return !(el % 2)
}

let evenNumbers = mappedArr.filter(filterFunc)
console.log(evenNumbers)
