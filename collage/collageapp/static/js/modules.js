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
    /*create and return a new draggable object*/
    var createDraggable = function($el, extraOptions) {
        var $newDraggable = $el.draggable({ containment: ".container", revert : 'invalid', helper: "clone" });
        return $newDraggable;
    }
    
    /*create and return a new droppable object*/
    var createDroppable = function($el) {
        var $newDroppable = $el.droppable({ tolerance: "pointer" });
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
    
    return {draggable : createDraggable, droppable : createDroppable, bindDrop : onDrop, bindDrag : onDrag};
}


