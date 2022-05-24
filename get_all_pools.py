import codecs
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
transport = AIOHTTPTransport(url="https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3")
client = Client(transport=transport, fetch_schema_from_transport=True)
query = gql("""
query UNISWAP($skip: Int, $first: Int, $txLimit: BigInt){
  pools(first: $first, skip: $skip, where: {txCount_gt: $txLimit}) {
    token0 {
        id
        name
    }
    token1 {
        id
        name
    }
    txCount
    id
    
  }
}
""")
def main():
    params = {"skip": -1000, "first": 1000, "txLimit" : 100}
    result = {}
    with codecs.open("pools.txt", "w") as file: 

        while result.get("pools") != []:
            params["skip"] += 1000
            result = client.execute(query, variable_values=params)

            for i in result["pools"]:
                file.write(i["token0"]["id"] + " " + ''.join(letter for letter in i["token0"]["name"] if letter.isalnum()) + " ")
                file.write(i["token1"]["id"] + " " + ''.join(letter for letter in i["token1"]["name"] if letter.isalnum()) + " ")
                file.write(i["id"] + " ")
                file.write("\n")
main()