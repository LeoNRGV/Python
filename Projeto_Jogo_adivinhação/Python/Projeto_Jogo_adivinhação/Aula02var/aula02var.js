var nome = "Ana";
console.log(nome); 

var altura = 5;
var comprimento = 7;

var area;
area = altura * comprimento;
console.log(area)




////////////////////////////////////////////////////
let idade = 25;
console.log(idade);

let forma = "retangulo";
let altura = 5;
let comprimento = 7;
let area;

if (forma === 'retangulo') {
    area = altura * comprimento;
}  else{
    area = (altura * comprimento) / 2;
}
console.log(area)


////////////////////////////////////////////////////
const PI = 3.14;
console.log(PI); // 3.14

const forma1 = "triangulo";
const altura = 5;
const comprimento = 7;
let area;

if (forma === 'quadrado') {
    area = altura * comprimento;
}  else{
    area = (altura * comprimento) / 2;
}

/////////////////////////////////////////////////////
console.log(area)

const a = 5, b = 10;
console.log(a == b);
console.log(a === 5);
console.log(a != b);
console.log(a !== 5);
console.log(a > b);
console.log(a < b);
console.log(a >= 5);
console.log(a <= 10);

let idade1 = 20;
let status = idade >= 18 ? "adulto" : "menor";
console.log(status);

let nome1 = "joão";
const saudação = `Olá, ${nome}!`;
console.log(saudação);