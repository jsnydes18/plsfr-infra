import AWS from "aws-sdk";

const handler = async (event, context, callback) => {
  const { reqId } = event.queryStringParameters;
  const ddb = new AWS.DynamoDB();
  const params = {
    ExpressionAttributeValues: {
      ":v1": {
        S: reqId,
      },
    },
    KeyConditionExpression: "msgId = :v1",
    ProjectionExpression: "pageNum",
    TableName: "pullTable",
  };
  const preResults = await ddb.query(params).promise();
  console.log(preResults)
  const results = [];
  preResults.Items.forEach(item => {
    results.push(AWS.DynamoDB.Converter.unmarshall(item));
  });

  const response = {
    isBase64Encoded: false,
    statusCode: 200,
    headers: {},
    body: JSON.stringify({
      reqId,
      results,
    }),
  };
  console.log(response)
  return callback(null, response);
};

export { handler };
