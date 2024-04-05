import asyncio
import os

from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions

from src.pubsub_python import Pubsub

# these must be set, you can get them from your robot's 'CODE SAMPLE' tab
robot_api_key_id = os.getenv('API_KEY_ID') or ''
robot_api_key = os.getenv('API_KEY') or ''
robot_address = os.getenv('ROBOT_ADDRESS') or ''

async def connect():
    opts = RobotClient.Options.with_api_key(
      api_key=robot_api_key,
      api_key_id=robot_api_key_id
    )
    return await RobotClient.at_address(robot_address, opts)

async def main():
    robot = await connect()

    print('Resources:')
    print(robot.resource_names)

    api = Pubsub.from_robot(robot, name="mqtt-service")

    def printMsg(msg):
        print(msg)

    async def pub():
        await asyncio.sleep(1)
        await api.publish("test/topic", "test message", 0)

    async def sub():
            await api.subscribe("test/topic", printMsg)

    asyncio.ensure_future(sub())
    asyncio.ensure_future(pub())
    await asyncio.sleep(2)

    # Don't forget to close the machine when you're done!
    await robot.close()

if __name__ == '__main__':
    asyncio.run(main())

