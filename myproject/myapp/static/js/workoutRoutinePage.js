var modal = document.getElementById("myModal");
var buttons = document.querySelectorAll(".addWorkout");
var span = document.getElementsByClassName("close")[0];
var selectedDay;

function openModal(day) {
  modal.style.display = "block";
  selectedDay = day;
}

function closeModal() {
  modal.style.display = "none";
  document.getElementById("workout").value = "";
  document.getElementById("numInput1").value = "";
  document.getElementById("numInput2").value = "";
}

buttons.forEach(function (button) {
  button.onclick = function () {
    openModal(button.id.replace("Btn", "") + "Col");
  };
});

span.onclick = closeModal;

window.onclick = function (event) {
  if (event.target == modal) {
    closeModal();
  }
};

var workoutInput = document.getElementById("workout");
var numInput1 = document.getElementById("numInput1");
var numInput2 = document.getElementById("numInput2");

var addButton = document.querySelector(".modal-content .addbtn .addWorkout");

addButton.onclick = function () {
  var workout = workoutInput.value;
  var sets = numInput1.value;
  var reps = numInput2.value;

  if (workout === "" || sets === "" || reps === "") {
    return;
  }

  var div = document.createElement("div");
  div.className = "workoutAdding";
  div.id = "block";

  var closeBtn = document.createElement("span");
  closeBtn.className = "removeWorkout";
  closeBtn.innerHTML = "&times;";
  div.appendChild(closeBtn);

  div.innerHTML +=
    "<p>" + workout + "</p><p>" + sets + " sets of " + reps + " reps</p>";

  document.getElementById(selectedDay).appendChild(div);

  closeModal();
};

document.addEventListener(
  "click",
  function (event) {
    if (!event.target.matches(".removeWorkout")) return;
    event.stopPropagation();
    event.target.parentElement.remove();
  },
  false
);
