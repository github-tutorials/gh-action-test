def get_step_message(log, start, end, message):
    if end not in log:
        return ""
    return (
        message
        + "\n\n<details>\n```\n"
        + log[log.find(start) + len(start) + 1 : log.find(end) - 1]
        + "\n```\n</details>\n\n"
    )


with open("linting_output.txt", "r") as f:
    log = f.read()

message = ""

# black
message += get_step_message(
    log,
    start="### Running black ###",
    end="Problems detected by black",
    message=(
        "- black detected issues. Please run `black .` locally and push the changes. "
        "Here you can see the detected issues. Note that running black might "
        "also fix some of the issues which might be detected by `flake8`."
    ),
)

# flake8
message += get_step_message(
    log,
    start="### Running flake8 ###",
    end="Problems detected by flake8",
    message=(
        "- flake8 detected issues. Please fix them locally and push the changes. "
        "Here you can see the detected issues."
    ),
)

# mypy
message += get_step_message(
    log,
    start="### Running mypy ###",
    end="Problems detected by mypy",
    message=(
        "- mypy detected issues. Please fix them locally and push the changes. "
        "Here you can see the detected issues."
    ),
)

# cython-lint
message += get_step_message(
    log,
    start="### Running cython-lint ###",
    end="Problems detected by cython-lint",
    message=(
        "- cython-lint detected issues. Please fix them locally and push the changes. "
        "Here you can see the detected issues."
    ),
)

# deprecation order
message += get_step_message(
    log,
    start="### Checking for bad deprecation order ###",
    end="Problems detected by deprecation order check",
    message=(
        "- deprecation order check detected issues. Please fix them locally and "
        "push the changes. Here you can see the detected issues."
    ),
)

# doctest directives
message += get_step_message(
    log,
    start="### Checking for default doctest directives ###",
    end="Problems detected by doctest directive check",
    message=(
        "- doctest directive check detected issues. Please fix them locally and "
        "push the changes. Here you can see the detected issues."
    ),
)

# joblib imports
message += get_step_message(
    log,
    start="### Checking for joblib imports ###",
    end="Problems detected by joblib import check",
    message=(
        "- joblib import check detected issues. Please fix them locally and "
        "push the changes. Here you can see the detected issues."
    ),
)

if not len(message):
    # no issues detected, so this script "fails"
    exit(1)

message = (
    "## Linting issues\n\n"
    "This PR is introducing linting issues. Here's a summary of the issues. "
    "Note that you can avoid having linting issues by enabling `pre-commit` "
    "hooks. Instructions to install them can be found [here]("
    "https://scikit-learn.org/dev/developers/contributing.html#how-to-contribute)."
    "\n\n"
) + message

print(message)
