var primeCounter;
var prime;
for(let num = 1; num<=100;num++){
    primeCounter=0;
    prime = false;
    if(num==1){
        console.log(num);
    }else{
    for(let i = 2; i<=100;i++){
        if(num==i){
            continue;
        }else if(num%i==0){
            primeCounter++;
        }
    }
    if(primeCounter==0){
        console.log('Prime');
        prime = true;
    }
    if(prime == false){
        if(num%3==0 && num%5==0){
            console.log('FizzBuzz');
        }else if(num%3==0){
            console.log('Fizz');
        }else if(num%5==0){
            console.log('Buzz')
        }else{
            console.log(num);
        }
    }
    }
}