document.addEventListener("DOMContentLoaded", function () {
  // Active nav based on current page
  const currentPage = window.location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-link").forEach(link => {
    const linkPage = link.getAttribute("href");
    if (linkPage === currentPage) {
      link.classList.add("active");
    } else {
      link.classList.remove("active");
    }
  });

  // Destination search
  const searchInput = document.getElementById("destinationSearch");
  const items = document.querySelectorAll(".destination-item");

  if (searchInput && items.length > 0) {
    searchInput.addEventListener("input", function () {
      const value = this.value.toLowerCase().trim();

      items.forEach(item => {
        const name = item.getAttribute("data-name");
        if (name.includes(value)) {
          item.style.display = "block";
        } else {
          item.style.display = "none";
        }
      });
    });
  }

  // Contact form validation
  const form = document.getElementById("contactForm");
  const successBox = document.getElementById("formSuccess");

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();

      const name = document.getElementById("name");
      const email = document.getElementById("email");
      const subject = document.getElementById("subject");
      const message = document.getElementById("message");

      let valid = true;

      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

      if (!name.value.trim()) {
        name.classList.add("is-invalid");
        valid = false;
      } else {
        name.classList.remove("is-invalid");
        name.classList.add("is-valid");
      }

      if (!emailPattern.test(email.value.trim())) {
        email.classList.add("is-invalid");
        valid = false;
      } else {
        email.classList.remove("is-invalid");
        email.classList.add("is-valid");
      }

      if (!subject.value.trim()) {
        subject.classList.add("is-invalid");
        valid = false;
      } else {
        subject.classList.remove("is-invalid");
        subject.classList.add("is-valid");
      }

      if (!message.value.trim()) {
        message.classList.add("is-invalid");
        valid = false;
      } else {
        message.classList.remove("is-invalid");
        message.classList.add("is-valid");
      }

      if (valid && successBox) {
        successBox.classList.remove("d-none");
        form.reset();
        document.querySelectorAll(".is-valid").forEach(el => el.classList.remove("is-valid"));
      }
    });
  }
});