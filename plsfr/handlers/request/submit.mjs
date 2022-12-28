import AWS from "aws-sdk";

const handler = async (event, context, callback) => {
  const { input } = JSON.parse(event.body);
  const sqs = new AWS.SQS();
  const params = {
    MessageBody: input,
    QueueUrl: "https://sqs.us-east-2.amazonaws.com/677532242987/submitq",
  };
  const res = await sqs.sendMessage(params).promise();

  const response = {
    isBase64Encoded: false,
    statusCode: 200,
    headers: {},
    body: JSON.stringify({
      reqId: res.MessageId,
    })
  };
  return callback(null, response);
};

export { handler };
