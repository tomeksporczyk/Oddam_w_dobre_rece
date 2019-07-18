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
        // Get the form fields and hidden div
        var checkbox = $("#other");
        var hidden = $("#hidden-fields");
        var text = "";
        // Hide the fields.
        hidden.hide();
        // event listener for when the state of the checkbox changes.
        checkbox.change(function () {
            // Check to see if the checkbox is checked.
            if (checkbox.is(':checked')) {
                // populate the text field's value with text if previously provided
                $("#hidden-field").val(text);
                // Show the hidden fields.
                hidden.show();
            } else {
                // hide fields
                hidden.hide();
                // save text field's value
                text = $("#hidden-field").val();
                // if text field is hidden its value is ""
                $("#hidden-field").val("");
            }
        });
    });

    $('#search_province').click(function(){
        dropdown_search($(this).val(), 'institutions_province')
    });

    function dropdown_search(value, id) {
        $("span#".concat(id)).each(function () {
            var found = 'true';
            $(this).each(function(){
                if ($(this).text().indexOf(value) < 0)
                {
                    found = 'false';
                }
            });
            if (found === 'true')
            {
                $(this).closest('div').show()
            }
            else
            {
                $(this).closest('div').hide()
            }
        })
    }

    var $targets = $('input[name="target"]');
    $targets.change(function(){
        var $checked = $targets.filter(function(){
            return $(this).prop('checked');
        });
        console.log($checked.val())
        $("span#institutions_target").each(function () {
            var found = 'true';
            $(this).each(function(){
                if ($(this).text().indexOf($checked) < 0)
                {
                    found = 'false';
                }
            });
            if (found === 'true')
            {
                $(this).closest('div').show()
            }
            else
            {
                $(this).closest('div').hide()
            }
        })
    })

});