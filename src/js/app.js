var UI = require('ui');
var ajax = require('ajax');
var Vector2 = require('vector2');


var image = new UI.Image({
  position: new Vector2(0, 0),
  size: new Vector2(144, 168),
  image: 'images/cup.png'
});
 
var main = new UI.Window({
  backgroundColor:'white'
});

main.add(image);


var screen = 0;

var tData;

function get(){

  main.each(function(element) {
    main.remove(element);
  });
ajax({ url: 'https://worldcup.sfg.io/matches/today', type: 'json' },
  function(data) {
    console.log(data);
    tData = data;
    var results = data;
    for(var i = 0; i < results.length;i++){
      if(results[i].status != "future"){
      }else{
        var r = results[i - 1];
        var StageName = r.stage_name;
        var text = new UI.Text({
          size: new Vector2(144, 168),
          text:StageName,
          textAlign:'center',
        color: 'black',
        position: new Vector2(0, 0),
          font:'GOTHIC_18_BOLD'
        });
        main.add(text);
        var team1 = r.home_team.code;
        var team2 = r.away_team.code;
        var text = new UI.Text({
          size: new Vector2(144, 168),
          text:team1,
          textAlign:'left',
        color: 'black',
        position: new Vector2(25, 110),
          font:'GOTHIC_24_BOLD'
        });
        main.add(text);
        var text = new UI.Text({
          size: new Vector2(119, 168),
          text:team2,
          textAlign:'right',
        color: 'black',
        position: new Vector2(0, 110),
          font:'GOTHIC_24_BOLD'
        });
        main.add(text);

        var score1 = r.home_team.goals;
        var score2 = r.away_team.goals;

        var text = new UI.Text({
          size: new Vector2(144, 168),
          text:score1,
          textAlign:'left',
        color: 'black',
        position: new Vector2(25, 60),
          font:'SANS_50'
        });
        main.add(text);
        var text = new UI.Text({
          size: new Vector2(119, 168),
          text:score2,
          textAlign:'right',
        color: 'black',
        position: new Vector2(0, 60),
          font:'SANS_50'
        });
        main.add(text);
        var text = new UI.Text({
          size: new Vector2(144, 168),
          text:"-",
          textAlign:'center',
        color: 'black',
        position: new Vector2(0, 60),
          font:'SANS_50'
        });
        main.add(text);

        var time = r.time;

        var text = new UI.Text({
          size: new Vector2(144, 168),
          text:time,
          textAlign:'center',
        color: 'black',
        position: new Vector2(0, 30),
          font:'GOTHIC_24_BOLD'
        });
        main.add(text);

        main.show();
        i = results.length;
      }
    }
  }
);
}

setInterval(function(){get();},20000);
get();
 
