window.onload = function(){
    document.getElementById("review_submit").onclick = model_Submit;
}

function model_Submit() {

    var Model_name = $("#selected_model").val();

    $.ajax({
        url : '/adm/change/',
        data: {
            model_name: Model_name
        },
        type: "POST",
        dataType: "json",
        success : function(){
            alert('변경되었습니다')
        },
        fail : function(){
            
        }
    })

}