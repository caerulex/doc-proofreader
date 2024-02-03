# Copyright caerulex 2024

"""User prompts."""

USER_PROMPT_1 = """
Do NOT repeat the provided passage. Only output mistakes, if there are any! Do not invent or fabricate mistakes where none exist.
Do not change any formatting, such as bold or italics HTML tags unless:
1. The tag does not correctly include ending punctuation. For instance, it would be correct to change `on</i>.` to `on.</i>`.

Go sentence by sentence. Decompose the sentence into subject/verb/etc. to ensure you properly assess it for errors.
IF AND ONLY IF YOU ENCOUNTER A SENTENCE WITH AN ERROR:
1. Start with the "＊" character.
2. Write out the corrected sentence with all errors corrected. Do NOT repeat the original sentence. Put brackets around all changes to highlight them within the revised sentence. I.e. given: `The down was beautiful.`, output: `The [town] was beautiful.`.
3. After the sentence, call out the changed portion with the format [<original>] -> [<fixed>]. I.e. [down -> town].
Here is another example:
＊Even if the drayavin had razed the city hours after leaving Shevenar, the longest these people [could have been in hiding] was five days. [could be in hiding] -> [could have been in hiding]

If the original and revised sentence are identical, no error was found.
If a sentence does NOT have an error, output NOTHING and move on to the next sentence.

If there are no errors in the entire passage, say that no errors were found.
"""

USER_PROMPT_2 = """
The story is written in third person past tense.
In this story, "tier one" and "tier two" up to "tier X" are considered nouns describing a tier of power. So the sentence, "there were two tier one threats" should NOT be corrected to "there were two-tier one threats" because there are TWO threats that are both TIER ONE.
"half elf" should not be corrected to "half-elf".
"""

USER_PROMPT_3 = """
Thank you for your efforts, I really appreciate it :) I will give you a 20 percent bonus if you find every mistake and correctly report when there are no errors.
"""
