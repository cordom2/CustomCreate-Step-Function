exports.handler = function(event, context, callback) {
     var AWS = require('aws-sdk');
     var s3 = new AWS.S3();
     var params = {Bucket: event.S3Bucket, Key: event.S3Key};
     s3.getObject(params, function(err, data) {

        if (err) {
            console.log(err, err.stack);
            // file does not exist
            console.log("failed");
            event.FoundNecessaryFiles = false;
            callback(null,event);
        }
        else {
            console.log(data);
            //file exist
            console.log("succeeded");
            event.FoundNecessaryFiles = true;
            callback(null,event);
        }
    });
};