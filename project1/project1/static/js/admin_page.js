window.onload = function(){
    document.getElementById("review_submit").onclick = model_Submit;
    document.getElementById("log_download").onclick = download_Submit;
    document.getElementById("user_page").onclick = user_Page;
}

function user_Page(){

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

function download_Submit() {

    var Data = "";

    $.ajax({
        url : '/adm/download/',
        data: {
            data: Data
        },
        type: "POST",
        dataType: "json",
        success : function(){
            let element = document.createElement('a');
            element.setAttribute('href','../static/csv/log.csv')
            element.setAttribute('download', 'User_input.csv');
            element.style.display = 'none';
            document.body.appendChild(element);
            element.click();
            document.body.removeChild(element);
            alert('asd')
        },
        fail : function(){
            
        }
    })

}
