var app = app || {};

app.initArtifactPage = function() {
    $(window).on('hashchange', function() {
        var url = "data/artifact";
        var params = {'format':'html'}
        var lookup = window.location.hash.substring(1).split('/');
        if (lookup.length > 1) {
            var index = lookup[0];
            var key = lookup[1];
            params[index] = key;
        }
        $.get(url, params, function(data) {
            $("#content").html(data);
        });
    });
    $(window).trigger('hashchange');
};
