Array.prototype.myMap = function(callback) {
    const newArray = [];
    // Only change code below this line
    for(let i=0; i<this.length; i++){
      newArray.push(callback(this[i], i, this));
    }
    // Only change code above this line
    return newArray;
  };

  //this is for referencing better functionallity
  // (https://forum.freecodecamp.org/t/freecodecamp-challenge-guide-implement-map-on-a-prototype/301230)