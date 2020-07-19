const div = document.querySelector("div");

const color1 = "salmon";
const color2 = "powderblue";

div.addEventListener("click", function (e) {
  //for check
  //   console.log(e.target.parentNode.nodeName);
  document
    .querySelectorAll("div")
    .forEach((div) => (div.style.backgroundColor = ""));
  if (e.target.parentNode.nodeName === "DIV") {
    e.target.parentNode.style.backgroundColor = color2;
  }
  e.target.style.backgroundColor = color1;
});
