function validateForm() {
    let name = document.getElementById("name").value;
    let age = document.getElementById("age").value;
    let email = document.getElementById("email").value;
    let phone = document.getElementById("phone").value;

    if (name === "" || age === "" || email === "" || phone === "") {
        alert("All fields are required!");
        return false;
    }

    if (age < 1) {
        alert("Age must be valid!");
        return false;
    }

    if (phone.length < 10) {
        alert("Enter a valid phone number!");
        return false;
    }

    alert("Form submitted successfully!");
    return true;
}

// Search doctors
document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.createElement("input");
    searchInput.placeholder = "Search doctor...";
    searchInput.classList.add("search-box");
    document.body.insertBefore(searchInput, document.body.children[1]);

    const cards = document.querySelectorAll(".card");

    searchInput.addEventListener("keyup", function () {
        const value = searchInput.value.toLowerCase();

        cards.forEach(card => {
            const text = card.innerText.toLowerCase();

            if (text.includes(value)) {
                card.style.display = "block";
            } else {
                card.style.display = "none";
            }
        });
    });
});

// Hover animation
const cards = document.querySelectorAll(".card");
cards.forEach(card => {
    card.addEventListener("mouseenter", () => {
        card.style.transform = "scale(1.05)";
        card.style.transition = "0.3s";
    });

    card.addEventListener("mouseleave", () => {
        card.style.transform = "scale(1)";
    });
});

// Register button action
const registerBtn = document.querySelector(".btn");
if (registerBtn) {
    registerBtn.addEventListener("click", () => {
        alert("Redirecting to registration page...");
    });
}

