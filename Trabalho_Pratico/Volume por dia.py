%%bash

mongo
  
use twitterdb

var map = function() {
    var datetime = this._id.getTimestamp();

    var analise_por_dia = new Date(datetime.getFullYear(),
                                     datetime.getMonth(),
                                     datetime.getDate());
    emit(analise_por_dia, {count: 1});
}

var reduce = function(key, values) {
    var tot = 0;
    for(var x = 0; i < values.length; x++) { tot += values[x].count; }
    return {count: tot};
}

db.tweets_collection.mapReduce( map, reduce, { "out": "Volume_Dia" } );

db.Volume_Dia.find().limit(50).sort({"_id":-1})
