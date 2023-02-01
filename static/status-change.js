console.log("script launched")

var badges = document.querySelectorAll('.status-badge__text');


// отслеживаем события кликов на элементах и возвращаем кликнутый
document.onclick = e => {
    var badges = document.querySelectorAll('.status-badge__text');
    return e.target, badges
}


function toggleButtons(e) {
    e.target.parentElement.classList.toggle("selected");
}


for (var i = 0 ; i < badges.length; i++) {
    badges[i].addEventListener('click' , toggleButtons);
}
