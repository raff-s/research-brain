# Research second brain

This Python program loads data from websites stores the embeddings in a vector DB and allows you to query the stored data passing it to GPT to make it easy to digest.
This allows you to create a nice resource DB of useful content that you can query instead of trying to remember all the details.

## Setup

```sh
pip install -r requirements.txt
```

Setup your `OPENAI_API_KEY` in a `.env` file or make it available in your environment

## Usage

### Load data

```sh
python scripts/load_data.py "https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/" "https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/"
```

### Ask questions

```sh
python app.py "What is copilot?"

Answer:
GitHub Copilot is an AI-powered coding assistant developed by GitHub in collaboration with OpenAI. It uses machine learning models to generate code suggestions and help developers write code more efficiently. Copilot can provide code completions, suggest whole lines or blocks of code, and even generate entire functions based on the context of the code being written. It learns from millions of lines of code from public repositories and adapts to the coding style and patterns of individual developers.


Sources:
https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/
https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/
https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/
https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/


python app.py "How to write better prompts?"

Answer:
To write better prompts with GitHub Copilot, you can follow these three best practices:

1. Set the stage with a high-level goal: When starting with a blank file or empty codebase, provide a big picture description of what you want to build or accomplish. This helps prime GitHub Copilot with context before diving into the details. Think of it as having a conversation with someone and breaking down the problem together.

2. Use code blocks, individual lines of code, or natural language comments: Developers can write code blocks, individual lines of code, or comments in their IDE to generate specific suggestions from GitHub Copilot. These instructions or comments guide GitHub Copilot to provide the desired coding suggestions.

3. Provide specific details for the desired output: When crafting prompts, be specific about the desired output from the generative AI coding tool. This can include details such as the functionality, features, or behavior you want to achieve. The more specific and clear you are, the better GitHub Copilot can generate accurate results.

Remember, these best practices may vary depending on the specific problem you are working on and the model of GitHub Copilot. Prompt crafting is an iterative process, so it's important to experiment, learn, and adjust your prompts based on the results you get.


Sources:
https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/
https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/
https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/
https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/
```

## Notes

This is setup as a throw away solution, if you want to use it to research more than one topic consider using a different vector DB or at least setup [collections](https://github.com/chroma-core/chroma) to organize the data better
