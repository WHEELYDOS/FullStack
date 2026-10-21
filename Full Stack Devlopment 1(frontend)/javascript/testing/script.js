
var counter = 0;
var min = 15;

setInterval(() => {
    counter -= 1;

    if (counter <= 0) {
        counter = 60;
        min -= 1;
    }

    console.log(min + ":" + counter + " have passed");

    document.getElementById("counter").textContent =
        min + ":" + String(counter).padStart(2, "0") + " have passed";

}, 1000);
