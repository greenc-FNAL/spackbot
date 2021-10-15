# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import random
import spackbot.helpers as helpers


async def tell_joke(gh):
    """
    Tell a joke to ease the PR tension!
    """
    joke = await gh.getitem(
        "https://official-joke-api.appspot.com/jokes/programming/random"
    )
    joke = joke[0]
    return f"> {joke['setup']}\n *{joke['punchline']}*\n😄️"


def say_hello():
    """
    Respond to saying hello.
    """
    messages = [
        "Hello!",
        "Hi! How are you?",
        "👋️",
        "Hola!",
        "Hey there!",
        "Howdy!",
        "こんにちは！",
    ]
    return random.choice(messages)


commands_message = f"""
You can interact with me in many ways!

- `{helpers.botname} hello`: say hello and get a friendly response back!
- `{helpers.botname} help` or `{helpers.botname} commands`: see this message
- `{helpers.botname} run pipeline` or `{helpers.botname} re-run pipeline`: to request a new run of the GitLab CI pipeline
- `{helpers.botname} fix style` if you have write and would like me to run `spack style --fix` for you.
- `{helpers.botname} maintainers` or `{helpers.botname} request review`: to look for and assign reviewers for the pull request.

I'll also help to label your pull request and assign reviewers!
If you need help or see there might be an issue with me, open an issue [here](https://github.com/spack/spack-bot/issues)
"""

style_message = """
It looks like you had an issue with style checks! To fix this, you can run:

```bash
$ spack style --fix
```

And then update the pull request here.
"""

maintainer_request = """
It looks like you are opening an issue about a package, and we've found maintainers that might be able to help!

{maintainers}

"""


multiple_packages = """
Hey there! I noticed that you are adding or updating multiple packages:\n\n

{packages}

To get a speedier review for each, I'd like to suggest that you break this into multiple pull requests, with one per package.
"""


non_reviewers_comment = """\
  @{non_reviewers} can you review this PR?

  This PR modifies the following package(s), for which you are listed as a maintainer:

  * {packages_with_maintainers}
"""

no_maintainers_comment = """\
Hi @{author}! I noticed that the following package(s) don't yet have maintainers:

* {packages_without_maintainers}

Are you interested in adopting any of these package(s)? If so, simply add the following to the package class:
```python
    maintainers = ['{author}']
```
If not, could you contact the developers of this package and see if they are interested? You can quickly see who has worked on a package with `spack blame`:

```bash
$ spack blame {first_package_without_maintainer}
```
Thank you for your help! Please don't add maintainers without their consent.

_You don't have to be a Spack expert or package developer in order to be a "maintainer," it just gives us a list of users willing to review PRs or debug issues relating to this package. A package can have multiple maintainers; just add a list of GitHub handles of anyone who wants to volunteer._
"""
