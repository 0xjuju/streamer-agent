
from django.test import TestCase
from framework.agents import OpenAI


class TestAgents(TestCase):
    def setUp(self):
        self.api = OpenAI()

    def test_create_assistant(self):

        personality = ("A very funny guy that works at Mcdonalds. He doesn't take life too seriously. His only goal in "
                       "life is to make it big time rich. He spends all of his time outside of work gambling on various"
                       "cryptocurrencies. He doesn't care when he loses, because despite his strong gambling "
                       "mentality, he has greate bankroll management skills. When he makes a trade that goes to zero, "
                       "he laughs it off and makes a joke. He is always 100% bullish crypto, but always makes sarcastic"
                       " jokes about working at McDonalds. One of his favorite phrases to say when questioned about his"
                       " goals or when he buys a new token is 'I'm just tryna turn this stack into a Milly you feel me?'"
                       " He is an extrovert and laughs at everyone's jokes. He is down to earth and can talk about "
                       "anything. Even though he has no formal education, he is quite good at empathizing with others, "
                       "and communicating with them. He never says bad things about anyone, and supports his fellow "
                       "traders with support when they are losing money, or the market is bearish. When he is not, "
                       "he is at his computer live-streaming his trades and talking with his fans on Twitch.tv. "
                       "Whenever he is talking to anyone, he is streaming. He is always looking through the comments "
                       "to see what his fans are talking about, and engages with them frequently. He never gives "
                       "financial advice, and when he buys a token live, he always says a bullish corny line but always"
                       " follows it with 'Not Financial Advice'.")

        agent = self.api.create_assistant(
            instructions=f"You are a person named Tony with the following personality: {personality}"
        )

        print(agent)

    def test_create_message(self):
        thread_id = "thread_lNDAAmvVmcyj3rEvnLaAPqtJ"
        message = self.api.create_message(thread_id, "user", "Hey, what are you up to today?")
        print(message)

    def test_create_thread(self):
        thread = self.api.create_thread()
        print(thread)

    def test_run_thread(self):

        agent_id = "asst_0R8QEVA4TEaSdgSJ2hSfjMpw"
        thread = self.api.create_thread()

        message = " Hey, what's your name?"

        self.api.create_message(thread.id, "user", message)

        run = self.api.run_thread(thread.id, agent_id)

        if run.status == 'completed':
            messages = self.api.list_messages(thread.id)
            for message in messages:
                print(message.role, message.content[0].text)
        else:
            print(run.status)

    def test_get_fine_tuned_model(self):
        assistant = self.api.create_assistant(instructions="", model="ft:gpt-4o-2024-08-06:personal::AuQ1j7Ro")

        thread = self.api.create_thread()

        message = "King29: what's the point of this stream?"
        self.api.create_message(thread.id, "user", message)

        run = self.api.run_thread(thread.id, assistant.id)

        if run.status == 'completed':
            messages = self.api.list_messages(thread.id)
            for message in messages:
                print(message.role, message.content[0].text)
        else:
            print(run.status)













