$(document).ready(function(){
    endpoint = location.protocol + "//" + location.host + "/api/3/action/";

    var active_view = $('li.active.view_item:first').data('id');

    $('#canonical').click(function(){
        var el = $(this);
        data = {
            'resource_view_id': active_view,
            'homepage': $('#homepage').hasClass('active'),
            'canonical': !$(this).hasClass('active')
        }
        
        $.ajax({
            method: "POST",
            data: encodeURIComponent(JSON.stringify(data)),
            url: endpoint + 'featured_upsert',
        }).done(function(result){
            if (result['result']['canonical'] === 'True'){
                el.addClass('active');
            } else {
                el.removeClass('active');
            }
        });
    });

    $('#homepage').click(function(){
        data = {
            'resource_view_id': active_view,
            'homepage': !$(this).hasClass('active'),
            'canonical': $('#canonical').hasClass('active')
        }
        
        $.ajax({
            method: "POST",
            data: encodeURIComponent(JSON.stringify(data)),
            url: endpoint + 'featured_upsert',
        }).done(function(result){
            if (result['result']['homepage'] === 'True'){
                $(this).addClass('active');
            } else {
                $(this).removeClass('active');
            }
        });
    });
});
