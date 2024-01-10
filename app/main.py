from openai import OpenAI
import os


client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))


def main() -> None:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "What is duck-typing?"
            }
        ],
        model="gpt-3.5-turbo"
    )
    print('\n'.join(choice.message.content for choice in chat_completion.choices))


if __name__ == '__main__':
    main()
