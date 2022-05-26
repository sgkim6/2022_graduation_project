window.onload = function(){
    document.getElementById("review_submit").onclick = click_Submit;
}

function click_Submit() {

    var Data = $("#review_input").val();

    $.ajax({
        url : '/api/',
        data: {
            review: Data
        },
        type: "POST",
        dataType: "json",
        success : function(response){
            console.log(response)
            $("#analysis").css("display", "block");
            $("#review_analysis").html(Data);
            $("#senti").text(response.senti);
            $("#accuracy").text(response.score);
            // $("#review_analysis_result").html(response);
        }
    })

   
}
