$(document).ready(function() {
    $('form').on('submit', function(event) {
        event.preventDefault();
        var fileInput = $('input[type="file"]')[0];
        var file = fileInput.files[0];

        if (file) {
            var reader = new FileReader();
            reader.onloadend = function() {
                var base64data = reader.result.split(',')[1];
                var message = { image: base64data };

                $.ajax({
                    type: 'POST',
                    url: '/predict',
                    contentType: 'application/json',
                    data: JSON.stringify(message),
                    success: function(response) {
                        console.log('Prediction:', response.prediction);
                        var imageUrl = 'data:image/png;base64,' + base64data; 
                        $('#uploaded-image').attr('src', imageUrl);
                        $('#image-display').show();
                        var predictions = response.prediction;
                        var resultsHtml = "";
                        for (var key in predictions) {
                            if (predictions.hasOwnProperty(key)) {
                                resultsHtml += key + ": " + (predictions[key] * 100).toFixed(2) + "%<br>";
                            }
                        }
                        $('#prediction-results').html(resultsHtml);
                    },
                    error: function(error) {
                        console.log('An error occurred:', error);
                    }
                });
            };
            reader.readAsDataURL(file);
        } else {
            console.log('No file selected');
        }
    });
});
