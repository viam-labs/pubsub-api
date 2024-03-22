# pubsub-api

Proto API and grpc bindings for pubsub capabilities

*pubsub-api* provides Proto API and grpc bindings for pubsub capabilities

Note: At this time, only the Python API is fully working, Go and others to come later.

## API

The pubsub resource implements the following API:

### publish(topic=*string*, message=*string*, qos=*number*)

The *publish()* command takes:

* topic: The pubsub topic to publish to
* message: the message to publish to the topic
* qos: the quality of service, if supported by the broker (for example, MQTT accepts 0|1|2)

### subscribe(topic=*string*)

The *subscribe()* command takes:

* topic: The pubsub topic to subscribe to

### unsubscribe(topic=*string*)

The *unsubscribe()* command takes:

* topic: The pubsub topic to unsubscribe to

## Using pubsub-api with the Python SDK

Because this module uses a custom protobuf-based API, you must include this project in your client code.  One way to do this is to include it in your requirements.txt as follows:

```
pubsub_api @ git+https://github.com/viam-labs/pubsub-api.git@main
```

You can now import and use it in your code as follows:

```
from pubsub_python import Pubsub
api = Pubsub.from_robot(robot, name="pubsub")
api.publish("topic", "message", 0)
```

See client.py for an example.

## Using pubsub with the Golang SDK

Because this module uses a custom protobuf-based API, you must import and use in your client code as follows:

``` go
import pubsub "github.com/viam-labs/pubsub-api/src/pubsub_go"

api, err := pubsub.FromRobot(robot, "pubsub")
fmt.Println("err", err)
api.Publish(context.Background(), "topic", "message", 0)
```

See client.go for an example.

## Building

To rebuild the GRPC bindings, run:

``` bash
make generate
```

Then, in `src/pubsub_python/grpc/pubsub_grpc.py change:

``` python
import pubsub_pb2
```

to:

``` python
from . import pubsub_pb2
```

Then, update the version in pyproject.toml
