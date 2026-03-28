from binance.client import Client

API_KEY = "s0hVUQc0TPOKmmObMMXseeCsykdvWOVRbl3xm37uGX6GSDcwFrArhyUm7rG1U7Zb"
API_SECRET = "CSm89gdhRUcXQruO7K22Cyz9MXlCdlDKpm0BvfF6rupxR76h15lJEtdLwBjnLyLd"

def get_client():
    client = Client(API_KEY, API_SECRET, testnet=True)

    return client