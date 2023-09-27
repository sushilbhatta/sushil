// / TODO: Select all elements needed
//    Use the HTML to figure out what classes/ids will work best for selecting each element
const form = document.querySelector("#form");
const username = document.querySelector("#username");
const password = document.querySelector("#password");
// const rememberPassword = document.querySelector("#remember");

form.addEventListener("submit", (e) => {
  // e.preventDefault();   
  loginValidation();
});

function setError(element, errorMessage) {
  const inputControl = element.parentElement;
  const errorDisplay = inputControl.querySelector(".error");
  errorDisplay.innerText = errorMessage;
  inputControl.classList.add("error");
  inputControl.classList.remove("success");
}

function setSuccess(element) {
  const inputControl = element.parentElement;
  const errorDisplay = inputControl.querySelector(".error");
  errorDisplay.innerText = "";
  inputControl.classList.add("success");
  inputControl.classList.remove("error");
}

const loginValidation = () => {
  if (username.value === "") {
    setError(username, "username is required");
  } else {
    setSuccess(username);
  }

  if (password.value === "") {
    setError(password, "password is required");
  }else {
    setSuccess(password);
  }
};


