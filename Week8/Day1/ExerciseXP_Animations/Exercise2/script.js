const box = document.getElementById('animate');

function myMove() {
    let counter = 0;
    let idInterval = setInterval(function() {
        if (counter === 350) {
            clearInterval(idInterval)
        } else {
            box.style.left = counter + 'px';
            counter ++;
        }
    }, 5)
}

