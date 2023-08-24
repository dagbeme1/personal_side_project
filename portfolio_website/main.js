// Add an event listener to smooth scroll to sections when navigation links are clicked
document.addEventListener("DOMContentLoaded", function () {
    // Select all navigation links in the document
    const navLinks = document.querySelectorAll("nav ul li a");

    // Loop through each navigation link
    navLinks.forEach(link => {
        // Add a click event listener to each link
        link.addEventListener("click", scrollToSection);
    });

    // Function to scroll to a section smoothly
    function scrollToSection(event) {
        // Prevent the default link behavior
        event.preventDefault();

        // Get the target section's ID from the link's href attribute
        const targetId = event.target.getAttribute("href");

        // Select the target section using its ID
        const targetSection = document.querySelector(targetId);

        // Scroll to the target section with smooth behavior
        window.scrollTo({
            top: targetSection.offsetTop,
            behavior: "smooth"
        });
    }
});

// Display a message when the contact form is submitted
document.querySelector("#contact form").addEventListener("submit", function (event) {
    // Prevent the default form submission
    event.preventDefault();

    // Display an alert to thank the user for contacting
    alert("Thank you for reaching out! I'll get back to you soon.");
});
