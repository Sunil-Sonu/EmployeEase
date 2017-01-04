/**
 * Created by Dharmista on 11-Jul-16.
 */

    function show(matter) {
        $("#popup").fadeToggle();
        $("#outer").load("/about/"+matter);
    }
    $(document).ready(function(){
        $("#close").click(function(){
            $("#popup").fadeToggle();
        });
        $("#search").click(function(){
            if($("#item").val()!='')
                $(".body_main").load('http://localhost:8000/jobs/get/'+$("#item").val());
        });
    });
