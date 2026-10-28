// Guess the correct number between 1 and 100.
//  If the guess is too low, say “Higher!” If the guess is too high, 
// say “Lower!” Keep giving hints until the correct number is guessed.
// Only 7 chances will be given to the user 

let secretNumber = Math.floor(Math.random() * 100) + 1;
let attempts = 0;
const maxAttempts = 7;
let gameOver = false;

const guessInput = document.getElementById("guessInput");
const guessBtn = document.getElementById("guessBtn");
const message = document.getElementById("message");
const attemptsDisplay = document.getElementById("attempts");
const restartBtn = document.getElementById("restartBtn");

guessBtn.addEventListener("click", function () {
    if (gameOver) return;

    const guess = Number(guessInput.value);

    if (guessInput.value === "" || guess < 1 || guess > 100) {
        message.textContent = "Enter a number between 1 and 100!";
        return;
    }

    attempts++;
    attemptsDisplay.textContent = attempts;

    if (guess === secretNumber) {
        message.textContent = "Correct! You won!";
        gameOver = true;
    } else if (attempts === maxAttempts) {
        message.textContent =
            `Game Over! The number was ${secretNumber}.`;
        gameOver = true;
    } else if (guess < secretNumber) {
        message.textContent = "Higher!";
    } else {
        message.textContent = "Lower!";
    }

    if (gameOver) {
        guessInput.disabled = true;
        guessBtn.disabled = true;
    } else {
        guessInput.value = "";
        guessInput.focus();
    }
});
