const container = document.getElementById('container');
const cols = container.querySelectorAll('.col');
const contents = container.querySelectorAll('.content');
const button = container.querySelector('button');
let player = 1;
let win = false;
let counter = 0;

document.addEventListener('click', selector);
button.addEventListener('click', deleteBoard);

function selector(e) {
    for (let i = 0; i < 9; i++) {
        
        /* Validate if the box available */
        if (e.target === cols[i]) {
            if (player === 1) {
                if (contents[i].innerText === '') {
                    contents[i].innerText = 'X';
                    contents[i].style.color = 'rgba(255,0,0,.7)';
                    player = 2;
                    counter++;
                }
            }else{
                if (contents[i].innerText === '') {
                    contents[i].innerText = 'O';
                    contents[i].style.color = 'rgba(0,0,0,.7)';
                    player = 1;
                    counter++;
                }
            }
        }
    }
    winnerChecker();
}

function winnerChecker() {
    
    /* Validate if the player won horizontally */
    for (let r = 0; r <= 6; r+=3) {
        if (contents[r].innerText !=='' && contents[r].innerText === contents[r+1].innerText && contents[r].innerText===contents[r+2].innerText) {
            win = true;
        }   
    }
    /* Validate if the player won vertically */
    for (let r = 0; r < 3; r++) {
        if (contents[r].innerText !=='' && contents[r].innerText === contents[r+3].innerText && contents[r].innerText===contents[r+6].innerText) {
            win = true;
        }   
    }
    /* Validate if the player won diagonally */
    if (contents[0].innerText !=='' && contents[0].innerText === contents[4].innerText && contents[0].innerText===contents[8].innerText) {
        win = true;
    }   
    if (contents[2].innerText !=='' && contents[2].innerText === contents[4].innerText && contents[2].innerText===contents[6].innerText) {
        win = true;
    }   
    if (win === true) {
        if (player === 1) {
            alert('O has won');
            deleteBoard();
        }else{
            alert('X has won');
            deleteBoard();
        }
    }
    if(counter === 9){
        alert('Cats game!');
        deleteBoard();
    }
}

function deleteBoard() {
    for (let i = 0; i < cols.length; i++) {
        let col = cols[i];
        let content = col.querySelector('.content');
        content.innerText = '';
    }
    win = false;
    counter = 0;
    document.addEventListener('click', selector);
}