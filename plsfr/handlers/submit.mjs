import crypto from "crypto";

const handler = async (event, context, callback) => {
  const { input } = event.body;
  const reqId = crypto.randomUUID();
  console.log(reqId);

  const response = {
    isBase64Encoded: false,
    statusCode: 200,
    headers: {},
    body: JSON.stringify({
      reqId,
    })
  };
  return callback(null, response);
};

export { handler };
