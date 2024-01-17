from yowsup.layers.auth import YowAuthenticationProtocolLayer, YowCryptLayer
from yowsup.layers import YowLayerEvent
from yowsup.layers.network import YowNetworkLayer
from yowsup.stacks import YowStackBuilder

# Replace with your own phone number and password
phone_number = "+923156526523"
password = "Apple.com@2033"

# Create a Yowsup stack and add the necessary layers
stack_builder = YowStackBuilder()
stack = stack_builder \
    .pushDefaultLayers() \
    .push(YowAuthenticationProtocolLayer, credentials=(phone_number, password)) \
    .push(YowCryptLayer) \
    .push(YowNetworkLayer) \
    .build()

# Start the stack and wait for it to connect to the WhatsApp server
stack.start()
stack.sendEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))
