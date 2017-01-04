/**
 * Created by Dharmista on 24-Jun-16.
 */
function get_space(){
    $("#submit").click(function () {
       var arr = document.getElementsByClassName("scre");
       var arr_length = parseInt(arr.length);
        sum=0;
        for(i=0;i<arr_length;i++)
         sum += parseFloat(arr[i].innerHTML);
        var ans;
        if($("#target").val()==''){
            $("#sugg").html("<br>Please enter a target value");
        }
        else {
            var tar = parseFloat($("#target").val());
            ans = (8 * tar - sum) / 2;
            $("#sugg").html("<br>You must approximately get " + ans + "% in both semesters...");
            if (0 <= ans && ans <= 93) {
                $("#sugg").append(" All d best");
            }
            else if (ans <= 0) {
                $("#sugg").html("You can get 0 in all the remaining semesters... COOL")
            }
            else if (ans <= 100) {
                $("#sugg").append(" Which may be slightly diffcult. <br>But all d best");
            }
            else {
                $("#sugg").append(" Which is impossible");
            }
        }
    });
}

$(document).ready(function(){
    $("#show_targ").click(function(){
        $("#myModal").modal();
    });
});

$(document).ready(function () {
    $("#show_targ").click(function(){
        get_space();
    });
});