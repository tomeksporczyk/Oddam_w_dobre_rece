
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
        selectSearch($(this).val(), 'institutions_province')
    });

    function selectSearch(value, id) {
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
    $targets.change(function() {
        var value = $targets.filter(function() {
            return this.checked;
        });
        console.log(value.val());
    selectSearch(value.val(), 'institutions_target')
    });

    $('#search_name').keyup(function(){
                searchName($(this).val());
            });

    function searchName(value){
                $('div#institution_name').each(function(){
                    var found = 'false';
                    $(this).each(function(){
                        if($(this).text().toUpperCase().indexOf(value.toUpperCase()) >= 0)
                        {
                            found = 'true';
                        }
                    });
                    if(found === 'true')
                    {
                        $(this).parent().closest('div').show();
                    }
                    else
                    {
                        $(this).parent().closest('div').hide();
                    }
                })
            }
    $('#last-button').click(function(){
        var selectedItems = [];
        $.each($('input[name="item"]:checked'), function(){
            selectedItems.push($(this).siblings('span.description').text());
        });
        console.log(selectedItems);
        $.each($('input[name="other"]:checked'), function () {
            selectedItems.push($(this).siblings('span.description').text())
        });

        var quantity = $('input[name="quantity"]').val();
        console.log(quantity);

        var institution = $('input[name="institution"]:checked').siblings('span#dupa').children('div#institution_name').text();

        console.log(institution);

        var street = $('input[name="street"]').val();
        console.log(street);

        var city = $('input[name="city"]').val();
        console.log(city);

        var postalCode = $('input[name="postal_code"]').val();
        console.log(postalCode);

        var phoneNumber = $('input[name="phone_number"]').val();
        console.log(phoneNumber);

        var date_ = $('input[name="date"]').val();
        console.log(date_);

        var time_ = $('input[name="time"]').val();
        console.log(time_);

        var message = $('textarea[name="message"]').val();
        console.log(message);

        var quantityItems = $('<span class="summary--text">'.concat(quantity, ' worki: <br>',  selectedItems.join(',<br>'), '</span>'));
        $('#quantity-items-summary').append(quantityItems);

        var institutionSummary = $('<span class="summary--text">Dla fundacji '.concat(institution, '</span>'));
        $('#institution-summary').append(institutionSummary);

        var addressSummary = $('<li>'.concat(street, '</li><li>', city, '</li><li>', postalCode, '</li><li>', phoneNumber, '</li>'));
        $('#address-summary').append(addressSummary);

        var courierInfoSummary = $('<li>'.concat('</li><li>', date_, '</li><li>', time_, '</li><li>', message,'</li>'));
        $('#courier-info-summary').append(courierInfoSummary)


    })

});
