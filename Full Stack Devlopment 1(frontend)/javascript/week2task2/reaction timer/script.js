    let start;
    let interval;

    function startTimer() {
        clearInterval(interval);
        start = Date.now();

        interval = setInterval(function () {
            document.getElementById("timer").innerText =
                (Date.now() - start) + " ms";
        }, 10);
        
    }

    function stopTimer() {
        clearInterval(interval);
    }