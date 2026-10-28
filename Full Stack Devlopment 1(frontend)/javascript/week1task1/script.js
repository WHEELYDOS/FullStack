
let score = 0;
let currentQuestion = 0;

let questions = [
    "What does HTML stand for?",
    "Which keyword declares a variable in JavaScript?",
    "Which symbol is used for single-line comments?",
    "Which method prints output to the console?",
    "Which data type represents true or false?"
];

let answers = ["A", "B", "C", "C", "C"];

let question = document.getElementById("question");
let options = document.querySelectorAll(".option");
let scoreDisplay = document.getElementById("score");
let progress = document.getElementById("progress");
let selectedOption = document.getElementById("selectedOption");
let nextBtn = document.getElementById("nextBtn");

function showQuestion() {
    question.textContent = questions[currentQuestion];
    progress.textContent = "Q" + (currentQuestion + 1) + "/" + questions.length;
    selectedOption.textContent = "";
    
    options.forEach(function(option) {
        option.disabled = false;
    });
}

options.forEach(function(option) {
    option.addEventListener("click", function() {
        selectedOption.textContent = "Selected option: " + option.textContent;

        if (option.textContent === answers[currentQuestion]) {
            score++;
            scoreDisplay.textContent = "Score: " + score;
        }

        options.forEach(function(btn) {
            btn.disabled = true;
        });
    });
});

nextBtn.addEventListener("click", function() {
    if (currentQuestion < questions.length - 1) {
        currentQuestion++;
        showQuestion();
    } else {
        question.textContent = "Quiz Completed!";
        selectedOption.textContent = "Final Score: " + score;
        progress.textContent = "Q" + questions.length + "/" + questions.length;
        nextBtn.disabled = true;
    }
});

showQuestion();
