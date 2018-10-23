
console.log('TEST S3!');  

const AWS = require('aws-sdk');

const s3 = new AWS.S3({accessKeyId : 'AKIAIYMMB4WYPGD7IOQQ', 
					  secretAccessKey : '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', 
					  useAccelerateEndpoint: true});



  	var fileurls = [];
  
	/*setting the presigned url expiry time in seconds, also  if user making the request is an authorized user for your app (this will be specific to your app’s auth mechanism so i am skipping it)*/
  	const signedUrlExpireSeconds = 60 * 60;
  	const myKey = '111111.jpg';
  	const myBucket = 'profile-avatars-dev';
  	const contenttype = 'text/csv'
    const params = {Bucket: myBucket, Key: myKey, Expires: signedUrlExpireSeconds, ACL: 'bucket-owner-full-control', ContentType: contenttype}

	s3.getSignedUrl('putObject', params, function (err, url, res){

		if(err){
 			
 			console.log('Error getting presigned url from AWS S3');
 			//res.json({ success : false, message : 'Pre-Signed URL error', urls : fileurls});
		 }
 		else{
 			
 			fileurls[0] = url;
 			console.log('Presigned URL: ', fileurls[0]);
 			//res.json({ success : true, message : 'AWS SDK S3 Pre-signed urls generated successfully.', urls : fileurls});
 			

 			const file = '/Users/luisvargas/Desktop/nationalGeographic_default_avatar.jpg'
				/*
 			const headers = new HttpHeaders({'Content-Type': contenttype});
 			const req = new HttpRequest(
 										'PUT',
 										fileurls[0],
 										file,	
 										{
										   headers: headers,	
   											reportProgress: true, //This is required for track upload process
 										});
			
			 return http.request(req);
			*/
			}
		
	});
