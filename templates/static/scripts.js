// scripts.js
document.addEventListener('DOMContentLoaded', function() {
    console.log("JavaScript is working!");

    //  Adding a simple click event to a button
    const addButton = document.querySelector('#add-button');
    if (addButton) {
        addButton.addEventListener('click', function() {
            alert("Add button clicked!");
        });
    }
});
