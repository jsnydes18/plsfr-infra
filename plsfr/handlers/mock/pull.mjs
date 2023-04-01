const handler = async (event, context, callback) => {
    const { reqId } = event.queryStringParameters;
    const pages = [];
    const numPages = Math.ceil(Math.random() * 10);
    for (let x = 0; x <= numPages; x += 1) {
      const playlists = [];
      for (let y = 0; y <= Math.ceil(Math.random() * 25); y += 1) {
        playlists.push({
          name: "test",
          followers: Math.ceil(Math.random() * 10000),
          tracks: Math.ceil(Math.random() * 200),
          popularity: Math.random() * 100,
          lastModified: `${Math.ceil(Math.random() * 365)} days ago`,
          ownerDetails: {
            spotify: "1234567890",
            instagram: "@testinsta",
            twitter: "@testtwit",
            email: "testemail@testurl.com",
          },
        });
      }
      pages.push({
        pageNum: x,
        playlists,
      });
    }

    const response = {
      isBase64Encoded: false,
      statusCode: 200,
      headers: {
        "Access-Control-Allow-Headers":"*",
        "Access-Control-Allow-Methods":"OPTIONS,GET",
        "Access-Control-Allow-Origin":"*"
      },
      body: JSON.stringify({
        reqId,
        results: pages,
      }),
    };
    return callback(null, response);
  };

  export { handler };
