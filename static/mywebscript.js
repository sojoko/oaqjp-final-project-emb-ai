function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const output = document.getElementById("system_response");
    const query = new URLSearchParams({ textToAnalyze });
    const xhttp = new XMLHttpRequest();

    xhttp.onload = function () {
        output.textContent = xhttp.responseText;
    };
    xhttp.onerror = function () {
        output.textContent = "Unable to reach the server. Please try again.";
    };

    xhttp.open("GET", `emotionDetector?${query}`, true);
    xhttp.send();
}
