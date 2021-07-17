# Based on https://www.youtube.com/watch?v=s_4ZrtQs8Do
from abc import ABC, abstractmethod


class MessageSender(ABC):
    @abstractmethod
    def get_sender_info(self):
        """One line sender info."""
        raise NotImplementedError

    @abstractmethod
    def send(self, msg):
        """Send a single message."""
        raise NotImplementedError

    @abstractmethod
    def get_limit(self):
        """Maximum size limit for single message."""
        raise NotImplementedError


class TweetSender(MessageSender):
    """Sends a message similar to a tweet."""

    def get_sender_info(self):
        return "===You are using TweetSender==="

    def send(self, msg):
        """Chunk message and sends chunks."""
        limit = self.get_limit()
        for start in range(0, len(msg), limit):
            chunk = msg[start: start + limit]
            print(f'Sending message chunk: "{chunk}"')

    def get_limit(self):
        """A tweet message can contain upto 14 chars."""
        return 14


class EmailSender(MessageSender):
    """Sends a message similar to email."""

    def get_sender_info(self):
        return "===You are using EmailSender==="

    def send(self, msg):
        """Sends message as email."""
        if len(msg) > self.get_limit():
            raise Exception("Message too long to send.")
        print(f'Sending email: {msg}')

    def get_limit(self):
        """A email message can contain upto 1000 chars."""
        return 1000


def main(sender: MessageSender, msg: str):
    print(sender.get_sender_info())
    sender.send(msg)


def get_sender():
    factories = {
        "email": EmailSender(),
        "tweet": TweetSender()
    }
    sender = input("Choose a sender (email, tweet): ")
    if sender in factories:
        return factories[sender]
    print("Invalid sender.")


def get_message():
    return input("Enter message to send: ")


if __name__ == "__main__":
    sender = get_sender()
    if sender:
        main(sender, get_message())
