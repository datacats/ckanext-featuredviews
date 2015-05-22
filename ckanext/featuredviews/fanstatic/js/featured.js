$(document).ready(function(){
    ckanapi = new CKAN.Client(location.protocol + "//" + location.host)

    var active_view = $('li.active.view_item:first').data('id')

    $('#canonical').click(function(){
        data = {
            'resource_view_id': active_view,
            'homepage': $('#homepage').hasClass('active'),
            'canonical': !$(this).hasClass('active')
        }
        ckanapi.action('featured_upsert', data, function(err, result){
            if (err == null){
                if (result['result']['canonical'] === 'True'){
                    $('#canonical').addClass('active');
                } else {
                    $('#canonical').removeClass('active');
                }
            }
        })
    });

    $('#homepage').click(function(){
        data = {
            'resource_view_id': active_view,
            'homepage': !$(this).hasClass('active'),
            'canonical': $('#canonical').hasClass('active')
        }
        ckanapi.action('featured_upsert', data, function(err, result){
            if (err == null){
                if (result['result']['homepage'] === 'True'){
                    $('#homepage').addClass('active');
                } else {
                    $('#homepage').removeClass('active');
                }
            }
        })
    });
});
