import json

import openai
from decouple import config


class OpenAI:
    def __init__(self):
        self.api_key = config("OPENAI_API_KEY")
        openai.api_key = self.api_key
        self.default_model = "ft:gpt-4o-2024-08-06:personal::AuQ1j7Ro"

    @staticmethod
    def create_assistant(instructions: str, model="gpt-4o", temperature=0.7):
        """
        Creates an OpenAI assistant with the given personality.

        Args:

            model (str, optional): Model to use for the assistant (default: "gpt-4").
            temperature (float, optional): Sampling temperature (default: 0.7).

        Returns:
            dict: The response from the OpenAI API.

        Raises:
            Exception: If the API request fails.
        """

        try:
            assistant = openai.beta.assistants.create(
                model=model,
                instructions=instructions,
                temperature=temperature
            )
            return assistant

        except Exception as e:
            raise Exception(f"Failed to create OpenAI assistant: {e}")

    @staticmethod
    def create_message(thread_id: str, role: str, content: str):

        if role not in ["user", "assistant"]:
            raise ValueError("Not a valid option")
        return openai.beta.threads.messages.create(
            thread_id=thread_id,
            role=role,
            content=content
        )

    def create_thread(self):
        """
        Creates a thread using OpenAI beta.threads API.

        Args:

        Returns:
            dict: The response from the OpenAI API.

        Raises:
            Exception: If the API request fails.
        """
        try:
            thread = openai.beta.threads.create()
            return thread
        except Exception as e:
            raise Exception(f"Failed to create thread: {e}")

    @staticmethod
    def fine_tune_model(training_file: str, model="gpt-4o-2024-08-06"):
        return openai.fine_tuning.jobs.create(
            model=model,
            training_file=training_file
        )

    @staticmethod
    def list_messages(thread_id: str):
        messages = openai.beta.threads.messages.list(thread_id)
        return messages

    def process_message(self, message: str, instructions: str, model: str = None, thread_id=None):

        thread_id = thread_id or self.create_thread().id
        print(thread_id)
        model = model or self.default_model

        assistant = self.create_assistant(model=model, instructions=instructions)

        self.create_message(thread_id, "user", message)

        run = self.run_thread(thread_id, assistant.id)

        if run.status == 'completed':
            messages = self.list_messages(thread_id)
            return messages
        else:
            print(run.status)
            return None

    def retrieve_thread(self, thread_id):
        """
        Retrieves an existing thread given its thread ID.

        Args:
            thread_id (str): The ID of the thread to retrieve.

        Returns:
            dict: The response from the OpenAI API.

        Raises:
            Exception: If the API request fails.
        """
        try:
            thread = openai.beta.threads.retrieve(thread_id=thread_id)
            return thread
        except Exception as e:
            raise Exception(f"Failed to retrieve thread: {e}")

    def run_thread(self, thread_id, assistant_id):
        """
        Adds a user message to the thread and runs the assistant logic.

        Args:
            thread_id (str): The ID of the thread.
            user_message (str): The user's input message.

        Returns:
            dict: The response from the OpenAI API.

        Raises:
            Exception: If the API request fails.
        """
        try:
            response = openai.beta.threads.runs.create_and_poll(
                thread_id=thread_id,
                assistant_id=assistant_id,
            )

            return response
        except Exception as e:
            raise Exception(f"Failed to run thread: {e}")

    def upload_file(self, filename: str):
        with open(filename, "rb") as f:

            return openai.files.create(
                file=f,
                purpose="fine-tune"
            )


if __name__ == "__main__":
    # print(OpenAI().upload_file("training_data.jsonl"))
    file_id = "file-4S26qeSTZQyQndySde9TTJ"

    print(OpenAI().fine_tune_model(training_file=file_id))



