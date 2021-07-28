var men = [];
var name = 'Socrates';
var socrates = 'man';

console.log('All men are mortals');
men.push(socrates);
if(men[men.length -1] ==='man'){
    console.log(name + ' is a ' + socrates);
    console.log('Therefore, '+name+' is mortal');
}else{
    console.log(name + ' is a ' + socrates);
    console.log('Therefore, '+name+' is not mortal');
}
