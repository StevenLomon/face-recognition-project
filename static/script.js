$(document).ready(function() {
    var base64image = null; 

    $('form').on('submit', function(event) {
        event.preventDefault();
        var fileInput = $('input[type="file"]')[0];
        var file = fileInput.files[0];

        if (file) {
            var reader = new FileReader();
            reader.onloadend = function() {
                base64image = reader.result.split(',')[1]; 
                $('#uploaded-image').attr('src', 'data:image/png;base64,' + base64image);
                $('#image-display').show();
            };
            reader.readAsDataURL(file);
        } else {
            console.log('No file selected');
        }
    });

    
    $('.prediction-button').click(function() {
        var predictionType = $(this).data('type'); 

        if (base64image) {
            var message = {
                image: base64image,
                type: predictionType 
            };
        
            $.ajax({
                type: 'POST',
                url: '/predict',
                contentType: 'application/json',
                data: JSON.stringify(message),
                success: function(response) {
                    console.log('Prediction:', response.prediction);
                    var predictions = response.prediction;
                    var resultsHtml = "";
                    for (var key in predictions) {
                        if (predictions.hasOwnProperty(key)) {
                            resultsHtml += '<div class="prediction-result">' +
                                                '<span class="prediction-key">' + key + ':</span> ' +
                                                '<span class="prediction-value">' + (predictions[key] * 100).toFixed(2) + '%</span>' +
                                            '</div>';
                        }
                    }
                    $('#prediction-results').html(resultsHtml);
                },
                error: function(error) {
                    console.log('An error occurred:', error);
                }
            });
        }
    });
});
