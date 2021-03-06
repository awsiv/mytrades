import logging

import gate_api
from gate_api.exceptions import ApiException, GateApiException

logger = logging.getLogger()
logger.setLevel(logging.INFO)

configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)
api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency

try:
    # List all futures contracts
    api_response = api_instance.list_delivery_contracts(settle)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->list_delivery_contracts: %s\n" % e)

