$(document).ready(function(){
    endpoint = location.protocol + "//" + location.host + "/api/3/action/";

    var active_view = $('li.active.view_item:first').data('id');

    $('#canonical, #homepage').click(function(){
        var el = $(this);
        canonical_or_homepage = el.attr('id');
        
        var data = {
            'resource_view_id': active_view,
        };
        data[canonical_or_homepage] = !el.hasClass('active')
        
        $.ajax({
            method: "POST",
            data: encodeURIComponent(JSON.stringify(data)),
            url: endpoint + 'featured_upsert',
        }).done(function(result){
            if (result['result'][canonical_or_homepage] === 'True'){
                el.addClass('active');
            } else {
                el.removeClass('active');
            }
        });
    });
});
