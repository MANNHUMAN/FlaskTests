$(function(){
    $("p").on({
        click: function(){
            $(this).css("color", "red");
        },
        mouseleave: function(){
            $(this)/css("color", "palevioletred");
        },
    })})