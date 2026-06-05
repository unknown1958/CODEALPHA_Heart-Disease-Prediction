const form = document.getElementById("contactForm");
const statusEl = document.getElementById("formStatus");

const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const messageInput = document.getElementById("message");

const nameError = document.getElementById("nameError");
const emailError = document.getElementById("emailError");
const messageError = document.getElementById("messageError");

// Basic client-side validation (nice bonus for the “Form Validation” bullet) [web:33][web:42]
function validateForm() {
  let ok = true;

  // reset errors
  nameError.textContent = "";
  emailError.textContent = "";
  messageError.textContent = "";
  statusEl.textContent = "";
  statusEl.className = "form-status";

  if (!nameInput.value.trim()) {
    nameError.textContent = "Name is required.";
    ok = false;
  }

  if (!emailInput.value.trim()) {
    emailError.textContent = "Email is required.";
    ok = false;
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailInput.value.trim())) {
    emailError.textContent = "Please enter a valid email.";
    ok = false;
  }

  if (!messageInput.value.trim()) {
    messageError.textContent = "Message is required.";
    ok = false;
  }

  return ok;
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  if (!validateForm()) return;

  const payload = {
    name: nameInput.value.trim(),
    email: emailInput.value.trim(),
    message: messageInput.value.trim()
  };

  try {
    statusEl.textContent = "Submitting...";
    statusEl.className = "form-status";

    const res = await fetch("/api/contact", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    const data = await res.json();

    if (res.ok && data.success) {
      statusEl.textContent = data.message || "Form Submitted Successfully";
      statusEl.className = "form-status form-status--success";
      form.reset();
    } else {
      statusEl.textContent =
        data.message || "Something went wrong. Please try again.";
      statusEl.className = "form-status form-status--error";
    }
  } catch (err) {
    console.error(err);
    statusEl.textContent = "Unable to submit. Please check your connection.";
    statusEl.className = "form-status form-status--error";
  }
});