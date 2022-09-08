from pade.core.agent import Agent
from pade.misc.utility import display_message, start_loop
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from name_gen import get_name
import sys


class MyReceiver(Agent):

    def __init__(self, port):
        self.name = get_name(port-1)
        self.aid = AID(name=f"{self.name}[R]@localhost:{port}")
        super().__init__(self.aid)

    def on_start(self):
        super().on_start()
        print(f'\n{self.name} is listening to message...\n')

    def react(self, message: ACLMessage):
        super().react(message)
        # print("---------- New Message ----------")
        name = "[-- ME --]" if self.aid.port == message.sender.port + \
            1 else message.sender.localname
        print(f'\n{name} --> {message.content}\n')


class MySender(Agent):

    def __init__(self, port, r_port):
        self.aid = AID(f"{get_name(port)}@localhost:{port}")
        self.aid_r = AID(f"{get_name(port)}[R]@localhost:{port+1}")
        self.receiver = AID(f"{get_name(r_port-1)}[R]@localhost:{r_port}")
        super().__init__(self.aid)

    def on_start(self):
        super().on_start()
        print(f"\n{self.aid.localname} is ready to send messages...\n")
        self.call_later(1.0, self.send_message)

    def react(self, message):
        super().react(message)
        # self message to self if recieved by sender end
        self.send_message(message, self.aid_r)

    def send_message(self, mess=None, other_recv=None):
        if not mess:
            mess = input("\nEnter Message \n(or Say 'BYE' to exit): ")
        if mess.lower() == "bye":
            exit()
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(self.receiver)
        message.add_receiver(self.aid_r)
        self.add_all_agents(message.receivers)
        message.set_content(
            f"{mess if len(mess) > 0 else 'Empty Message'}")
        self.send(message)
        print("\n----- Message sent -----\n")
        self.call_later(1.0, self.send_message)

    def add_all_agents(self, receivers):
        for receiver in receivers:
            self.agentInstance.table[receiver.localname] = receiver


if __name__ == "__main__":
    _, ag_type, port, *r_port = sys.argv
    port = int(port)

    if ag_type == "-s":
        sender = MySender(port, int(r_port[0]))
        start_loop([sender])
    elif ag_type == "-r":
        receiver = MyReceiver(port)
        start_loop([receiver])
    else:
        print(f"Invalid argument for agent type: {ag_type}")
