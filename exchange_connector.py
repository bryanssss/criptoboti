import requests

class ExchangeConnector:
    def __init__(self, api_key, api_secret, base_url):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url

    def get_balance(self):
        url = f'{self.base_url}/balance'
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(url, headers=headers)
        return response.json()

    def execute_trade(self, trade_type, amount, price):
        url = f'{self.base_url}/trade'
        headers = {'Authorization': f'Bearer {self.api_key}'}
        data = {'type': trade_type, 'amount': amount, 'price': price}
        response = requests.post(url, headers=headers, json=data)
        return response.json()

# Example usage:
# connector = ExchangeConnector('your_api_key', 'your_api_secret', 'https://api.cryptoexchange.com')
# balance = connector.get_balance()
# print(balance)
# trade_response = connector.execute_trade('buy', 1.0, 50000)
# print(trade_response)