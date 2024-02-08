# Doc-Proofreader

A simple document proofreading tool that utilizes OpenAI's GPT-4 model.

## Setting Up

### 1. Install Python.

Download and install Python from the official website. Ensure to check "Add Python to PATH" during installation.

The version of Python this repo was tested with was `3.11.6`, but an earlier version, like `3.10`, should probably work.

### 2. Set up the virtual environment.

Navigate to your project folder in the command line and run:

```bash
python -m venv .doc-proofreader_venv
```

The project folder is defined as `doc-proofreader` -- the top level folder of this git repository.

### 3. Activate the virtual environment.

If you use VSCode, it should automatically recognize the new environment. If you don't use VSCode, run:

- Windows: Run `.doc-proofreader_venv\Scripts\activate`.
- MacOS/Linux: Run `source .doc-proofreader_venv/bin/activate`.

### 4. Install the dependencies in the virtual environment.

Navigate to your project folder in the command line and run:

```bash
pip install .
```

### 5. Store your GPT token

Store your GPT token by putting it in a file OR adding it to your environment variables.

#### Method 1. Store in a File (recommended method)

This option is probably the simplest for beginners!

- Create a file called `.env` within the project folder
- Add `OPENAI_API_KEY=your_api_key_here` to the file. Don't forget to save!

If you're running on macOS/Linux, the following two lines will create the file and add the token to it:
```bash
touch ./doc_proofreader/.env
echo 'OPENAI_API_KEY="your_api_key_here"' >> ./doc_proofreader/.env
```

#### Method 2. Add the key to the environment variables

There are two ways to do this. One is temporary, the other is permanent.

**A. Export on command line (temporary).**

You will need to re-run this command every time you open a new command line window.

```bash
export OPENAI_API_KEY="YourAPIKeyHere"
```

**B. Add to system or user environment variables (permanent). You only need to do this once.**

**Windows:** Press the Windows key. Search your applications for "Environment Variables". Add the GPT token as an environment variable.

**MacOS:** Edit the `~/.zshrc` file. Add the line:

```bash
export OPENAI_API_KEY="YourAPIKeyHere"
```

Then run:

```bash
source ~/.zshrc
```

**Linux:** Edit the `~/.bashrc` file. Add the same line as for MacOS, above. Then run:

```bash
source ~/.bashrc
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

## Common Issues and Solutions

### Issue 1: ModuleNotFoundError for `openai`

**Symptom:** Error indicating the `openai` module is not found.  This dependency should be included if all setup steps are followed.

**Solution:** Install the `openai` package within your virtual environment using `pip install openai`.

### Issue 2: Providing the OpenAI API Key

**Symptom:** Uncertainty about where to add the OpenAI API key.

**Solution:** 
- Create a `.env` file in your project directory.
- Add `OPENAI_API_KEY=your_api_key_here` to the file.
- Ensure `python-dotenv` is installed using `pip install python-dotenv`. This dependency should be included if all setup steps are followed.

## Contact

If you need help or want to report a bug, please DM caerulex on discord.
