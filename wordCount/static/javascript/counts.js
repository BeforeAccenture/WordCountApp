$(document).ready(function() {
    $('#id_sentence').on('input', function() {
        var csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            url: '/counts/',
            type: 'POST',
            data: {
                'text': $(this).val(),
                'csrfmiddlewaretoken': csrftoken
            },
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            },
            success: function(data) {
                document.getElementById("wordcount").innerHTML = "WORD COUNT : " + data["WordCount"];
                document.getElementById("lettercount").innerHTML = "LETTER COUNT : " + data["LetterCount"];
                document.getElementById("linecount").innerHTML = "LINE COUNT : " + data["LineCount"];
            },
            error: function(xhr, status, error) {
                console.log(error);
            }
        });
    });
});
