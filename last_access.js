/*

  Comments-
1)	Script takes a list of filenames as arguments.
2)	An error message is printed if the path to the file is not found.
3)	An error message is printed to handle anything that is not a file.
4)	It also assumes that spaces for the files have been escaped.
*/

var fs = require('fs'),
    fileStats = [];

exports.loadFileStats = function( paths ) {

  paths.forEach( function( path ) {

    try {
      var stats = fs.statSync( path );
      appendFileStats( stats, path );
    } catch ( e ) {
      
    }

  });

};

exports.printLastTouched = function() {
  if ( fileStats.length > 0 ) {
    sortFiles();
    console.log(fileStats[0].path);
  } else {
    console.log("no file available.");
  }
};

appendFileStats = function( stats, path ) {
  if ( stats.isFile() ) {
    stats.path = path;
    fileStats.push( stats );
  } else {
    console.log( "not a file." );
  }
};

sortFiles = function() {
  fileStats.sort( function( a, b ) {
    return Date.parse( b.atime ) - Date.parse( a.atime )
  } );
};

