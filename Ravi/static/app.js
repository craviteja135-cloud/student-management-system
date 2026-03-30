document.addEventListener("DOMContentLoaded", function () {
  
  const form = document.getElementById("studentform");
  const saveBtn = document.getElementById("btnsave");

  if (!form) return;

  form.addEventListener("submit", function (e) {
    const name = document.getElementById("nametxt").value.trim();
    const course = document.getElementById("coursetxt").value.trim();
    const college = document.getElementById("collegetxt").value.trim();
    const email = document.getElementById("emailtxt").value.trim();
    const phone = document.getElementById("phone").value.trim();

    if (name.length < 3) {
      alert("Name should be atleast 3 characters");
      e.preventDefault();
      return;
    }

    if (!email.includes("@") || !email.includes(".")) {
      alert("Plz enter Email correctly");
       e.preventDefault();
      return;
    }

    if (phone.length !== 10 || isNaN(phone)) {
      alert("Phone Number should be 10 digits...");
       e.preventDefault();
      return;
    }

    saveBtn.disabled = true;
    saveBtn.innerText = "Saving...";

    form.submit();
  });

});