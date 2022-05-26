//index.html 동작 실험용 node.js 파일

var express = require("express")
var http = require("http"), path = require("path");

var static = require("serve-static");

const bodyParser = require("body-parser");

var app = express();
var router = express.Router();

//우선 포트는 8080에 할당해서 실험.
app.set("port", process.env.PORT||8080);
app.set("host", "127.0.0.1");

app.use(static(__dirname));
app.use(bodyParser.urlencoded({extended : false}));

// * 사용자 POST 요청 *
router.route("/source/index.html").post(function(req, res){

    //사용자가 서버에게 제출한 리뷰 문자열 POST 방식으로 받아오기.
    var review_input = req.body.review;

    //다시 사용자에게 보내는 response.
    var response = "NULL";
    res.send(response);
});
// app.all("*", function(req, res) {
//     res.status(404).send("<h1> ERROR - 페이지를 찾을 수 없습니다. </h1>");
// });

app.use("/", router);

http.createServer(app).listen(app.get("port"), app.get("host"), () => {
    console.log("Express server running at" + 
        " / Port : " + app.get("port") + " / Host : " + app.get("host"));
});

//http://localhost:8080/
