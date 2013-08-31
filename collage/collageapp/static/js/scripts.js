/*page script file, perform necessary js operations for index.html*/
$(document).ready(function() {
    var $COLLAGE = $('section.collage');        
    
    var help = helpers();
    var im = images();
    var dragDrop = dragandrop();
    
    /*create the drag/drop areas and bind appropriately*/
    $( ".images ul li img" ).each(function() {
        dragDrop.draggable($(this));
    });
    
    $COLLAGE.find('.postcard').each(function() {
        var $droppable = dragDrop.droppable($(this));
        dragDrop.bindDrop($droppable, function(event, ui) {
            var $draggable = ui.draggable;
                        
            /*remove relative positioning on draggables then add them to the collage*/
            $draggable.css('position', 'static');
            $droppable.append($draggable);            
            
            /*we want to still be able to move the draggable after we've dropped it, so reinitialize it*/
            dragDrop.draggable($draggable);
            dragDrop.bindDrag($draggable, function() {
                $draggable.css('position', 'relative');
            })

            /*scale the image to the maximum size possible while maintaining aspect ratio*/
            im.scaleMax($draggable, $droppable);
        });
    });   
    
    /*when the user wants to create the collage, send the post data*/
    $('button.submit').click(function() {
        var collageName = $('input[name="name"]').val();
        $.post('/create/', JSON.stringify(dragDrop.createJson(collageName)), function(data) {
            $('.collage-alert').removeClass('gone');
            /*replace the placeholder collage id in the collage alert link to the collage with the actual id*/
            var collageId = $.parseJSON(data).collage_id;
            var collageUrl = $('.collage-alert a').attr('href');
            $('.collage-alert a').attr('href', collageUrl.replace(/\d+/, collageId));
        });        
    })
})
