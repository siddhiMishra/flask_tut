
    $(document).ready(function() {
      $('#translate-button').click(function() {
        var apiKey = 'your-api-key-here';
        var apiUrl = 'https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-hi';
        var inputText = $('#input-text').val();

        $.ajax({
          type: 'POST',
          url: apiUrl,
          headers: {
            'Authorization': 'Bearer ' + apiKey,
            'Content-Type': 'application/json'
          },
          data: JSON.stringify({
            'inputs': inputText
          }),
          success: function(response) {
            $('#translated-text').text(response[0].output);
          },
          error: function(xhr, status, error) {
            console.log(xhr.responseText);
          }
        });
      });
    });
  