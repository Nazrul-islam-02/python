function sum(a,b){
console.log(a+b)
}

function outer(func){

    return function (a,b){
        func(a,b)
        console.log(a-b)
    }

}

result = outer(sum)

result(10,15)

