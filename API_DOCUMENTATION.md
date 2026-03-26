# API Documentation

This file contains the module documentation for the CriptoBoti API.

## Overview

The CriptoBoti API provides functionality for trading and managing cryptocurrency assets.

## Modules

### 1. Authentication
- **Endpoint:** `/auth`
- **Methods:** `POST`
- **Description:** Authenticates users and returns an access token.

### 2. Market Data
- **Endpoint:** `/market`
- **Methods:** `GET`
- **Description:** Retrieves market data for various cryptocurrencies.

### 3. Trading
- **Endpoint:** `/trade`
- **Methods:** `POST`
- **Description:** Executes a trade operation based on user input.

## Usage Examples

### Authentication Example
```python
import requests

response = requests.post('https://api.criptoboti.com/auth', data={'username': 'user', 'password': 'pass'})
print(response.json())
```

### Market Data Example
```python
response = requests.get('https://api.criptoboti.com/market')
print(response.json())
```

### Trading Example
```python
response = requests.post('https://api.criptoboti.com/trade', json={'action': 'buy', 'amount': 1, 'currency': 'BTC'})
print(response.json())
```

## Error Handling

In case of errors, the API will return an appropriate status code and message for debugging.