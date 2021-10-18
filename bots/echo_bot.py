# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount


class EchoBot(ActivityHandler):
    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")

    async def on_message_activity(self, turn_context: TurnContext):
        transfer = [{
"type": "message",
"text": "I'll transfer you to a human agent",
"channelData": {
    "action": {
        "name": "TRANSFER",
        "parameters": {
            "skill": "3369363250"
        }
    }
}          
}]
        if (turn_context.activity.text == "agent"):
            return await turn_context.send_activity(MessageFactory.text(transfer[0]))

        return await turn_context.send_activity(
            MessageFactory.text(f"Echo: {turn_context.activity.text}")
        )
