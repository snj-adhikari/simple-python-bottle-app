$(function(){
    //Executes when clicked button
    $('.start-button').on('click' , function(){
        $.ajax({
            url:'https://localhost:8080/start',
            method:"GET", 
            success:function (timer){
                // Get timer  on second 
                var localTimer = timer ;
                setInterval(function(){
                    $('.timer').text(timer- 1)                
                }, 1000)// runs every second;
            }
        });
    });
    //Executes when clicked enter file  , submit result
    $('.input-text').bind('enterKey' , function(){
        var question = $(this).data('question');
        var answer = $(this).val();
        $.ajax({
            url:'https://localhost:8080/score',
            method:"POST",
            data:{
                question: question , 
                answer: answer, 
            },
            success:function (){
                get_question();
            }
        });
    })
    function get_question(){
        $.ajax({
            url: 'https://localhost:8080/question', 
            method: 'GET', 
            success: function (data){
                $(".question").data(data.question);
                $('.input-text').data('question' , data.question);
            }
        })
    }
});