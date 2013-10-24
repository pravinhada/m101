use photoalbum

// Adding index on image of album collection
db.albums.ensureIndex({'images':1});

// now iterating
var cursor = db.images.find();

var i = 0;

while(cursor.hasNext()){
    doc = cursor.next();
    image_id = doc._id;
    album = db.albums.find({images:image_id}).count();
    if(album == 0){
	// now delete from collection
	db.images.remove({_id:image_id});
	i++;
    }
}

print("Total removed images: ", i);
 
db.images.find({'tags':'kittens'}).count();
