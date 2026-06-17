const buttons = document.querySelectorAll(".card");

buttons.forEach(button => {
  button.addEventListener("click", () => {
    console.log(`${button.innerText.split("\n")[0]} button clicked`);
  });
});