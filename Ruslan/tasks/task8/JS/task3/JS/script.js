const num1 = parseFloat(prompt("Введите число №1")); //variable for first input number, i use parseFloat for transformation string to float
const num2 = parseFloat(prompt("Введите число №2")); //variable for second input number
const num3 = parseFloat(prompt("Введите число №3")); //variable for third input number
if (num1 > num2 && num1 > num3) { //compare num1, num2 and num3
    console.log(num1); //if num1 is largest, it will be displayed
} else if (num2 > num1 && num2 > num3) { //compare num1, num2 and num3
    console.log(num2); //if num2 is largest, it will be displayed
} else if (num3 > num1 && num3 > num2) { //compare num1, num2 and num3
    console.log(num3); //if num3 is largest, it will be displayed
}
//  Almost correct . Not handle the case where two or all three numbers are equal.  How do you figure out  this issue 
