/**
 * Created with IntelliJ IDEA.
 * User: Bobby
 * Date: 8/29/13
 * Time: 5:08 PM
 * To change this template use File | Settings | File Templates.
 */

/*A closure around generic helper methods*/
var helpers = function() {
    /*get an elements width and height*/
    function getDimensions($el) {
        var h = $el.height();
        var w = $el.width();

        return {height : h, width: w};
    }
    
    return {getDimensions : getDimensions};
}

/*A closure around everything having to do with images*/
var images = function() {        
    var getDimensions = helpers().getDimensions;
    
    /*PRIVATE FUNCTION: is the image a "tall" image?*/
    var isTallImage = function($img) {
        var isTall = getAspectRatio($img) < 1;
        return isTall;
    }
    
    /*PRIVATE FUNCTION: get the aspect ratio of the image. IMPORTANT: Width is the scaling factor, height is 1*/
    var getAspectRatio = function($img) {
        var height = getDimensions($img).height;
        var width = getDimensions($img).width;        
        
        return width / height;
    }
    
    /*scale an image by a given percentage, maintaining its aspect ratio*/
    var scaleImage = function($img, scaleFactor) {        
        var origHeight = getDimensions($img).height;
        var origWidth = getDimensions($img).width;
        
        $img.css('height', origHeight * scaleFactor);
        $img.css('width', origWidth * scaleFactor);
    }
    
    /*scale an image to entirey fill a container without losing its aspect ratio*/
    var scaleToMax = function($img, $container) {
        var imgWidth = getDimensions($img).width;
        var imgHeight = getDimensions($img).height;
        var contWidth = getDimensions($container).width;
        var contHeight = getDimensions($container).height;        
        
        /*when determining scaling factor, it is safest to take the larger factor to ensure we completely fill the container*/
        var scalingFactor = (contWidth / imgWidth) > (contHeight / imgHeight) ? contWidth / imgWidth : contHeight / imgHeight;
        scaleImage($img, scalingFactor);      
    }
    
    return {scale : scaleImage, scaleMax : scaleToMax};
}

/*A closure around everything having to do with drag / drop interactions*/
var dragandrop = function() {  
    var help = helpers();
    
    /*PRIVATE VARIABLE: the droppables*/
    var $droppables = [];

    /*called when the user chooses to reset the collage*/
    var reset = function() {
        $droppables = [];
    }
    
    /*create and return a new draggable object*/
    var createDraggable = function($el, extraOptions) {
        var $newDraggable = $el.draggable({ containment: ".container", revert : 'invalid', helper: "clone" });
        return $newDraggable;
    }
    
    /*create and return a new droppable object*/
    var createDroppable = function($el) {
        var $newDroppable = $el.droppable({ tolerance: "pointer" });
        $droppables.push($newDroppable);
        return $newDroppable;
    }
    
    /*bind a droppable to the drop event, second parameter is a function designating what to do on drop */
    var onDrop = function($droppable, cb) {
        $droppable.on( "drop", function( event, ui ) {
            cb(event, ui);
        });
    }
    
    /*bind a draggable drag event, second parameter is cb function for on drag*/
    var onDrag = function($draggable, cb) {
        $draggable.on('drag', function( event, ui) {
            cb(event, ui);
        });
    }
    
    /*check if a droppable is occupied by an image*/
    var droppableTaken = function($droppable) {
        return $droppable.hasClass('taken');
    }
    
    /*create the json data for the post*/
    var createJson = function(collageName) {
        var jsonData = {name: collageName, data: []};
        for (var i = 0, j = $droppables.length ; i < j ; i++) {
            /*first check if the droppable has an image dropped on it*/
            var image = $droppables[i].find('img').length > 0 ? $droppables[i].find('img').first() : null;
            if (image != null ) {
                jsonData.data.push({postcard_width : help.getDimensions($droppables[i]).width, 
                                    postcard_height : help.getDimensions($droppables[i]).height,
                                    image : $(image).attr('src')});
            }                            
        }                
        
        return jsonData;
    }
    
    return {reset : reset, draggable : createDraggable, droppable : createDroppable, 
            bindDrop : onDrop, bindDrag : onDrag,  taken : droppableTaken, createJson : createJson};
}


