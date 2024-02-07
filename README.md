# Doc-Proofreader

A simple document proofreading tool that utilizes OpenAI's GPT-4 model.

## Setting Up

1. Install Python.

Google a tutorial online for your respective operating system if you don't have it already. The version of Python this repo was tested with was `3.11.6`, but an earlier version, like `3.10`, should probably work.

2. Set up the environment.

```bash
python -m venv .doc-proofreader_venv
```

3. Activate the environment.

If you use VSCode, it should automatically recognize the new environment. If you don't use VSCode, run:

```bash
source .doc-proofreader_venv/bin/activate
```

4. Install the dependencies.

```bash
pip install .
```

5. Create and Populate Environment Variables

For Unix/Linx
```bash
touch ./doc_proofreader/.env
echo 'OPENAI_API_KEY="YourAPIKeyHere"' >> ./doc_proofreader/.env
```
Or, if exporting

```bash
export OPENAI_API_KEY="YourAPIKeyHere"
```

## Usage

Run using this command:

```bash
python -m doc_proofreader "path to your docx file"
```

You can pass additional information/instructions to GPT-4, custom to your document, following this example:

```bash
python -m doc_proofreader "path to your docx file" --additional-instructions "your custom instructions"
```

Custom instructions might look like, `"half elf" should not be corrected to "half-elf".`

You should be able to run this example as-is:

```bash
python -m doc_proofreader "./tests/resources/test_doc.docx" --additional-instructions '"half elf" should not be corrected to "half-elf".'
```

## Contact

If you need help or want to report a bug, please DM caerulex on discord.
