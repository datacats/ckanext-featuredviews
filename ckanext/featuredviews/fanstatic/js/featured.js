$(document).ready(function(){
    ckanapi = new CKAN.Client(location.protocol + "//" + location.host)

    var active_view = $('li.active.view_item:first').data('id')

    $('input:checkbox.featured').change(function(){
        if (this.checked) {
            //ckanapi.action('featured_create')
        }
    });
});
