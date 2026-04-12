// Event Submit by Form
document.getElementById('registrationForm').addEventListener('submit', function(event) {
    // Prevent the website from reloading when you click the button.
    event.preventDefault();

    // Lấy giá trị từ các ô input
    const name = document.getElementById('fullName').value;
    const email = document.getElementById('userEmail').value;
    
    let isValid = true;

    // Name Validation (must not be empty)
    if (name.trim() === "") {
        document.getElementById('nameError').style.display = 'block';
        isValid = false;
    } else {
        document.getElementById('nameError').style.display = 'none';
    }

    // Email Validation (must contain '@')
    if (!email.includes("@")) {
        document.getElementById('emailError').style.display = 'block';
        isValid = false;
    } else {
        document.getElementById('emailError').style.display = 'none';
    }

    // If both validations pass, show success message
    if (isValid) {
        document.getElementById('registrationForm').style.display = 'none';
        document.getElementById('successMessage').style.display = 'block';
        console.log("Form submitted successfully for:", name);
    }
});