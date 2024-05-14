const inputNumber = parseFloat(prompt("Введите число"));
function isEven (number) { //function testing number is even or odd
    return number % 2 === 0; //checking the modulus after dividing a number by 2
    }
console.log(isEven (inputNumber)); //output to console

// Try to figure out why do you need use float  not int and why ?  Can you use int ? 
