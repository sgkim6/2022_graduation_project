window.onload = function(){
    document.getElementById("review_submit").onclick = click_Submit;
    document.getElementById("database_submit").onclick = database_Submit;
}

function click_Submit() {

    var Data = $("#review_input").val();
    let start = new Date();

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
            let end = new Date();
            elapsed = (end - start) / 1000;
            console.log(elapsed);
            // $("#review_analysis_result").html(response);
        },
        fail : function(){
            $("#analysis").css("display", "block");
            $("#review_analysis").html(Data);
            $("#senti").text("연결 실패");
            $("#accuracy").text("연결 실패");
        }
    })

}

function database_Submit() {

    var reviewData = $("#review_analysis").text();
    var resultData = $("input[name='check']:checked").val();;
    console.log(reviewData);
    console.log(resultData);

    $.ajax({
        url : '/api2/',
        data: {
            review: reviewData,
            result: resultData
        },
        type: "POST",
        dataType: "json",
        success : function(response){
            console.log(response)
            $("#analysis").css("display", "none");
            $('#review_input').val('');
        }
    })

}
