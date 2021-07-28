const nameVerifier = (name)=>{
    name = name.toLowerCase();
    if(name==='socrates'){
        console.log(name+' is a mortal');
        return true;
    }else{
        console.log(name + ' is not a mortal')
        return false;
    }
}

console.log(nameVerifier('socrates'))