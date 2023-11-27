function moveProgressBar() {
  const executeButton = document.getElementById("executeButton");
  executeButton.disabled = true;
  const progressBar = document.getElementById("myBar");
  const progresBarText = progressBar.querySelector(".progress-bar-text");
  let percent = 0;
  progressBar.style.width = percent + "%";
  progresBarText.textContent = percent + "%";

  let progress = setInterval(function () {
    if (percent >= 100) {
      clearInterval(progress);
      executeButton.disabled = false;
      alert("fin");
    } else {
      percent = percent + 10;
      progressBar.style.width = percent + "%";
      progresBarText.textContent = percent + "%";
    }
  }, 1000);
}
