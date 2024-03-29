import crypto from "crypto";

const handler = async (event, context, callback) => {
  const { input } = JSON.parse(event.body);
  const reqId = crypto.randomUUID();
  console.log(reqId);

  const response = {
    isBase64Encoded: false,
    statusCode: 200,
    headers: {
      "Access-Control-Allow-Headers":"*",
      "Access-Control-Allow-Methods":"OPTIONS,PUT",
      "Access-Control-Allow-Origin":"*"
    },
    body: JSON.stringify({
      reqId,
    })
  };
  return callback(null, response);
};

export { handler };
