$(document).ready(function(){
    ckanapi = new CKAN.Client(location.protocol + "//" + location.host)

    var active_view = $('li.active.view_item:first').data('id')

    $('input:checkbox.canonical').change(function(){
        data = {
            'resource_view_id': active_view,
            'canonical': this.checked
        }
        ckanapi.action('featured_upsert', data, function(err, result){
            console.log(result);
        })
    });

    $('input:checkbox.homepage').change(function(){
        data = {
            'resource_view_id': active_view,
            'homepage': this.checked
        }
        ckanapi.action('featured_upsert', data, function(err, result){
            console.log(result);
        })
    });
});
