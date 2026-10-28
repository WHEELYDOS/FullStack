
let result = document.getElementById("result");

function play(user) {
    let choices = ["Rock", "Paper", "Scissors"];
    let computer = choices[Math.floor(Math.random() * 3)];

    if (user === computer) {
        result.innerText = "Draw! Computer chose " + computer;
    } else if (
        (user === "Rock" && computer === "Scissors") ||
        (user === "Paper" && computer === "Rock") ||
        (user === "Scissors" && computer === "Paper")
    ) {
        result.innerText = "You Win! Computer chose " + computer;
    } else {
        result.innerText = "You Lose! Computer chose " + computer;
    }
}

document.getElementById("rock").onclick = () => play("Rock");
document.getElementById("paper").onclick = () => play("Paper");
document.getElementById("scissors").onclick = () => play("Scissors");
