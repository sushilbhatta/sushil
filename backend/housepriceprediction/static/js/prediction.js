document.addEventListener("DOMContentLoaded", function () {
  const customSelect = document.querySelector(".custom-select");

  // Toggle the dropdown when the select is clicked
  customSelect.addEventListener("click", function (e) {
    e.stopPropagation();
    customSelect.classList.toggle("open");
  });

  // Close the dropdown if clicked outside of it
  document.addEventListener("click", function (e) {
    if (!customSelect.contains(e.target)) {
      customSelect.classList.remove("open");
    }
  });
});
