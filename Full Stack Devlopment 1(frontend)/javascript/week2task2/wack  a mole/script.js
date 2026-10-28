let score = 0;
let active = 0;
let game;

function hit(n) {
    if (n == active) {
        score++;
        document.getElementById("score").innerText = score;
        active = 0;
    }
}
function startGame() {
    clearInterval(game);
    score = 0;
    let time = 30;
    active = 0;
    document.getElementById("score").innerText = score;
    document.getElementById("time").innerText = time;
    game = setInterval(function () {
        if (time <= 0) {
            clearInterval(game);
            active = 0;
            alert("Game Over! Your score: " + score);
            return;
        }
        time--;
        document.getElementById("time").innerText = time;
        active = Math.floor(Math.random() * 9) + 1;
        for (let i = 1; i <= 9; i++) {
            document.getElementById(i).innerText = "";
        }
        document.getElementById(active).innerText = "0";
    }, 800);
}
