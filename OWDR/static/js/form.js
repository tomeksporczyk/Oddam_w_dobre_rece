// var otherCheckbox = document.querySelector('#other');
//   var hidden = document.querySelector("#hidden-fields");
//   otherCheckbox.addEventListener("onclick", function(){
//     if (hidden.getAttribute("style") === "display: none"){
//       hidden.setAttribute("style", "display: block")
//       }
//     else{
//       hidden.setAttribute("style", "display: none")
//     }
//   })

$(document).ready(function() {
    $(function () {
// alert('dupa');
        // Get the form fields and hidden div
        var checkbox = $("#other");
        var hidden = $("#hidden-fields");
        // var populate = $("#populate");

        // Hide the fields.
        // Use JS to do this in case the user doesn't have JS
        // enabled.
        hidden.hide();

        // Setup an event listener for when the state of the
        // checkbox changes.
        checkbox.change(function () {
            // Check to see if the checkbox is checked.
            // If it is, show the fields and populate the input.
            // If not, hide the fields.
            if (checkbox.is(':checked')) {
                // Show the hidden fields.
                hidden.show();
                // Populate the input.
                // populate.val("Dude, this input got populated!");
            } else {
                // Make sure that the hidden fields are indeed
                // hidden.
                hidden.hide();
                $("#hidden-field").val("");
            }
        });
    });
});