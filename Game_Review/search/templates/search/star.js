function starRate() {



 $(document).ready(function(){
            var options = {
                max_value: 6,
                step_size: 0.5,
                selected_symbol_type: 'hearts',
                url: 'http://localhost/test.php',
                initial_value: 3,
                update_input_field_name: $("#input2"),
            }
            $(".rate").rate();

            $(".rate").rate("setFace", 5, '😊');
            $(".rate").rate("setFace", 1, '😒');

            
            var options3 = {
                selected_symbol_type: 'utf8_emoticons',
                max_value: 4,
                step_size: 1,
                convert_to_utf8: true,
                only_select_one_symbol: true,
            };
            

            setTimeout(function(){
                $("#rate4").rate({
                    selected_symbol_type: 'fontawesome_beer',
                    max_value: 5,
                    step_size: 0.25,
                });

               
            }, 2000);

           

            $("#rate7").rate({
                selected_symbol_type: 'image2',
                max_value: 5,
                step_size: 1,
                update_input_field_name: $("#input1"),
                only_select_one_symbol: true,
                symbols:{
                    image2: {
                        base: ['<div style="background-image: url(\'./images/emoji1.png\');" class="im2">&nbsp;</div>',
                               '<div style="background-image: url(\'./images/emoji2.png\');" class="im2">&nbsp;</div>',
                               '<div style="background-image: url(\'./images/emoji3.png\');" class="im2">&nbsp;</div>',
                               '<div style="background-image: url(\'./images/emoji4.png\');" class="im2">&nbsp;</div>',
                               '<div style="background-image: url(\'./images/emoji5.png\');" class="im2">&nbsp;</div>',],
                        hover: ['<div style="background-image: url(\'./images/emoji1.png\');" class="im2">&nbsp;</div>',
                               '<div style="background-image: url(\'./images/emoji2.png\');" class="im2">&nbsp;</div>',
                               '<div style="background-image: url(\'./images/emoji3.png\');" class="im2">&nbsp;</div>',
                               '<div style="background-image: url(\'./images/emoji4.png\');" class="im2">&nbsp;</div>',
                               '<div style="background-image: url(\'./images/emoji5.png\');" class="im2">&nbsp;</div>',],
                        selected: ['<div style="background-image: url(\'./images/emoji1.png\');" class="im2">&nbsp;</div>',
                               '<div style="background-image: url(\'./images/emoji2.png\');" class="im2">&nbsp;</div>',
                               '<div style="background-image: url(\'./images/emoji3.png\');" class="im2">&nbsp;</div>',
                               '<div style="background-image: url(\'./images/emoji4.png\');" class="im2">&nbsp;</div>',
                               '<div style="background-image: url(\'./images/emoji5.png\');" class="im2">&nbsp;</div>',],
                    },
                },
            });
        });
    
}

