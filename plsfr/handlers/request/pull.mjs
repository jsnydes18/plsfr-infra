import AWS from "aws-sdk";

const handler = async (event, context, callback) => {
  const { reqId } = event.queryStringParameters;
  const ddb = new AWS.DynamoDB();
  const params = {
    // AttributesToGet: [
    //   "pageNum",
    //   "playlists"
    // ],
    ExpressionAttributeValues: {
      ":v1": {
        S: reqId,
      },
    },
    KeyConditionExpression: "msgId = :v1",
    // ProjectionExpression: "pageNum",
    // Select: "SPECIFIC_ATTRIBUTES",
    Select: "ALL_ATTRIBUTES",
    TableName: "pullTable",
  };
  console.log(params)
  const preResults = await ddb.query(params).promise();
  console.log(preResults)
  const results = [];
  preResults.Items.forEach(item => {
    results.push(AWS.DynamoDB.Converter.unmarshall(item));
  });

  const response = {
    isBase64Encoded: false,
    statusCode: 200,
    headers: {
      "Access-Control-Allow-Headers":"Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
      "Access-Control-Allow-Methods":"OPTIONS,GET",
      "Access-Control-Allow-Origin":"*"
    },
    body: JSON.stringify({
      reqId,
      results,
    }),
  };
  console.log(response)
  return callback(null, response);
};

export { handler };
