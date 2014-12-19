$(document).ready(function(){

    $('#results-button').on('click', function(e){
        e.preventDefault();

        var term = $('#search-term').val();

        if(term == ''){
            return;
        }

        $.ajax({
            type: "GET",
            contentType: 'text/plain; charset=utf-8',
            url: "/search",
            data: { key_word: term }
        }).done(function( data ) {
            $('#results-list').html(data);
        });
    });

});
