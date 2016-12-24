%%bash

mongo
  
use twitterdb


var map = function() {
    var datetime = this._id.getTimestamp();

    var analise_por_hora  = new Date(datetime.getFullYear(),
                                     datetime.getMonth(),
                                     datetime.getDate(),
                                     datetime.getHours());
    emit(analise_por_hora , {count: 1});
}

var reduce = function(key, values) {
    var tot = 0;
    for(var x = 0; i < values.length; x++) { tot += values[x].count; }
    return {count: total};
}

db.tweets_collection.mapReduce( map, reduce, { "out": "Volume_Hora" } );

db.Volume_Hora.find().limit(10).sort({"_id":-1})
