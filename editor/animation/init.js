requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {
        var io = new extIO({
            functions: {
                js: 'chase',
                python: 'chase'
            }
        });
        io.start();
    }
);

multipleArguments: true,

animationTemplateName: 'animation',

animation: function($expl, data){
                if (!data.ext || !data.ext.explanation) {
                    return;
                }
                var expl = data.ext.explanation;
                $expl.addClass('output').html(expl);
            },

animation: function($expl, data){
                var checkioInput = data.in;
                if (!checkioInput){
                    return;
                }
                var canvas = new MedianCanvas($expl[0], checkioInput);
                canvas.createCanvas();
                canvas.animateCanvas();
            },

,
            retConsole: function (ret) {
                $tryit.find(".checkio-result").html("Your Result
" + ret);
            }

,
            tryit:function (this_e) {

}

$tryit = $(this_e.extSetHtmlTryIt(this_e.getTemplate('tryit')));
this_e.extSendToConsoleCheckiO(tCanvas.gatherData());

