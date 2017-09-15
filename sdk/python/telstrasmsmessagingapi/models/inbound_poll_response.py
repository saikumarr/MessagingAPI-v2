# -*- coding: utf-8 -*-

"""
    telstrasmsmessagingapi.models.inbound_poll_response

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""


class InboundPollResponse(object):

    """Implementation of the 'InboundPollResponse' model.

    Poll for incoming messages returning the latest. Only works if no callback
    url was specified when provisioning a number.

    Attributes:
        to (string): The phone number (recipient) that the message was sent
            to(in E.164 format).
        mfrom (string): The phone number (sender) that the message was sent
            from (in E.164 format).
        body (string): Text body of the message that was sent
        received_timestamp (string): The date and time when the message was
            recieved by recipient.
        more_messages (int): Indicates if there are more messages that can be
            polled from the server. 0=No more messages available. Anything
            else indicates there are more messages on the server.
        message_id (string): Optional message ID of the SMS you sent. Use this
            ID to view the message status or get responses.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "to" : "to",
        "mfrom" : "from",
        "body" : "body",
        "received_timestamp" : "receivedTimestamp",
        "more_messages" : "moreMessages",
        "message_id" : "messageId"
    }

    def __init__(self,
                 to=None,
                 mfrom=None,
                 body=None,
                 received_timestamp=None,
                 more_messages=None,
                 message_id=None):
        """Constructor for the InboundPollResponse class"""

        # Initialize members of the class
        self.to = to
        self.mfrom = mfrom
        self.body = body
        self.received_timestamp = received_timestamp
        self.more_messages = more_messages
        self.message_id = message_id


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        to = dictionary.get("to")
        mfrom = dictionary.get("from")
        body = dictionary.get("body")
        received_timestamp = dictionary.get("receivedTimestamp")
        more_messages = dictionary.get("moreMessages")
        message_id = dictionary.get("messageId")

        # Return an object of this model
        return cls(to,
                   mfrom,
                   body,
                   received_timestamp,
                   more_messages,
                   message_id)

